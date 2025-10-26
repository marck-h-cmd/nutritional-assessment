from owlready2 import *

onto = get_ontology("http://nutricion.org/onto.owl")

with onto:
    class Alimento(Thing): pass
    class calorias(DataProperty, FunctionalProperty): 
        domain = [Alimento]
        range = [float]
    class proteinas_gramos(DataProperty, FunctionalProperty): 
        domain = [Alimento]
        range = [float]
