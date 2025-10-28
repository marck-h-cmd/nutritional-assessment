import random

def es_compatible_con_restricciones(alimento, restricciones_usuario, onto, return_razon=False):
    """
    Verifica si un alimento es compatible con una lista de restricciones.
    Si return_razon es True, devuelve una tupla (bool, str) con el motivo.
    """
    if not restricciones_usuario:
        return (True, None) if return_razon else True

    restricciones_alimento = list(alimento.incompatibleCon)
    
    # Razón 1: Incompatibilidad directa
    for restriccion_usuario in restricciones_usuario:
        for restriccion_alimento in restricciones_alimento:
            if restriccion_alimento.name == restriccion_usuario:
                razon = f"Incompatible con la restricción {restriccion_usuario}"
                return (False, razon) if return_razon else False
    
    nutrientes = list(alimento.contiene)
    nutrientes_nombres = [n.name for n in nutrientes]
    
    # Razón 2: Incompatibilidad por nutrientes
    if "RestriccionVegano" in restricciones_usuario and "ProductoAnimal" in nutrientes_nombres:
        razon = "Contiene ProductoAnimal, no apto para Vegano"
        return (False, razon) if return_razon else False
    
    if "RestriccionVegetariano" in restricciones_usuario and "ProductoAnimal" in nutrientes_nombres:
        # Los lácteos y huevos son compatibles con vegetarianos
        if not isinstance(alimento, onto.Lacteo) and alimento.name != "Huevos":
            razon = "Contiene ProductoAnimal, no apto para Vegetariano"
            return (False, razon) if return_razon else False
            
    if "RestriccionSinGluten" in restricciones_usuario and "Gluten" in nutrientes_nombres:
        razon = "Contiene Gluten, no apto para SinGluten"
        return (False, razon) if return_razon else False
        
    if "RestriccionSinLactosa" in restricciones_usuario and "Lactosa" in nutrientes_nombres:
        razon = "Contiene Lactosa, no apto para SinLactosa"
        return (False, razon) if return_razon else False
        
    if "RestriccionDiabetico" in restricciones_usuario and "Azucar" in nutrientes_nombres:
        razon = "Contiene Azucar, no apto para Diabetico"
        return (False, razon) if return_razon else False
        
    # Si pasa todas las validaciones, es compatible
    return (True, None) if return_razon else True