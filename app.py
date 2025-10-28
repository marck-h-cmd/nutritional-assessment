import streamlit as st
from knowledge.ontologia import crear_ontologia
from knowledge.individuos import crear_individuos
from engine.generador_menu import generar_menu_semanal
from ui.estilos import configurar_estilos
from ui.sidebar import mostrar_sidebar
from ui.menu_display import mostrar_menu_generado
from ui.pantalla_inicial import mostrar_pantalla_inicial

st.set_page_config(
    page_title="Asesor Nutricional Personalizado",
    page_icon="",
    layout="wide"
)

configurar_estilos()

st.markdown('<h1 class="main-header">🥗Asesor Nutricional Personalizado</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistema Experto basado en Ontologías y Razonamiento Lógico</p>', unsafe_allow_html=True)

if 'onto' not in st.session_state:
    with st.spinner(" Inicializando sistema experto..."):
        onto = crear_ontologia()
        onto = crear_individuos(onto)
        st.session_state.onto = onto
        st.session_state.ontologia_creada = True

onto = st.session_state.onto

restricciones, objetivo, objetivo_seleccionado, generar = mostrar_sidebar()

if generar:
    with st.spinner(" Generando tu menú personalizado..."):
        menu, insights = generar_menu_semanal(restricciones, objetivo, onto)
    
    mostrar_menu_generado(menu, restricciones, objetivo_seleccionado, insights)
else:
    mostrar_pantalla_inicial()
