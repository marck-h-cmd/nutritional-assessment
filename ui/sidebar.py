import streamlit as st

def mostrar_sidebar():
    objetivo_map = {
        "Perder Peso": "PerderPeso",
        "Ganar Músculo": "GanarMusculo",
        "Mantenimiento": "Mantenimiento",
        "Aumentar Energía": "AumentarEnergia"
    }
    
    with st.sidebar:
        st.header("👤 Perfil de Usuario")
        st.markdown("---")
        
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
        
        st.subheader("🎯 Objetivo Nutricional")
        objetivo_seleccionado = st.selectbox(
            "Selecciona tu objetivo:",
            [""] + list(objetivo_map.keys())
        )
        
        objetivo = objetivo_map.get(objetivo_seleccionado, None)
        
        st.markdown("---")
        
        generar = st.button("🚀 Generar Menú Semanal", type="primary", use_container_width=True)
        
        st.markdown("---")
        st.info("💡 **Tip:** Selecciona tus restricciones y objetivo para obtener un menú personalizado")
    
    return restricciones, objetivo, objetivo_seleccionado, generar
