import streamlit as st

def mostrar_pantalla_inicial():
    # Sección de características principales
    st.markdown("## 🌟 ¿Qué hace especial a nuestro asesor?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🧠 Entiende tus necesidades</h3>
            <p>Como un nutricionista experto, analiza tus restricciones y objetivos para crear planes personalizados</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Detecta incompatibilidades</h3>
            <p>Identifica automáticamente alimentos que no se adaptan a tu estilo de vida o salud</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Recomienda lo mejor para ti</h3>
            <p>Sugiere menús equilibrados que se ajusten perfectamente a tus metas nutricionales</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Cómo funciona - Versión visual y simple
    st.markdown("## 📋 Así de fácil es usar nuestro sistema")
    
    steps_col1, steps_col2, steps_col3, steps_col4 = st.columns(4)
    
    with steps_col1:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 1rem;">1️⃣</div>
            <h4>Cuéntanos sobre ti</h4>
            <p>Selecciona tus preferencias y objetivos en el panel lateral</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col2:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 1rem;">2️⃣</div>
            <h4>Nuestro sistema analiza</h4>
            <p>Evaluamos miles de combinaciones de alimentos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col3:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 1rem;">3️⃣</div>
            <h4>Filtramos lo adecuado</h4>
            <p>Descartamos lo que no se adapta a tu perfil</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col4:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 1rem;">4️⃣</div>
            <h4>¡Tu menú está listo!</h4>
            <p>Recibe recomendaciones perfectas para ti</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Base de alimentos - Versión visual
    st.markdown("## 🥗 Nuestra amplia base de alimentos")
    
    food_col1, food_col2, food_col3 = st.columns(3)
    
    with food_col1:
        st.markdown("""
        <div class="food-category">
            <h4>🌱 Proteínas Vegetales</h4>
            <p>Tofu • Lentejas • Garbanzos • Quinoa</p>
        </div>
        <div class="food-category">
            <h4>🥦 Vegetales Frescos</h4>
            <p>Brócoli • Espinacas • Zanahorias • Tomates</p>
        </div>
        """, unsafe_allow_html=True)
    
    with food_col2:
        st.markdown("""
        <div class="food-category">
            <h4>🍎 Frutas Naturales</h4>
            <p>Manzanas • Plátanos • Naranjas • Fresas</p>
        </div>
        <div class="food-category">
            <h4>🌾 Granos Integrales</h4>
            <p>Avena • Arroz integral • Pan integral</p>
        </div>
        """, unsafe_allow_html=True)
    
    with food_col3:
        st.markdown("""
        <div class="food-category">
            <h4>🥑 Grasas Saludables</h4>
            <p>Aguacate • Nueces • Aceite de oliva</p>
        </div>
        <div class="food-category">
            <h4>🥛 Alternativas Lácteas</h4>
            <p>Leche de almendra • Yogur vegetal</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Llamada a la acción mejorada
    st.markdown("""
    <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); border-radius: 20px; color: white; margin: 2rem 0;">
        <h2>🚀 ¡Comienza tu viaje saludable hoy!</h2>
        <p style="font-size: 1.3rem; margin: 1rem 0;">Configura tu perfil en el panel lateral y descubre tu menú ideal</p>
        <div style="font-size: 3rem; margin: 1rem 0;">👇</div>
        <p style="font-size: 1.1rem;"><strong>Tu salud merece atención personalizada</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer mejorado
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666; border-top: 1px solid #eee; margin-top: 2rem;">
        <p><strong>🍎 Asesor Nutricional Inteligente</strong></p>
        <p>Desarrollado con tecnología de inteligencia artificial para tu bienestar</p>
    </div>
    """, unsafe_allow_html=True)

# Para usar esta función, simplemente llama:
# mostrar_pantalla_inicial()