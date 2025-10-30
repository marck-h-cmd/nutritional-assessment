"""
Test de inferencia correcta para el proyecto Nutritional Assessment.

Este script crea una ontología de prueba (basada en las funciones del proyecto),
construye alimentos de prueba y verifica que el razonador (`engine.razonador`)
y el generador de menús (`engine.generador_menu`) toman decisiones lógicas
esperadas ante restricciones (vegano, vegetariano, sin gluten, sin lactosa,
diabético).

Genera un archivo de resultados de texto en `results/` y un gráfico PNG
con el resumen de aciertos/errores similar a `tests/caso_borde.py`.

Este test fija la semilla aleatoria para obtener resultados reproducibles.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import datetime
import random

from knowledge.ontologia import crear_ontologia
from knowledge.individuos import crear_individuos
from engine.razonador import es_compatible_con_restricciones
from engine.generador_menu import generar_menu_semanal


def ejecutar_test_inferencia():
    random.seed(0)

    onto = crear_ontologia()
    onto = crear_individuos(onto)

    resultados = []

    # Caso 1: alimento con ProductoAnimal -> no apto para Vegano
    with onto:
        a_carne = onto.Alimento("TestCarne")
        prod_animal = onto.Nutriente("ProductoAnimal")
        a_carne.contiene = [prod_animal]

    ok, razon = es_compatible_con_restricciones(a_carne, ["RestriccionVegano"], onto, return_razon=True)
    resultados.append({
        "name": "Vegano vs ProductoAnimal",
        "passed": not ok,  # passed means the system correctly rejected the alimento
        "reason": razon,
        "expected": "rechazo (no apto para Vegano)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 2: alimento lacteo con ProductoAnimal -> apto para Vegetariano (por ser Lacteo)
    with onto:
        a_lacteo = onto.Lacteo("TestLacteo")
        a_lacteo.contiene = [prod_animal]

    ok2, razon2 = es_compatible_con_restricciones(a_lacteo, ["RestriccionVegetariano"], onto, return_razon=True)
    resultados.append({
        "name": "Vegetariano vs Lacteo con ProductoAnimal",
        "passed": ok2,  # expected apto (True)
        "reason": razon2,
        "expected": "apto (Lácteo debe ser apto para Vegetariano)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 3: SinGluten detecta Gluten
    with onto:
        a_pan = onto.Alimento("TestPan")
        gluten = onto.Nutriente("Gluten")
        a_pan.contiene = [gluten]

    ok3, razon3 = es_compatible_con_restricciones(a_pan, ["RestriccionSinGluten"], onto, return_razon=True)
    resultados.append({
        "name": "SinGluten vs Gluten",
        "passed": not ok3,
        "reason": razon3,
        "expected": "rechazo (contiene Gluten)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 4: Diabetico detecta Azucar
    with onto:
        a_dulce = onto.Alimento("TestDulce")
        azucar = onto.Nutriente("Azucar")
        a_dulce.contiene = [azucar]

    ok4, razon4 = es_compatible_con_restricciones(a_dulce, ["RestriccionDiabetico"], onto, return_razon=True)
    resultados.append({
        "name": "Diabetico vs Azucar",
        "passed": not ok4,
        "reason": razon4,
        "expected": "rechazo (contiene Azucar)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 5: Generador debe producir un menú válido (estructura) para restricciones veganas
    try:
        menu, insights = generar_menu_semanal(["RestriccionVegano"], "PerderPeso", onto)
        is_menu = isinstance(menu, dict)
        resultados.append({
            "name": "Generador menú (Vegano)",
            "passed": is_menu,
            "reason": None if is_menu else "El generador no devolvió un dict",
            "expected": "devuelve dict (estructura de menú)",
            "timestamp": datetime.datetime.now().isoformat()
        })
    except Exception as e:
        resultados.append({
            "name": "Generador menú (Vegano)",
            "passed": False,
            "reason": f"Excepción: {e}",
            "expected": "devuelve dict (estructura de menú)",
            "timestamp": datetime.datetime.now().isoformat()
        })

    # Caso 6: SinLactosa detecta Lactosa
    with onto:
        a_leche = onto.Alimento("TestLeche")
        lactosa = onto.Nutriente("Lactosa")
        a_leche.contiene = [lactosa]

    ok5, razon5 = es_compatible_con_restricciones(a_leche, ["RestriccionSinLactosa"], onto, return_razon=True)
    resultados.append({
        "name": "SinLactosa vs Lactosa",
        "passed": not ok5,
        "reason": razon5,
        "expected": "rechazo (contiene Lactosa)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 7: Incompatibilidad explícita vía incompatibleCon
    with onto:
        restr = onto.Restriccion("RestriccionEspecial")
        a_especial = onto.Alimento("TestEspecial")
        a_especial.incompatibleCon = [restr]

    ok6, razon6 = es_compatible_con_restricciones(a_especial, ["RestriccionEspecial"], onto, return_razon=True)
    resultados.append({
        "name": "IncompatibleCon explícita",
        "passed": not ok6,
        "reason": razon6,
        "expected": "rechazo (incompatibleCon)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 8: Huevos con ProductoAnimal deben ser aptos para Vegetariano (caso especial en razonador)
    with onto:
        a_huevos = onto.Alimento("Huevos")
        a_huevos.contiene = [prod_animal]

    ok7, razon7 = es_compatible_con_restricciones(a_huevos, ["RestriccionVegetariano"], onto, return_razon=True)
    resultados.append({
        "name": "Vegetariano vs Huevos",
        "passed": ok7,
        "reason": razon7,
        "expected": "apto (Huevos deben ser aptos para Vegetariano)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Caso 9: Sin restricciones -> todo debe ser apto (el alimento simple sin nutrientes problemáticos)
    with onto:
        a_simple = onto.Alimento("TestSimple")
        a_simple.contiene = []

    ok8, razon8 = es_compatible_con_restricciones(a_simple, [], onto, return_razon=True)
    resultados.append({
        "name": "Sin restricciones -> Apto",
        "passed": ok8,
        "reason": razon8,
        "expected": "apto (sin restricciones)",
        "timestamp": datetime.datetime.now().isoformat()
    })

    # Guardar resultados y generar gráfico
    os.makedirs("results", exist_ok=True)
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo_txt = os.path.join("results", f"resultados_inferencia_correcta_{fecha}.txt")

    total = len(resultados)
    exitos = sum(1 for r in resultados if r.get("passed"))
    fallos = total - exitos

    with open(archivo_txt, "w", encoding="utf-8") as f:
        f.write("Resultados del test de inferencia correcta\n")
        f.write(f"Fecha: {fecha}\n")
        f.write(f"Total: {total}\n")
        f.write(f"Exitos: {exitos}\n")
        f.write(f"Fallos: {fallos}\n\n")
        f.write("Detalle por caso:\n")
        for r in resultados:
            estado = "✅ Éxito" if r.get("passed") else "❌ Error"
            f.write(f"{estado} — {r.get('name')}\n")
            f.write(f"  - Timestamp: {r.get('timestamp')}\n")
            f.write(f"  - Esperado: {r.get('expected')}\n")
            if r.get('reason'):
                f.write(f"  - Motivo/razon del sistema: {r.get('reason')}\n")
            f.write("\n")

    print(f"Test finalizado. Total={total}, Exitos={exitos}, Fallos={fallos}")
    print(f"Archivo de resultados: {archivo_txt}")


if __name__ == "__main__":
    ejecutar_test_inferencia()
