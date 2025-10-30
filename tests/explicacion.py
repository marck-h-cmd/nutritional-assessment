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
    
    ejecutar = st.button("🚀 Ejecutar Test de Explicación")

    if alimento_seleccionado and objetivo_seleccionado and ejecutar:
        alimento = alimentos[alimento_seleccionado]
        objetivo = objetivos[objetivo_seleccionado]
        
        st.markdown("### 📋 Explicación")
        
        # Explicación de compatibilidad con objetivo
        es_apropiado = objetivo in alimento.apropiado_para
        if es_apropiado:
            st.success(f"✅ {alimento.name} es apropiado para {objetivo.name} porque:")
        else:
            st.error(f"❌ {alimento.name} no es óptimo para {objetivo.name}")

        # Reglas/criterios simples por objetivo (heurística explicativa)
        criterios = {
            "PerderPeso": {
                "max_calorias": 300,
                "min_proteinas": 10
            },
            "GanarMusculo": {
                "min_proteinas": 20,
                "min_calorias": 200
            },
            "Mantenimiento": {
                "min_proteinas": 10,
                "max_calorias": 600
            },
            "AumentarEnergia": {
                "min_calorias": 250
            }
        }

        reglas = criterios.get(objetivo.name, {})
        razones = []
        contras = []

        calorias = getattr(alimento, "calorias", None)
        proteinas = getattr(alimento, "proteinas_gramos", None)

        if "min_proteinas" in reglas and proteinas is not None:
            if proteinas >= reglas["min_proteinas"]:
                razones.append(f"Proteínas suficientes (≥ {reglas['min_proteinas']}g): {proteinas}g")
            else:
                contras.append(f"Proteínas insuficientes (< {reglas['min_proteinas']}g): {proteinas}g")

        if "max_calorias" in reglas and calorias is not None:
            if calorias <= reglas["max_calorias"]:
                razones.append(f"Calorías contenidas (≤ {reglas['max_calorias']}): {calorias}")
            else:
                contras.append(f"Calorías elevadas (> {reglas['max_calorias']}): {calorias}")

        if "min_calorias" in reglas and calorias is not None:
            if calorias >= reglas["min_calorias"]:
                razones.append(f"Aporta energía (≥ {reglas['min_calorias']} kcal): {calorias}")
            else:
                contras.append(f"Bajo aporte energético (< {reglas['min_calorias']} kcal): {calorias}")

        # Nutrientes presentes
        nutrientes = [getattr(n, "name", str(n)) for n in getattr(alimento, "contiene", [])]

        # Mostrar detalle de por qué decidió eso
        st.markdown("### 🧠 Por qué el sistema decidió esto")
        if razones:
            st.write("- Factores a favor:")
            for r in razones:
                st.write(f"  • {r}")
        if contras:
            st.write("- Factores en contra:")
            for c in contras:
                st.write(f"  • {c}")
        if not razones and not contras:
            st.write("- No hay reglas cuantitativas aplicables; decisión basada en la ontología (`apropiado_para`).")

        # Nutrientes relevantes
        if nutrientes:
            st.write("- Nutrientes identificados:")
            for n in nutrientes:
                st.write(f"  • {n}")
        
        # Información nutricional
        st.markdown("### 🍎 Información Nutricional")
        st.write(f"- Calorías: {alimento.calorias}")
        st.write(f"- Proteínas: {alimento.proteinas_gramos}g")
        
        # Restricciones
        if hasattr(alimento, 'incompatibleCon') and alimento.incompatibleCon:
            st.warning("⚠️ No apto para personas con las siguientes restricciones:")
            for restriccion in alimento.incompatibleCon:
                st.write(f"- {restriccion.name}")