### 🧪 Casos de prueba manuales

| Entrada        | Resultado esperado                  |
|---------------|-------------------------------------|
| "ATGC"        | A=1, T=1, G=1, C=1, longitud=4      |
| "aaaa"        | A=4, longitud=4                     |
| " at gc "     | A=1, T=1, G=1, C=1, longitud=4      |
| ""            | longitud=0                          |

### ✅ Resultados (completa al correr el programa)

- Caso 1 ("ATGC"):
  - Obtuve: 4
  - ¿Coincide? Sí

- Caso 2 ("aaaa"):
  - Obtuve: 4
  - ¿Coincide? Sí

- Caso 3 (" at gc "):
  - Obtuve: 4
  - ¿Coincide? Si

- Caso 4 (""):
  - Obtuve: 0
  - ¿Coincide? Sí


### 🆕 Casos de prueba para v1.2

Los casos ahora se ejecutan con archivos de entrada. Asumiendo archivos de prueba en la carpeta `data/raw/` o similar:

- `archivo1.txt`: Contenido "ATGC"
- `archivo2.txt`: Contenido "aaaa"
- `archivo3.txt`: Contenido " at gc "
- `archivo4.txt`: Archivo vacío
- `archivo5.txt`: Contenido "ATGCX" (con carácter inválido)
- `noexiste.txt`: Archivo inexistente

Comandos y resultados esperados (ejecutar `python src/nucleotide_count.py <archivo>`):

- `python src/nucleotide_count.py archivo1.txt`
  - Resultado esperado: "La secuencia dada es válida" seguido de A=1, T=1, G=1, C=1, longitud=4

- `python src/nucleotide_count.py archivo2.txt`
  - Resultado esperado: "La secuencia dada es válida" seguido de A=4, T=0, G=0, C=0, longitud=4

- `python src/nucleotide_count.py archivo3.txt`
  - Resultado esperado: "La secuencia dada es válida" seguido de A=1, T=1, G=1, C=1, longitud=4

- `python src/nucleotide_count.py archivo4.txt`
  - Resultado esperado: "Error: El archivo 'archivo4.txt' está vacío."

- `python src/nucleotide_count.py archivo5.txt`
  - Resultado esperado: "La secuencia contiene caracteres inválidos, el/los cuales son {'X'}"

- `python src/nucleotide_count.py noexiste.txt`
  - Resultado esperado: "Error: El archivo 'noexiste.txt' no se encontró."
