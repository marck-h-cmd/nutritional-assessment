import random

def es_compatible_con_restricciones(alimento, restricciones_usuario, onto):
    if not restricciones_usuario:
        return True
    
    restricciones_alimento = list(alimento.incompatibleCon)
    
    for restriccion_usuario in restricciones_usuario:
        for restriccion_alimento in restricciones_alimento:
            if restriccion_alimento.name == restriccion_usuario:
                return False
    
    nutrientes = list(alimento.contiene)
    nutrientes_nombres = [n.name for n in nutrientes]
    
    if "RestriccionVegano" in restricciones_usuario:
        if "ProductoAnimal" in nutrientes_nombres:
            return False
    
    if "RestriccionVegetariano" in restricciones_usuario:
        if "ProductoAnimal" in nutrientes_nombres:
            if not isinstance(alimento, onto.Lacteo) and alimento.name != "Huevos":
                return False
    
    if "RestriccionSinGluten" in restricciones_usuario:
        if "Gluten" in nutrientes_nombres:
            return False
    
    if "RestriccionSinLactosa" in restricciones_usuario:
        if "Lactosa" in nutrientes_nombres:
            return False
    
    if "RestriccionDiabetico" in restricciones_usuario:
        if "Azucar" in nutrientes_nombres:
            return False
    
    return True
