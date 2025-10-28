import random
from engine.razonador import es_compatible_con_restricciones

def generar_menu_semanal(restricciones, objetivo, onto):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu_semanal = {}
    
    todos_alimentos = list(onto.Alimento.instances())
    
    alimentos_compatibles = [
        a for a in todos_alimentos 
        if es_compatible_con_restricciones(a, restricciones, onto)
    ]
    
    if objetivo:
        obj_instance = onto.search_one(iri=f"*{objetivo}")
        alimentos_objetivo = [
            a for a in alimentos_compatibles
            if obj_instance in list(a.apropiado_para)
        ]
        if alimentos_objetivo:
            alimentos_compatibles = alimentos_objetivo
    
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
    
    return menu_semanal

def calcular_nutricion_comida(alimentos):
    total_calorias = 0
    total_proteinas = 0
    for alimento in alimentos:
        total_calorias += alimento.calorias
        total_proteinas += alimento.proteinas_gramos
    return total_calorias, total_proteinas
