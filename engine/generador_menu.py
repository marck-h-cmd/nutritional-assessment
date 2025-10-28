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
    Genera una explicación en texto legible sobre por qué se creó el menú.
    """
    
    explicacion = f"### 💡 ¿Por qué este menú?"
    
    if restricciones:
        nombres_restricciones = [r.replace('Restriccion', '') for r in restricciones]
        explicacion += f"\n\nTu plan se ha diseñado específicamente para cumplir con tu objetivo de **{objetivo_seleccionado}** y respetando tus restricciones: **{', '.join(nombres_restricciones)}**."
    else:
        explicacion += f"\n\nTu plan se ha diseñado específicamente para cumplir con tu objetivo de **{objetivo_seleccionado}**, sin restricciones alimenticias seleccionadas."
    
    explicacion += "\n\n**1. Selección de Alimentos Clave:**"
    
    if insights.get('candidatos_finales'):
        num_candidatos = len(insights['candidatos_finales'])
        muestra_candidatos = insights['candidatos_finales'][:min(num_candidatos, 5)]
        
        explicacion += f"\nPara ayudarte a conseguir tu objetivo, hemos priorizado alimentos como: **{', '.join([a.name for a in muestra_candidatos])}**. "
        explicacion += f"Estos son especialmente efectivos porque son apropiados para **{objetivo_seleccionado}**."
    else:
        explicacion += "\nNo se encontraron alimentos específicos para tu objetivo, por lo que se usó una base de alimentos compatibles general."

    if insights.get('alimentos_descartados'):
        explicacion += "\n\n**2. Alimentos Excluidos:**"
        explicacion += "\nPara cumplir con tu perfil, hemos evitado ciertos alimentos. Por ejemplo:"
        
        for item in insights['alimentos_descartados'][:2]:
            explicacion += f"\n- **{item['alimento']}** fue excluido por ser incompatible con tu restricción de **{item['razon'].split(' ')[-1]}**."

    conclusion = f"### ✅ Conclusión\n\nEste menú te proporciona una base sólida y balanceada, combinando macronutrientes y micronutrientes para mantenerte con energía y ayudarte a alcanzar tu meta de **{objetivo_seleccionado}**. La variedad de alimentos asegura que obtengas un amplio espectro de vitaminas y minerales."

    return explicacion, conclusion
