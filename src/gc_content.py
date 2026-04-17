# Hardcoded sequence
dna_sequence = " ATGC "

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.upper()

# Evito que tome a los espacios como caracteres
contador_G = dna_sequence.count("G")
contador_A = dna_sequence.count("A")
contador_T = dna_sequence.count("T")
contador_C = dna_sequence.count("C")

length = contador_G + contador_A + contador_T + contador_C


# Conteos
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")


# Cálculo GC
gc_content = (count_g + count_c) / length * 100

# Output
print(f"GC content: {gc_content:.2f}%")