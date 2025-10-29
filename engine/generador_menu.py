import random
from engine.razonador import es_compatible_con_restricciones

def generar_menu_semanal(restricciones, objetivo, onto):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu_semanal = {}
    
    todos_alimentos = list(onto.Alimento.instances())
    
    alimentos_compatibles = []
    alimentos_descartados = []

    # Clasificar alimentos y obtener la razón del descarte
    for a in todos_alimentos:
        compatible, razon_descarte = es_compatible_con_restricciones(a, restricciones, onto, return_razon=True)
        if compatible:
            alimentos_compatibles.append(a)
        else:
            alimentos_descartados.append({
                'alimento': a.name,
                'razon': razon_descarte
            })
    
    candidatos_finales = alimentos_compatibles
    if objetivo:
        obj_instance = onto.search_one(iri=f"*{objetivo}")
        alimentos_objetivo = [
            a for a in alimentos_compatibles
            if obj_instance in list(a.apropiado_para)
        ]
        if alimentos_objetivo:
            candidatos_finales = alimentos_objetivo
            alimentos_compatibles = alimentos_objetivo
    
    # Crear el diccionario de insights
    insights = {
        'candidatos_finales': candidatos_finales,
        'alimentos_descartados': alimentos_descartados
    }
    
    proteinas = [a for a in alimentos_compatibles if isinstance(a, onto.Proteina)]
    carbohidratos = [a for a in alimentos_compatibles if isinstance(a, onto.Carbohidrato)]
    vegetales = [a for a in alimentos_compatibles if isinstance(a, onto.Vegetal)]
    frutas = [a for a in alimentos_compatibles if isinstance(a, onto.Fruta)]
    grasas = [a for a in alimentos_compatibles if isinstance(a, onto.Grasa)]
    
    for dia in dias:
        menu_dia = {
            "Desayuno": [],
            "Almuerzo": [],
            "Cena": [],
            "Snacks": []
        }
        
        if carbohidratos:
            menu_dia["Desayuno"].append(random.choice(carbohidratos))
        if frutas:
            menu_dia["Desayuno"].append(random.choice(frutas))
        if proteinas:
            menu_dia["Desayuno"].append(random.choice(proteinas))
        
        if proteinas:
            menu_dia["Almuerzo"].append(random.choice(proteinas))
        if carbohidratos:
            menu_dia["Almuerzo"].append(random.choice(carbohidratos))
        if vegetales and len(vegetales) >= 2:
            menu_dia["Almuerzo"].extend(random.sample(vegetales, 2))
        elif vegetales:
            menu_dia["Almuerzo"].append(random.choice(vegetales))
        
        if proteinas:
            menu_dia["Cena"].append(random.choice(proteinas))
        if vegetales and len(vegetales) >= 2:
            menu_dia["Cena"].extend(random.sample(vegetales, 2))
        elif vegetales:
            menu_dia["Cena"].append(random.choice(vegetales))
        if grasas:
            menu_dia["Cena"].append(random.choice(grasas))
        
        if frutas:
            menu_dia["Snacks"].append(random.choice(frutas))
        if grasas:
            menu_dia["Snacks"].append(random.choice(grasas))
        
        menu_semanal[dia] = menu_dia
    
    return menu_semanal, insights 

def calcular_nutricion_comida(alimentos):
    total_calorias = 0
    total_proteinas = 0
    for alimento in alimentos:
        total_calorias += alimento.calorias
        total_proteinas += alimento.proteinas_gramos
    return total_calorias, total_proteinas

def generar_explicacion(insights, objetivo_seleccionado, restricciones):
    """
    Genera una explicación de trazabilidad, instanciando la regla de inferencia
    para cada alimento evaluado, en el formato Alimento: Regla.
    """
    
    # Plantillas de reglas lógicas. Usaremos .format() para instanciarlas.
    mapa_reglas = {
        "Vegano": "∀x (Vegano(Usuario) ∧ Contiene({alimento}, ProductoAnimal)) → ¬Apto({alimento})",
        "Vegetariano": "∀x (Vegetariano(Usuario) ∧ Contiene({alimento}, ProductoAnimal) ∧ ¬EsLacteo({alimento}) ∧ ¬EsHuevo({alimento})) → ¬Apto({alimento})",
        "SinGluten": "∀x (SinGluten(Usuario) ∧ Contiene({alimento}, Gluten)) → ¬Apto({alimento})",
        "SinLactosa": "∀x (SinLactosa(Usuario) ∧ Contiene({alimento}, Lactosa)) → ¬Apto({alimento})",
        "Diabetico": "∀x (Diabetico(Usuario) ∧ Contiene({alimento}, Azucar)) → ¬Apto({alimento})"
    }
    regla_inclusion = "∀x (Objetivo(Usuario, {objetivo}) ∧ ApropiadoPara({alimento}, {objetivo})) → Recomendar({alimento})"

    explicacion = "### 🔍 Trazabilidad del Razonamiento\n\n"
    explicacion += "**1. Evidencia (Hechos Iniciales):**\n"
    explicacion += "El motor de inferencia partió de los siguientes hechos proporcionados por el usuario:\n"
    
    if restricciones:
        nombres_restricciones = [r.replace('Restriccion', '') for r in restricciones]
        explicacion += f"- **Hecho 1 (Restricciones):** `{', '.join(nombres_restricciones)}`\n"
    else:
        explicacion += "- **Hecho 1 (Restricciones):** `Ninguna`\n"

    explicacion += f"- **Hecho 2 (Objetivo):** `{objetivo_seleccionado}`\n"

    conclusion = "\n**2. Traza de Inferencias por Alimento:**\n"
    conclusion += "Se aplicaron las siguientes reglas de inferencia a la base de conocimiento:\n"

    if insights.get('alimentos_descartados'):
        conclusion += "\n**Inferencias de Exclusión:**\n"
        
        for item in insights['alimentos_descartados'][:3]:
            alimento_nombre = item['alimento']
            motivo = item['razon']
            regla_encontrada = None

            for clave_regla in mapa_reglas:
                if clave_regla in motivo:
                    regla_encontrada = mapa_reglas[clave_regla]
                    break
            
            if regla_encontrada:
                regla_instanciada = regla_encontrada.format(alimento=alimento_nombre)
                conclusion += f"- **{alimento_nombre}:** ```{regla_instanciada}```\n"

    if insights.get('candidatos_finales'):
        conclusion += "\n**Inferencias de Inclusión:**\n"
        
        # Tomamos hasta 3 ejemplos
        for alimento_obj in insights['candidatos_finales'][:3]:
            alimento_nombre = alimento_obj.name
            regla_instanciada = regla_inclusion.format(alimento=alimento_nombre, objetivo=objetivo_seleccionado)
            conclusion += f"- **{alimento_nombre}:** ```{regla_instanciada}```\n"
            
    conclusion += "\n---\n**Resultado Final:** El menú se construye utilizando únicamente los alimentos que resultaron **`Recomendados`**."

    return explicacion, conclusion