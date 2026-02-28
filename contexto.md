# 🧬 Contexto del ejercicio — Conteo de nucleótidos

## 📌 Problema

Desarrollar un script en Python que analice una secuencia de ADN
y reporte el conteo de nucleótidos.


## 🎯 Requisitos funcionales

- La secuencia estará definida directamente en el script (hardcoded).
- Debe ignorar espacios al inicio y al final.
- Debe convertir la secuencia a mayúsculas.
- Debe contar A, T, G y C.
- Debe calcular la longitud total.
- Debe mostrar los resultados en pantalla.


## ⚙ Requisitos no funcionales

- Código legible y ordenado.
- Uso de nombres descriptivos (snake_case).
- Uso de f-strings para imprimir resultados.
- Uso responsable de IA (documentado en `ai_log.md`).


## 🧠 Análisis

La secuencia puede contener:

- Espacios innecesarios.
- Letras minúsculas.

Por lo tanto, es necesario limpiar la secuencia antes de realizar los cálculos.


## 🧩 Diseño (versión simple)

Pasos generales del algoritmo:

1. Guardar la secuencia en una variable.
2. Limpiar la secuencia (`strip()` y `upper()`).
3. Calcular el conteo de cada nucleótido.
4. Calcular la longitud total.
5. Imprimir los resultados con formato claro.