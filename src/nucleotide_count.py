import argparse

def clean_sequence(secuencia):
    """
    Limpia la secuencia: elimina espacios y convierte a mayúsculas.
    
    Args:
        secuencia (str): Secuencia de DNA cruda
    
    Returns:
        str: Secuencia limpia
    """
    return secuencia.strip().upper()

def car_invalidos(secuencia):
    """
    Regresa los caracteres invalidos encontrados dentro de la secuencia
    
    Args:
        secuencia (str): Secuencia de DNA
    
    Returns:
        set: Set de caracteres inválidos
    """
    bases_validas = {"A", "C", "G", "T"}
    return set(secuencia) - bases_validas

def count_nucleotides(secuencia):
    """
    Cuenta las ocurrencias de cada nucleótido en la secuencia.
    
    Args:
        secuencia (str): Secuencia de DNA limpia
    
    Returns:
        dict: Diccionario con conteos de G, A, T, C
    """
    return {
        "G": secuencia.count("G"),
        "A": secuencia.count("A"),
        "T": secuencia.count("T"),
        "C": secuencia.count("C")
    }

def print_results(counts, length):
    """
    Imprime los resultados de los conteos y longitud.
    
    Args:
        counts (dict): Diccionario con conteos
        length (int): Longitud de la secuencia
    """
    print(f"Presencia de G: {counts['G']}")
    print(f"Presencia de A: {counts['A']}")
    print(f"Presencia de T: {counts['T']}")
    print(f"Presencia de C: {counts['C']}")
    print(f"Longitud de la secuencia: {length}")

def setup_argparse():
    
    parser = argparse.ArgumentParser(description="Contar nucleótidos en una secuencia de DNA")
    parser.add_argument("input_file", help="Archivo de texto que contiene la secuencia de DNA")
    
    return parser.parse_args()

def main():
   
    # Configuración de argparse
    args = setup_argparse()
    
    # Lectura del archivo
    try:    
        with open(args.input_file, 'r') as file:
            secuencia_adn = file.read()
            
            if secuencia_adn.strip() == "":
                print(f"Error: El archivo '{args.input_file}' está vacío.")
                return
            
    except FileNotFoundError:
        print(f"Error: El archivo '{args.input_file}' no se encontró.")
        return
     
    # Limpieza
    secuencia_limpia = clean_sequence(secuencia_adn)

    # Verificación de datos
    invalidos = car_invalidos(secuencia_limpia)

    # Regreso los resultados de la función 
    if invalidos:
        print(f"La secuencia contiene caracteres inválidos, el/los cuales son {invalidos}")
    else:
        print("La secuencia dada es válida (acepta A, C, G, T en mayúsculas o minúsculas).")
        
        # Conteos
        counts = count_nucleotides(secuencia_limpia)
        length = sum(counts.values())
        
        # Output
        print_results(counts, length)

        
    