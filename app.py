import streamlit as st
import subprocess
import os
import glob
from knowledge.ontologia import crear_ontologia
from knowledge.individuos import crear_individuos
from engine.generador_menu import generar_menu_semanal
from ui.estilos import configurar_estilos
from ui.sidebar import mostrar_sidebar
from ui.menu_display import mostrar_menu_generado
from ui.pantalla_inicial import mostrar_pantalla_inicial
from tests.explicacion import mostrar_explicacion_view

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
TESTS_DIR = os.path.join(BASE_DIR, "tests")

st.set_page_config(
    page_title="Asesor Nutricional Personalizado",
    page_icon="🥗",
    layout="wide"
)

# ESTILOS Y ENCABEZADOS
configurar_estilos()
st.markdown('<h1 class="main-header">🥗 Asesor Nutricional Personalizado</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistema Experto basado en Ontologías y Razonamiento Lógico</p>', unsafe_allow_html=True)

# 🧠 INICIALIZAR ONTOLOGÍA
if 'onto' not in st.session_state:
    with st.spinner("Inicializando sistema experto..."):
        onto = crear_ontologia()
        onto = crear_individuos(onto)
        st.session_state.onto = onto
        st.session_state.ontologia_creada = True

onto = st.session_state.onto


# MENÚ Y FUNCIONALIDAD PRINCIPAL

restricciones, objetivo, objetivo_seleccionado, generar = mostrar_sidebar()

if generar:
    with st.spinner("Generando tu menú personalizado..."):
        menu, insights = generar_menu_semanal(restricciones, objetivo, onto)
    mostrar_menu_generado(menu, restricciones, objetivo_seleccionado, insights)
else:
    mostrar_pantalla_inicial()

#  TEST DE CASOS BORDE (desde la app)
st.markdown("---")
st.markdown("## 🧩 Validación del Sistema — Casos Borde Dinámicos")

st.info(
    "🔍 Este test ejecuta combinaciones límite de restricciones y objetivos "
    "para verificar la robustez del sistema experto. "
    "Incluye casos con ninguna, una, múltiples y todas las restricciones."
)

if st.button("🚀 Ejecutar test de validación"):
    with st.spinner("Ejecutando test de casos borde... Esto puede tardar unos segundos ⏳"):
        try:
            # Ejecutar el script del test
            subprocess.run(["python", "tests/caso_borde.py"], check=True)
            st.success("✅ Test ejecutado correctamente. Se generaron los archivos de resultados.")
            
            # -------------------------------
            # 📊 Mostrar gráfico global
            # -------------------------------
            grafico_global = os.path.join(RESULTS_DIR, "grafico_resultados_borde.png")
            if os.path.exists(grafico_global):
                st.image(grafico_global, caption="📊 Resumen Global del Test de Casos Borde")

            # -------------------------------
            # 📄 Mostrar resumen estadístico y archivo de resultados
            # -------------------------------
            archivos_txt = glob.glob(os.path.join(RESULTS_DIR, "resultados_test_borde_*.txt"))
            if archivos_txt:
                ultimo = sorted(archivos_txt)[-1]
                with open(ultimo, "r", encoding="utf-8") as f:
                    contenido = f.read()

                # ---- Analizar el archivo para calcular estadísticas ----
                lineas = [l.strip() for l in contenido.splitlines() if l.strip()]
                total = None
                for l in lineas[:10]:
                    if "Total Casos Probados" in l:
                        try:
                            total = int(l.split(":")[-1].strip())
                        except:
                            total = None
                        break

                exitos = sum(1 for l in lineas if "✅" in l or "Éxito" in l)
                fallidos = sum(1 for l in lineas if "❌" in l or "Error" in l)

                if total is None:
                    total = exitos + fallidos

                porcentaje_exito = (exitos / total * 100) if total > 0 else 0

                # ---- Mostrar resumen visual ----
                st.markdown("### 📈 Resumen Estadístico del Test")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Casos Totales", total)
                col2.metric("Casos Exitosos", exitos, f"{(exitos/total*100):.1f}%" if total > 0 else "")
                col3.metric("Casos con Error", fallidos, f"{(fallidos/total*100):.1f}%" if total > 0 else "")
                
                # Color del resultado global
                if porcentaje_exito >= 80:
                    color = "✅"
                    estado = "Excelente"
                elif porcentaje_exito >= 60:
                    color = "🟡"
                    estado = "Aceptable"
                else:
                    color = "🔴"
                    estado = "Crítico"

                col4.metric("Tasa de Éxito Global", f"{porcentaje_exito:.2f}%", estado)

                # ---- Mostrar contenido detallado ----
                with st.expander("📋 Ver archivo de resultados completo"):
                    st.text(contenido)
                    
                
            else:
                st.info("No se encontró ningún archivo de resultados `resultados_test_borde_*.txt` en la carpeta del proyecto.")

        except subprocess.CalledProcessError:
            st.error("❌ Error durante la ejecución del test. Verifica el archivo caso_borde.py.")
        except Exception as e:
            st.error(f"⚠️ Error inesperado: {e}")
st.markdown("---")

mostrar_explicacion_view()

st.markdown("---")
st.caption("© 2025 — Sistema Experto Nutricional desarrollado en Python + Streamlit + Ontologías OWL 🧠")
