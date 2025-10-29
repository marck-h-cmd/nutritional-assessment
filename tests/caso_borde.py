import sys
import os
import itertools
import datetime
import matplotlib.pyplot as plt

# AJUSTAR RUTA DEL PROYECTO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# IMPORTS DEL PROYECTO

from knowledge.ontologia import crear_ontologia
from knowledge.individuos import crear_individuos
from engine.generador_menu import generar_menu_semanal


# CONFIGURACIÓN BASE
TODAS_RESTRICCIONES = [
    "RestriccionVegano",
    "RestriccionVegetariano",
    "RestriccionSinGluten",
    "RestriccionSinLactosa",
    "RestriccionDiabetico"
]

OBJETIVOS = [
    "PerderPeso",
    "GanarMusculo",
    "Mantenimiento",
    "AumentarEnergia"
]

ALIMENTOS_PROHIBIDOS = ["Pollo", "Pescado", "Huevo", "Pan", "Yogur", "Queso"]


# FUNCIÓN PRINCIPAL

def ejecutar_test_borde_dinamico():
    onto = crear_ontologia()
    onto = crear_individuos(onto)
    resultados = []
    errores = []

    print("INICIANDO TEST DE CASOS BORDE\n")

    #  DEFINIMOS CASOS BORDE REALES

    casos_borde = [
        (),  # Sin restricciones (mínimo)
        tuple(TODAS_RESTRICCIONES),  # Todas las restricciones (máximo)
    ]

    # Casos con una sola restricción
    casos_borde += [(r,) for r in TODAS_RESTRICCIONES]

    # Dos combinaciones intermedias (nivel medio)
    combinaciones_dobles = list(itertools.combinations(TODAS_RESTRICCIONES, 2))[:2]
    casos_borde += combinaciones_dobles

    print(f"Total de casos borde generados: {len(casos_borde)}\n")

    # EJECUCIÓN DE PRUEBAS
    for restricciones in casos_borde:
        for objetivo in OBJETIVOS:
            try:
                menu, insights = generar_menu_semanal(restricciones, objetivo, onto)
                assert menu and isinstance(menu, dict), "Menú vacío o mal generado"

                # Verificar alimentos prohibidos
                for dia, comidas in menu.items():
                    for tiempo, lista in comidas.items():
                        for alimento in lista:
                            nombre = getattr(alimento, "name", str(alimento))
                            for prohibido in ALIMENTOS_PROHIBIDOS:
                                assert prohibido.lower() not in nombre.lower(), f"X {nombre} no apto para {restricciones}"

                resultados.append((restricciones, objetivo, "OK Éxito"))
                print(f"OK {restricciones if restricciones else 'Sin restricciones'} + {objetivo} -> Menú válido")

            except AssertionError as e:
                error_msg = f"ERROR {restricciones if restricciones else 'Sin restricciones'} + {objetivo} -> {e}"
                errores.append(error_msg)
                print(error_msg)
            except Exception as e:
                error_msg = f"CRASH {restricciones if restricciones else 'Sin restricciones'} + {objetivo} -> Error inesperado: {e}"
                errores.append(error_msg)
                print(error_msg)


    # GUARDAR RESULTADOS EN ARCHIVO
    os.makedirs("results", exist_ok=True)
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    archivo = f"results/resultados_test_borde_{fecha}.txt"

    with open(archivo, "w", encoding="utf-8") as f:
        f.write("RESULTADOS DEL TEST DE CASOS BORDE\n")
        f.write(f"Fecha: {fecha}\n")
        total = len(casos_borde) * len(OBJETIVOS)
        f.write(f"Total Casos Probados: {total}\n\n")

        for r in resultados:
            f.write(f"{r[0]} | {r[1]} -> {r[2]}\n")

        if errores:
            f.write("\nERRORES DETECTADOS:\n")
            for e in errores:
                f.write(f"{e}\n")


    # MÉTRICAS Y RESUMEN
    total = len(casos_borde) * len(OBJETIVOS)
    exitosos = len(resultados)
    fallidos = len(errores)
    porcentaje_exito = (exitosos / total) * 100

    print("\nRESUMEN FINAL")
    print(f"Casos exitosos: {exitosos}")
    print(f"Casos con errores: {fallidos}")
    print(f"Tasa de Éxito: {porcentaje_exito:.2f}%")
    print(f"Resultados guardados en: {archivo}\n")

    resumen = f"""
    RESUMEN ESTADÍSTICO
    -----------------------------
    Casos Totales: {total}
    Casos Exitosos: {exitosos}
    Casos Fallidos: {fallidos}
    Porcentaje de Éxito: {porcentaje_exito:.2f}%
    -----------------------------
    """
    print(resumen)


    # GRAFICAR RESULTADOS GLOBALES

    etiquetas = ['Casos Exitosos', 'Casos con Error']
    valores = [exitosos, fallidos]
    colores = ['#2ECC71', '#E74C3C']

    plt.figure(figsize=(6, 5))
    plt.bar(etiquetas, valores, color=colores)
    plt.title("Resumen Global del Test de Casos Borde", fontsize=14, fontweight='bold')
    plt.xlabel("Tipo de Resultado")
    
    plt.ylabel("Cantidad de Casos")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.3, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig("results/grafico_resultados_borde.png", dpi=300)
    plt.show()

    print("Gráfico global generado: grafico_resultados_borde.png")

#  EJECUCIÓN DIRECTA

if __name__ == "__main__":
    ejecutar_test_borde_dinamico()
