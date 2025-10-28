import streamlit as st
from engine.generador_menu import calcular_nutricion_comida
from engine.generador_menu import generar_explicacion

def mostrar_menu_generado(menu, restricciones, objetivo_seleccionado, insights):
    st.success("✅ ¡Menú generado exitosamente!")
    
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
    st.markdown("## 💡 Explicación de tu Plan Personalizado")

    # Generar el texto usando la nueva función
    explicacion, conclusion = generar_explicacion(insights, objetivo_seleccionado, restricciones)

    with st.expander("Ver por qué se eligió este menú"):
        st.markdown(explicacion, unsafe_allow_html=True)
        st.markdown(conclusion, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 📅 Menú Semanal")
    
    tabs = st.tabs(list(menu.keys()))
    
    for tab, dia in zip(tabs, menu.keys()):
        with tab:
            menu_dia = menu[dia]
            
            col1, col2 = st.columns(2)
            
            with col1:
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
            