import streamlit as st
from knowledge.ontologia import crear_ontologia
from knowledge.individuos import crear_individuos

def mostrar_explicacion_view():
    # Inicializar ontología
    onto = crear_ontologia()
    crear_individuos(onto)
    
    st.header("🔍 Validación del Sistema — Test de Explicación")

    # Mapa de alimentos disponibles
    alimentos = {
        alimento.name: alimento 
        for alimento in onto.search(type=onto.Alimento)
    }
    
    # Mapa de objetivos
    objetivos = {
        objetivo.name: objetivo 
        for objetivo in onto.search(type=onto.Objetivo)
    }

    col1, col2 = st.columns(2)
    
    with col1:
        alimento_seleccionado = st.selectbox(
            "Selecciona un alimento:",
            [""] + list(alimentos.keys())
        )
    
    with col2:
        objetivo_seleccionado = st.selectbox(
            "Selecciona un objetivo:",
            [""] + list(objetivos.keys())
        )

    if alimento_seleccionado and objetivo_seleccionado:
        alimento = alimentos[alimento_seleccionado]
        objetivo = objetivos[objetivo_seleccionado]
        
        st.markdown("### 📋 Explicación")
        
        # Explicación de compatibilidad con objetivo
        if objetivo in alimento.apropiado_para:
            st.success(f"✅ {alimento.name} es apropiado para {objetivo.name} porque:")
            st.write(f"- Contiene {alimento.proteinas_gramos}g de proteína")
            st.write("- Contiene los siguientes nutrientes:")
            for nutriente in alimento.contiene:
                st.write(f"  • {nutriente.name}")
        else:
            st.error(f"❌ {alimento.name} no es óptimo para {objetivo.name}")
        
        # Información nutricional
        st.markdown("### 🍎 Información Nutricional")
        st.write(f"- Calorías: {alimento.calorias}")
        st.write(f"- Proteínas: {alimento.proteinas_gramos}g")
        
        # Restricciones
        if hasattr(alimento, 'incompatibleCon') and alimento.incompatibleCon:
            st.warning("⚠️ No apto para personas con las siguientes restricciones:")
            for restriccion in alimento.incompatibleCon:
                st.write(f"- {restriccion.name}")