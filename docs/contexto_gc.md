# 🧬 Contexto del ejercicio — GC Content

## 📌 Problema

Desarrollar un script que calcule el porcentaje de contenido GC
en una secuencia de ADN.

## 🎯 Requisitos funcionales

- La secuencia estará definida directamente en el script.
- Debe ignorar espacios.
- Debe convertir la secuencia a mayúsculas.
- Debe calcular el porcentaje de G y C respecto a la longitud total.
- Debe mostrar el resultado con 2 decimales.

## ⚙ Requisitos no funcionales

- Código legible y ordenado.
- Uso de f-strings para mostrar resultados.
- Evitar división entre cero.
- Uso responsable de IA documentado en `ai_log.md`.

## 🧠 Análisis

El porcentaje GC se calcula como:

(G + C) / longitud_total * 100

Debe considerarse el caso donde la longitud sea 0.

## 🧩 Diseño (versión simple)

1. Guardar la secuencia.
2. Limpiar la secuencia.
3. Contar G y C.
4. Calcular la longitud total.
5. Calcular porcentaje.
6. Imprimir resultado con formato adecuado.