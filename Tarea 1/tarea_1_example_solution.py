# tarea_1_example_solution.py

"""
Código de funciones

método 1: invert_case
"""


def invert_case(cadena):
    """
    Invierte las mayúsculas a minúsculas y viceversa en una cadena,
    verifica primero que el parámetro sea un string, no esté vacío y
    solo contenga letras del abecedario.

    Parámetros:
    cadena (str): La cadena de caracteres a invertir.

    Retorna:
    tupla: Código de error/éxito (-16, -32, -48 para errores, 0 para éxito) y
    la cadena invertida, o None si hay error.

    Códigos de error al estilo Linux:
    -16: EINVAL - Argumento inválido
    -32: EILSEQ - Secuencia de bytes ilegal
    -48: ENOENT - No existe archivo o directorio
    """
    if not isinstance(cadena, str):
        return -16, None  # EINVAL: Argumento inválido
    if cadena == "":
        return -48, None  # ENOENT: No existe archivo o directorio
    if not cadena.isalpha():
        return -32, None  # EILSEQ: Secuencia de bytes ilegal
    return 0, ''.join(char.lower() if char.isupper() else char.upper()
                      for char in cadena)


"""
Método 2: numero_primo
"""


def numero_primo(base):
    """
    Encuentra todos los números primos hasta un número límite dado, verificando
    primero que el parámetro de entrada sea un entero y no sea superior a 100.

    Parámetros:
    base (int): El número hasta el cual buscar números primos.

    Retorna:
    tupla: Código de error/éxito (-64, -80 para errores, 0 para éxito) y
    una lista de números primos, o None si hay error.

    Códigos de error al estilo Linux:
    -64: EDOM - Fuera del dominio matemático
    -80: ERANGE - Resultado fuera de rango
    """
    if isinstance(base, bool) or not isinstance(base, int):
        return -64, None  # EDOM: Fuera del dominio matemático
    if base > 100:
        return -80, None  # ERANGE: Resultado fuera de rango
    if base < 2:
        return 0, []
    primos = [n for n in range(2, base + 1)
              if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
    return 0, primos
