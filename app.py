import streamlit as st
from owlready2 import *
import random
from datetime import datetime
import sys
import os

# Configuración de la página
st.set_page_config(
    page_title="Asesor Nutricional Personalizado",
    page_icon="🥗",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .meal-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    .day-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        color: black;
    }
    .nutrient-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        border-radius: 20px;
        background: #f0f0f0;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .info-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def crear_ontologia():
    """Crea y configura la ontología de nutrición"""
 
    default_world.ontologies.clear()

    onto = get_ontology("http://www.nutricion.org/onto.owl")

    with onto:
        # Clases principales
        class Alimento(Thing): pass
        class Nutriente(Thing): pass
        class Restriccion(Thing): pass
        class Objetivo(Thing): pass
        class ComidaDiaria(Thing): pass

        # Subclases de Alimento
        class Proteina(Alimento): pass
        class Carbohidrato(Alimento): pass
        class Vegetal(Alimento): pass
        class Fruta(Alimento): pass
        class Lacteo(Alimento): pass
        class Grasa(Alimento): pass

        # Subclases de Restriccion
        class Vegetariano(Restriccion): pass
        class Vegano(Restriccion): pass
        class SinGluten(Restriccion): pass
        class SinLactosa(Restriccion): pass
        class Diabetico(Restriccion): pass

        # Propiedades de objeto
        class contiene(ObjectProperty):
            domain = [Alimento]
            range = [Nutriente]

        class incompatibleCon(ObjectProperty):
            domain = [Alimento]
            range = [Restriccion]

        class apropiado_para(ObjectProperty):
            domain = [Alimento]
            range = [Objetivo]

        # Propiedades de datos
        class calorias(DataProperty, FunctionalProperty):
            domain = [Alimento]
            range = [int]

        class proteinas_gramos(DataProperty, FunctionalProperty):
            domain = [Alimento]
            range = [float]

        class es_apto(DataProperty, FunctionalProperty):
            domain = [Alimento]
            range = [bool]

    # ---------------- INDIVIDUOS ---------------- #

    # Nutrientes (nombres únicos)
    proteina_nutriente = onto.Nutriente("Nutriente_Proteina")
    carbohidrato_nutriente = onto.Nutriente("Nutriente_Carbohidrato")
    fibra = onto.Nutriente("Fibra")
    vitaminas = onto.Nutriente("Vitaminas")
    minerales = onto.Nutriente("Minerales")
    grasas_saludables = onto.Nutriente("GrasasSaludables")
    producto_animal = onto.Nutriente("ProductoAnimal")
    gluten = onto.Nutriente("Gluten")
    lactosa = onto.Nutriente("Lactosa")
    azucar = onto.Nutriente("Azucar")

    # Restricciones
    rest_vegetariano = onto.Vegetariano("RestriccionVegetariano")
    rest_vegano = onto.Vegano("RestriccionVegano")
    rest_sin_gluten = onto.SinGluten("RestriccionSinGluten")
    rest_sin_lactosa = onto.SinLactosa("RestriccionSinLactosa")
    rest_diabetico = onto.Diabetico("RestriccionDiabetico")

    # Objetivos
    obj_perder_peso = onto.Objetivo("PerderPeso")
    obj_ganar_musculo = onto.Objetivo("GanarMusculo")
    obj_mantenimiento = onto.Objetivo("Mantenimiento")
    obj_energia = onto.Objetivo("AumentarEnergia")

    # ---------------- ALIMENTOS ---------------- #

    # PROTEÍNAS
    pollo = onto.Proteina("Pollo")
    pollo.calorias = 165
    pollo.proteinas_gramos = 31.0
    pollo.contiene = [proteina_nutriente, producto_animal]
    pollo.incompatibleCon = [rest_vegetariano, rest_vegano]
    pollo.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    pescado = onto.Proteina("Pescado")
    pescado.calorias = 140
    pescado.proteinas_gramos = 26.0
    pescado.contiene = [proteina_nutriente, producto_animal, grasas_saludables]
    pescado.incompatibleCon = [rest_vegetariano, rest_vegano]
    pescado.apropiado_para = [obj_ganar_musculo, obj_perder_peso]

    huevos = onto.Proteina("Huevos")
    huevos.calorias = 155
    huevos.proteinas_gramos = 13.0
    huevos.contiene = [proteina_nutriente, producto_animal]
    huevos.incompatibleCon = [rest_vegano]
    huevos.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    tofu = onto.Proteina("Tofu")
    tofu.calorias = 76
    tofu.proteinas_gramos = 8.0
    tofu.contiene = [proteina_nutriente]
    tofu.apropiado_para = [obj_ganar_musculo, obj_perder_peso, obj_mantenimiento]

    lentejas = onto.Proteina("Lentejas")
    lentejas.calorias = 116
    lentejas.proteinas_gramos = 9.0
    lentejas.contiene = [proteina_nutriente, fibra, minerales]
    lentejas.apropiado_para = [obj_mantenimiento, obj_perder_peso]

    garbanzos = onto.Proteina("Garbanzos")
    garbanzos.calorias = 164
    garbanzos.proteinas_gramos = 8.9
    garbanzos.contiene = [proteina_nutriente, fibra]
    garbanzos.apropiado_para = [obj_mantenimiento, obj_energia]

    # CARBOHIDRATOS
    arroz_integral = onto.Carbohidrato("ArrozIntegral")
    arroz_integral.calorias = 112
    arroz_integral.proteinas_gramos = 2.6
    arroz_integral.contiene = [carbohidrato_nutriente, fibra]
    arroz_integral.apropiado_para = [obj_ganar_musculo, obj_mantenimiento]

    quinoa = onto.Carbohidrato("Quinoa")
    quinoa.calorias = 120
    quinoa.proteinas_gramos = 4.4
    quinoa.contiene = [carbohidrato_nutriente, proteina_nutriente, fibra]
    quinoa.apropiado_para = [obj_ganar_musculo, obj_mantenimiento, obj_energia]

    avena = onto.Carbohidrato("Avena")
    avena.calorias = 68
    avena.proteinas_gramos = 2.4
    avena.contiene = [carbohidrato_nutriente, fibra]
    avena.apropiado_para = [obj_energia, obj_mantenimiento]

    papa = onto.Carbohidrato("Papa")
    papa.calorias = 77
    papa.proteinas_gramos = 2.0
    papa.contiene = [carbohidrato_nutriente, vitaminas]
    papa.apropiado_para = [obj_ganar_musculo, obj_energia]

    pan_integral = onto.Carbohidrato("PanIntegral")
    pan_integral.calorias = 247
    pan_integral.proteinas_gramos = 13.0
    pan_integral.contiene = [carbohidrato_nutriente, gluten, fibra]
    pan_integral.incompatibleCon = [rest_sin_gluten]
    pan_integral.apropiado_para = [obj_mantenimiento, obj_energia]

    camote = onto.Carbohidrato("Camote")
    camote.calorias = 86
    camote.proteinas_gramos = 1.6
    camote.contiene = [carbohidrato_nutriente, fibra, vitaminas]
    camote.apropiado_para = [obj_ganar_musculo, obj_energia]

    # VEGETALES
    brocoli = onto.Vegetal("Brocoli")
    brocoli.calorias = 34
    brocoli.proteinas_gramos = 2.8
    brocoli.contiene = [fibra, vitaminas, minerales]
    brocoli.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    espinaca = onto.Vegetal("Espinaca")
    espinaca.calorias = 23
    espinaca.proteinas_gramos = 2.9
    espinaca.contiene = [fibra, vitaminas, minerales]
    espinaca.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    zanahoria = onto.Vegetal("Zanahoria")
    zanahoria.calorias = 41
    zanahoria.proteinas_gramos = 0.9
    zanahoria.contiene = [fibra, vitaminas]
    zanahoria.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    tomate = onto.Vegetal("Tomate")
    tomate.calorias = 18
    tomate.proteinas_gramos = 0.9
    tomate.contiene = [vitaminas, minerales]
    tomate.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    lechuga = onto.Vegetal("Lechuga")
    lechuga.calorias = 15
    lechuga.proteinas_gramos = 1.4
    lechuga.contiene = [fibra, vitaminas]
    lechuga.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    # FRUTAS
    manzana = onto.Fruta("Manzana")
    manzana.calorias = 52
    manzana.proteinas_gramos = 0.3
    manzana.contiene = [fibra, vitaminas]
    manzana.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    platano = onto.Fruta("Platano")
    platano.calorias = 89
    platano.proteinas_gramos = 1.1
    platano.contiene = [carbohidrato_nutriente, vitaminas]
    platano.apropiado_para = [obj_energia, obj_ganar_musculo]

    naranja = onto.Fruta("Naranja")
    naranja.calorias = 47
    naranja.proteinas_gramos = 0.9
    naranja.contiene = [vitaminas, fibra]
    naranja.apropiado_para = [obj_mantenimiento, obj_energia]

    fresas = onto.Fruta("Fresas")
    fresas.calorias = 32
    fresas.proteinas_gramos = 0.7
    fresas.contiene = [vitaminas, fibra]
    fresas.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    # LÁCTEOS
    yogur = onto.Lacteo("Yogur")
    yogur.calorias = 59
    yogur.proteinas_gramos = 10.0
    yogur.contiene = [proteina_nutriente, lactosa, producto_animal]
    yogur.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    yogur.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    queso = onto.Lacteo("Queso")
    queso.calorias = 402
    queso.proteinas_gramos = 25.0
    queso.contiene = [proteina_nutriente, lactosa, producto_animal]
    queso.incompatibleCon = [rest_vegano, rest_sin_lactosa]
    queso.apropiado_para = [obj_ganar_musculo]

    leche_almendra = onto.Lacteo("LecheAlmendra")
    leche_almendra.calorias = 17
    leche_almendra.proteinas_gramos = 0.6
    leche_almendra.contiene = [vitaminas]
    leche_almendra.apropiado_para = [obj_perder_peso, obj_mantenimiento]

    # GRASAS SALUDABLES
    aguacate = onto.Grasa("Aguacate")
    aguacate.calorias = 160
    aguacate.proteinas_gramos = 2.0
    aguacate.contiene = [grasas_saludables, fibra]
    aguacate.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    nueces = onto.Grasa("Nueces")
    nueces.calorias = 654
    nueces.proteinas_gramos = 15.2
    nueces.contiene = [grasas_saludables, proteina_nutriente]
    nueces.apropiado_para = [obj_ganar_musculo, obj_energia]

    aceite_oliva = onto.Grasa("AceiteOliva")
    aceite_oliva.calorias = 884
    aceite_oliva.proteinas_gramos = 0.0
    aceite_oliva.contiene = [grasas_saludables]
    aceite_oliva.apropiado_para = [obj_mantenimiento, obj_ganar_musculo]

    return onto

# Función para verificar compatibilidad (razonamiento backward)
def es_compatible_con_restricciones(alimento, restricciones_usuario, onto):
    """
    Razonamiento hacia atrás para verificar compatibilidad
    Vegano(x) ∧ Contiene(x, ProductoAnimal) → NoApto(x)
    """
    if not restricciones_usuario:
        return True
    
    # Obtener restricciones del alimento
    restricciones_alimento = list(alimento.incompatibleCon)
    
    # Verificar incompatibilidades
    for restriccion_usuario in restricciones_usuario:
        for restriccion_alimento in restricciones_alimento:
            if restriccion_alimento.name == restriccion_usuario:
                return False
    
    # Verificar contenido para reglas específicas
    nutrientes = list(alimento.contiene)
    nutrientes_nombres = [n.name for n in nutrientes]
    
    # Regla: Vegano → No ProductoAnimal
    if "RestriccionVegano" in restricciones_usuario:
        if "ProductoAnimal" in nutrientes_nombres:
            return False
    
    # Regla: Vegetariano → No ProductoAnimal (excepto lácteos/huevos)
    if "RestriccionVegetariano" in restricciones_usuario:
        if "ProductoAnimal" in nutrientes_nombres:
            # Permitir lácteos y huevos para vegetarianos
            if not isinstance(alimento, onto.Lacteo) and alimento.name != "Huevos":
                return False
    
    # Regla: SinGluten → No Gluten
    if "RestriccionSinGluten" in restricciones_usuario:
        if "Gluten" in nutrientes_nombres:
            return False
    
    # Regla: SinLactosa → No Lactosa
    if "RestriccionSinLactosa" in restricciones_usuario:
        if "Lactosa" in nutrientes_nombres:
            return False
    
    # Regla: Diabético → Bajo Azúcar
    if "RestriccionDiabetico" in restricciones_usuario:
        if "Azucar" in nutrientes_nombres:
            return False
    
    return True

# Función para generar menú
def generar_menu_semanal(restricciones, objetivo, onto):
    """Genera un menú semanal personalizado"""
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu_semanal = {}
    
    # Obtener todos los alimentos
    todos_alimentos = list(onto.Alimento.instances())
    
    # Filtrar alimentos compatibles
    alimentos_compatibles = [
        a for a in todos_alimentos 
        if es_compatible_con_restricciones(a, restricciones, onto)
    ]
    
    # Filtrar por objetivo si existe
    if objetivo:
        obj_instance = onto.search_one(iri=f"*{objetivo}")
        alimentos_objetivo = [
            a for a in alimentos_compatibles
            if obj_instance in list(a.apropiado_para)
        ]
        if alimentos_objetivo:
            alimentos_compatibles = alimentos_objetivo
    
    # Categorizar alimentos
    proteinas = [a for a in alimentos_compatibles if isinstance(a, onto.Proteina)]
    carbohidratos = [a for a in alimentos_compatibles if isinstance(a, onto.Carbohidrato)]
    vegetales = [a for a in alimentos_compatibles if isinstance(a, onto.Vegetal)]
    frutas = [a for a in alimentos_compatibles if isinstance(a, onto.Fruta)]
    grasas = [a for a in alimentos_compatibles if isinstance(a, onto.Grasa)]
    
    # Generar menú para cada día
    for dia in dias:
        menu_dia = {
            "Desayuno": [],
            "Almuerzo": [],
            "Cena": [],
            "Snacks": []
        }
        
        # Desayuno
        if carbohidratos:
            menu_dia["Desayuno"].append(random.choice(carbohidratos))
        if frutas:
            menu_dia["Desayuno"].append(random.choice(frutas))
        if proteinas:
            menu_dia["Desayuno"].append(random.choice(proteinas))
        
        # Almuerzo
        if proteinas:
            menu_dia["Almuerzo"].append(random.choice(proteinas))
        if carbohidratos:
            menu_dia["Almuerzo"].append(random.choice(carbohidratos))
        if vegetales and len(vegetales) >= 2:
            menu_dia["Almuerzo"].extend(random.sample(vegetales, 2))
        elif vegetales:
            menu_dia["Almuerzo"].append(random.choice(vegetales))
        
        # Cena
        if proteinas:
            menu_dia["Cena"].append(random.choice(proteinas))
        if vegetales and len(vegetales) >= 2:
            menu_dia["Cena"].extend(random.sample(vegetales, 2))
        elif vegetales:
            menu_dia["Cena"].append(random.choice(vegetales))
        if grasas:
            menu_dia["Cena"].append(random.choice(grasas))
        
        # Snacks
        if frutas:
            menu_dia["Snacks"].append(random.choice(frutas))
        if grasas:
            menu_dia["Snacks"].append(random.choice(grasas))
        
        menu_semanal[dia] = menu_dia
    
    return menu_semanal

# Función para calcular información nutricional
def calcular_nutricion_comida(alimentos):
    total_calorias = 0
    total_proteinas = 0
    for alimento in alimentos:
        total_calorias += alimento.calorias
        total_proteinas += alimento.proteinas_gramos
    return total_calorias, total_proteinas


# INTERFAZ PRINCIPAL
st.markdown('<h1 class="main-header">🥗 Asesor Nutricional Personalizado</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistema Experto basado en Ontologías y Razonamiento Lógico</p>', unsafe_allow_html=True)

# Crear la ontología una sola vez
if 'onto' not in st.session_state:
    with st.spinner("🔄 Inicializando sistema experto..."):
        st.session_state.onto = crear_ontologia()
        st.session_state.ontologia_creada = True

onto = st.session_state.onto

# Sidebar con información del perfil
with st.sidebar:
    st.header("👤 Perfil de Usuario")
    st.markdown("---")
    
    # Restricciones alimenticias
    st.subheader("🚫 Restricciones Alimenticias")
    restricciones = []
    
    if st.checkbox("🌱 Vegano"):
        restricciones.append("RestriccionVegano")
    if st.checkbox("🥚 Vegetariano"):
        restricciones.append("RestriccionVegetariano")
    if st.checkbox("🌾 Sin Gluten"):
        restricciones.append("RestriccionSinGluten")
    if st.checkbox("🥛 Sin Lactosa"):
        restricciones.append("RestriccionSinLactosa")
    if st.checkbox("🍬 Diabético"):
        restricciones.append("RestriccionDiabetico")
    
    st.markdown("---")
    
    # Objetivo nutricional
    st.subheader("🎯 Objetivo Nutricional")
    objetivo_map = {
        "Perder Peso": "PerderPeso",
        "Ganar Músculo": "GanarMusculo",
        "Mantenimiento": "Mantenimiento",
        "Aumentar Energía": "AumentarEnergia"
    }
    
    objetivo_seleccionado = st.selectbox(
        "Selecciona tu objetivo:",
        [""] + list(objetivo_map.keys())
    )
    
    objetivo = objetivo_map.get(objetivo_seleccionado, None)
    
    st.markdown("---")
    
    # Botón de generar
    generar = st.button("🚀 Generar Menú Semanal", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.info("💡 **Tip:** Selecciona tus restricciones y objetivo para obtener un menú personalizado")

# Contenido principal
if generar:
    with st.spinner("🔄 Generando tu menú personalizado..."):
        menu = generar_menu_semanal(restricciones, objetivo, onto)
    
    st.success("✅ ¡Menú generado exitosamente!")
    
    # Mostrar resumen del perfil
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Tu Perfil")
        if restricciones:
            st.write("**Restricciones:**")
            for r in restricciones:
                st.markdown(f"- {r.replace('Restriccion', '')}")
        else:
            st.write("Sin restricciones")
    
    with col2:
        st.markdown("### 🎯 Tu Objetivo")
        if objetivo_seleccionado:
            st.write(f"**{objetivo_seleccionado}**")
        else:
            st.write("Alimentación balanceada general")
    
    st.markdown("---")
    st.markdown("## 📅 Menú Semanal")
    
    # Tabs para cada día
    tabs = st.tabs(list(menu.keys()))
    
    for tab, dia in zip(tabs, menu.keys()):
        with tab:
            menu_dia = menu[dia]
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Desayuno
                st.markdown("### 🌅 Desayuno")
                alimentos_desayuno = menu_dia["Desayuno"]
                if alimentos_desayuno:
                    cals, prots = calcular_nutricion_comida(alimentos_desayuno)
                    st.markdown(f"""
                    <div class="meal-card">
                        <h4>Alimentos:</h4>
                        {''.join([f"<li>{a.name}</li>" for a in alimentos_desayuno])}
                        <br><br>
                        <strong>📊 Total: {cals} kcal | {prots:.1f}g proteína</strong>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Cena
                st.markdown("### 🌙 Cena")
                alimentos_cena = menu_dia["Cena"]
                if alimentos_cena:
                    cals, prots = calcular_nutricion_comida(alimentos_cena)
                    st.markdown(f"""
                    <div class="meal-card">
                        <h4>Alimentos:</h4>
                        {''.join([f"<li>{a.name}</li>" for a in alimentos_cena])}
                        <br><br>
                        <strong>📊 Total: {cals} kcal | {prots:.1f}g proteína</strong>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                # Almuerzo
                st.markdown("### ☀️ Almuerzo")
                alimentos_almuerzo = menu_dia["Almuerzo"]
                if alimentos_almuerzo:
                    cals, prots = calcular_nutricion_comida(alimentos_almuerzo)
                    st.markdown(f"""
                    <div class="meal-card">
                        <h4>Alimentos:</h4>
                        {''.join([f"<li>{a.name}</li>" for a in alimentos_almuerzo])}
                        <br><br>
                        <strong>📊 Total: {cals} kcal | {prots:.1f}g proteína</strong>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Snacks
                st.markdown("### 🍎 Snacks")
                alimentos_snacks = menu_dia["Snacks"]
                if alimentos_snacks:
                    cals, prots = calcular_nutricion_comida(alimentos_snacks)
                    st.markdown(f"""
                    <div class="meal-card">
                        <h4>Alimentos:</h4>
                        {''.join([f"<li>{a.name}</li>" for a in alimentos_snacks])}
                        <br><br>
                        <strong>📊 Total: {cals} kcal | {prots:.1f}g proteína</strong>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Resumen diario
            todos_alimentos = (alimentos_desayuno + alimentos_almuerzo + 
                             alimentos_cena + alimentos_snacks)
            cals_totales, prots_totales = calcular_nutricion_comida(todos_alimentos)
            
            st.markdown(f"""
            <div class="info-box">
                <h3>📊 Resumen del Día</h3>
                <p><strong>Calorías totales:</strong> {cals_totales} kcal</p>
                <p><strong>Proteínas totales:</strong> {prots_totales:.1f}g</p>
            </div>
            """, unsafe_allow_html=True)

else:
    # Pantalla inicial
    st.markdown("## 🎯 Bienvenido al Asesor Nutricional")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="day-card">
            <h3>🧬 Base de Conocimiento</h3>
            <p>Ontología OWL con alimentos, nutrientes y restricciones</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="day-card">
            <h3>🔍 Motor de Inferencia</h3>
            <p>Razonamiento hacia atrás para verificar compatibilidad</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="day-card">
            <h3>🎨 Personalización</h3>
            <p>Menús adaptados a tus necesidades únicas</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Información sobre el sistema
    st.markdown("## 📚 Cómo Funciona el Sistema")
    
    with st.expander("🔬 Sistema Experto con Owlready2", expanded=True):
        st.markdown("""
        ### Arquitectura del Sistema
        
        **1. Base de Conocimiento (BC)**
        - **Ontología OWL** con clases: Alimento, Nutriente, Restricción, Objetivo
        - **Relaciones semánticas**: contiene, incompatibleCon, apropiadoPara
        - **Propiedades**: calorías, proteínas, aptitud
        
        **2. Base de Hechos (BH)**
        - Perfil del usuario con restricciones alimenticias
        - Objetivos nutricionales personalizados
        - Preferencias y necesidades individuales
        
        **3. Motor de Inferencia (MI)**
        - **Razonamiento hacia atrás (Backward Chaining)**
        - Verificación de reglas lógicas:
          - `Vegano(x) ∧ Contiene(x, ProductoAnimal) → NoApto(x)`
          - `SinGluten(x) ∧ Contiene(x, Gluten) → NoApto(x)`
          - `Diabético(x) ∧ Contiene(x, Azúcar) → NoApto(x)`
        """)
    
    with st.expander("🧠 Reglas de Inferencia"):
        st.markdown("""
        ### Lógica de Razonamiento
        
        El sistema aplica las siguientes reglas:
        
        ```
        ∀x (Vegano(Usuario) ∧ Contiene(x, ProductoAnimal)) → ¬Apto(x)
        
        ∀x (Vegetariano(Usuario) ∧ Contiene(x, Carne)) → ¬Apto(x)
        
        ∀x (SinGluten(Usuario) ∧ Contiene(x, Gluten)) → ¬Apto(x)
        
        ∀x (SinLactosa(Usuario) ∧ Contiene(x, Lactosa)) → ¬Apto(x)
        
        ∀x (Objetivo(Usuario, PerderPeso) ∧ Apropiado(x, PerderPeso)) → Recomendar(x)
        ```
        
        **Proceso de Razonamiento:**
        1. El usuario selecciona restricciones y objetivos
        2. El sistema consulta la ontología
        3. Verifica compatibilidad usando backward chaining
        4. Filtra alimentos según reglas lógicas
        5. Genera menú optimizado
        """)
    
    with st.expander("📊 Base de Datos de Alimentos"):
        st.markdown("""
        ### Alimentos en la Ontología
        
        **Proteínas:**
        - 🍗 Pollo, Pescado (no vegano/vegetariano)
        - 🥚 Huevos (no vegano)
        - 🌱 Tofu, Lentejas, Garbanzos (aptos para todos)
        
        **Carbohidratos:**
        - 🌾 Arroz integral, Quinoa, Avena
        - 🥔 Papa, Camote
        - 🍞 Pan integral (contiene gluten)
        
        **Vegetales:**
        - 🥦 Brócoli, Espinaca, Zanahoria
        - 🍅 Tomate, Lechuga
        
        **Frutas:**
        - 🍎 Manzana, Plátano, Naranja
        - 🍓 Fresas
        
        **Grasas Saludables:**
        - 🥑 Aguacate
        - 🌰 Nueces
        - 🫒 Aceite de oliva
        
        **Lácteos:**
        - 🥛 Yogur, Queso (no vegano/sin lactosa)
        - 🌰 Leche de almendra (apta para todos)
        """)
    
    with st.expander("⚙️ Instalación y Requisitos"):
        st.markdown("""
        ### Requisitos del Sistema
        
        ```bash
        # Instalar dependencias
        pip install streamlit owlready2
        
        # Ejecutar la aplicación
        streamlit run app.py
        ```
        
        **Bibliotecas utilizadas:**
        - `streamlit`: Framework para la interfaz web
        - `owlready2`: Manejo de ontologías OWL y razonamiento
        
        **Características:**
        - ✅ Razonamiento lógico automático
        - ✅ Ontología OWL completa
        - ✅ Interfaz moderna y responsive
        - ✅ Generación de menús personalizados
        - ✅ Cálculo nutricional en tiempo real
        """)
    
    # Ejemplo visual de inferencia
    st.markdown("---")
    st.markdown("## 🎓 Ejemplo de Inferencia")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>📥 Entrada</h3>
            <p><strong>Usuario:</strong> Vegano</p>
            <p><strong>Objetivo:</strong> Ganar músculo</p>
            <p><strong>Alimento:</strong> Pollo</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h3>📤 Salida</h3>
            <p><strong>Verificación:</strong></p>
            <p>Vegano(Usuario) ∧ Contiene(Pollo, ProductoAnimal)</p>
            <p>→ <strong>❌ NoApto(Pollo)</strong></p>
            <p><em>Alternativa: Tofu, Lentejas</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Call to action
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;">
        <h2>👈 ¡Comienza Ahora!</h2>
        <p style="font-size: 1.2rem;">Configura tu perfil en el panel lateral y genera tu menú personalizado</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 1rem; color: #666; border-top: 1px solid #eee; margin-top: 2rem;">
        <p><strong>Sistema Experto de Nutrición</strong> | Powered by Owlready2 & Streamlit</p>
        <p>🧬 Ontología OWL | 🔍 Razonamiento Lógico | 🎯 Personalización IA</p>
    </div>
    """, unsafe_allow_html=True)