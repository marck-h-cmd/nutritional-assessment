import streamlit as st

def mostrar_pantalla_inicial():
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
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;">
        <h2>👈 ¡Comienza Ahora!</h2>
        <p style="font-size: 1.2rem;">Configura tu perfil en el panel lateral y genera tu menú personalizado</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 1rem; color: #666; border-top: 1px solid #eee; margin-top: 2rem;">
        <p><strong>Sistema Experto de Nutrición</strong> | Powered by Owlready2 & Streamlit</p>
        <p>🧬 Ontología OWL | 🔍 Razonamiento Lógico | 🎯 Personalización IA</p>
    </div>
    """, unsafe_allow_html=True)
