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


## 🆕 Versión 1.2

### Cambios principales
- El script ahora lee la secuencia desde un archivo de texto especificado por línea de comandos usando `argparse`.
- El código está organizado en funciones separadas para mayor legibilidad y mantenibilidad.
- Se agregó validación para caracteres inválidos (solo se aceptan A, T, G, C, mayúsculas o minúsculas).
- Se maneja errores como archivo no encontrado o archivo vacío.
- La secuencia se limpia (espacios y conversión a mayúsculas) antes del procesamiento.

### Requisitos funcionales actualizados
- La secuencia se lee desde un archivo pasado como argumento.
- Si hay caracteres inválidos, se informa al usuario y el programa termina sin procesar.
- Solo se procesa si la secuencia es válida.

### Diseño actualizado
1. Configurar argparse para recibir el archivo de entrada.
2. Leer el contenido del archivo.
3. Verificar si el archivo existe y no está vacío.
4. Limpiar la secuencia.
5. Validar caracteres.
6. Si válida, contar nucleótidos y calcular longitud.
7. Imprimir resultados.