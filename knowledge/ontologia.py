from owlready2 import *

def crear_ontologia():
    default_world.ontologies.clear()
    onto = get_ontology("http://www.nutricion.org/onto.owl")

    with onto:
        class Alimento(Thing): pass
        class Nutriente(Thing): pass
        class Restriccion(Thing): pass
        class Objetivo(Thing): pass
        class ComidaDiaria(Thing): pass

        class Proteina(Alimento): pass
        class Carbohidrato(Alimento): pass
        class Vegetal(Alimento): pass
        class Fruta(Alimento): pass
        class Lacteo(Alimento): pass
        class Grasa(Alimento): pass

        class Vegetariano(Restriccion): pass
        class Vegano(Restriccion): pass
        class SinGluten(Restriccion): pass
        class SinLactosa(Restriccion): pass
        class Diabetico(Restriccion): pass
        class Hipertenso(Restriccion): pass

        class contiene(ObjectProperty):
            domain = [Alimento]
            range = [Nutriente]

        class incompatibleCon(ObjectProperty):
            domain = [Alimento]
            range = [Restriccion]

        class apropiado_para(ObjectProperty):
            domain = [Alimento]
            range = [Objetivo]

        class calorias(DataProperty, FunctionalProperty):
            domain = [Alimento]
            range = [int]

        class proteinas_gramos(DataProperty, FunctionalProperty):
            domain = [Alimento]
            range = [float]

        class es_apto(DataProperty, FunctionalProperty):
            domain = [Alimento]
            range = [bool]

    return onto
