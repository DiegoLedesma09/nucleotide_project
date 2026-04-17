# Hardcoded sequence
secuencia_adn = "  "

# Limpieza
secuencia_adn = secuencia_adn.strip()
secuencia_adn = secuencia_adn.upper()

# Función de verificación de datos

def car_invalidos(secuencia):
    """
    Regresa los caracteres invalidos encontrados dentro de la secuencia
    
    Args:
        secuencia_adn: (str) Secuencia de DNA
    
    Returns:
        set: Set de caracteres inválidos
        
    """
    
    bases_validas = {"A", "C", "G", "T"}
    
    return set(secuencia) - bases_validas

invalidos = car_invalidos(secuencia_adn)

# Regreso los resultados de la función 
if invalidos:
    print(f"La secuencia contiene caracteres inválidos, el/los cuales son {invalidos}")
    
else:
    print(f"La secuencia dada es válida")

# Conteos
contador_G = secuencia_adn.count("G")
contador_A = secuencia_adn.count("A")
contador_T = secuencia_adn.count("T")
contador_C = secuencia_adn.count("C")

# Para evitar el error de la presencia de espacios
length_2 = contador_G + contador_C + contador_A + contador_T


# Output
print(f"Presencia de G: {contador_G}")
print(f"Presencia de A: {contador_A}")
print(f"Presencia de T: {contador_T}")
print(f"Presencia de C: {contador_C}")
print(f"Longitud de la secuencia: {length_2}")


    
    