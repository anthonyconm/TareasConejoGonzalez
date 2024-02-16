import tarea_1_example_solution
import random
import string

# Codigos de retorno esperados
# Caso de éxito => 0

# Errores esperados metodo de separar letras
# Error en caso de que la entrada no sea un string => -16
# Error en caso de un caracter fuera del abecedario => -32
# Error en caso de un string vacio => -48

# Errores esparados metodo de números primos
# Error en caso de que no se pase un número entero => -64
# Error en caso de que el número entero sea mayor a 100 => -80


# Prueba 1
# Verifica todos los casos de error de la solución
def test_casos_error_inversor():
    # Error por número
    estado, res1 = tarea_1_example_solution.invert_case(7)
    assert estado == -16
    assert res1 is None
    estado, res1 = tarea_1_example_solution.invert_case(3.3)
    assert estado == -16
    assert res1 is None
    estado, res1 = tarea_1_example_solution.invert_case(True)
    assert estado == -16
    assert res1 is None
    estado, res1 = tarea_1_example_solution.invert_case(None)
    assert estado == -16
    assert res1 is None

    # Error por caracter fuera del abecedario
    random_punctuation = random.choice(string.punctuation)
    estado, res1 = tarea_1_example_solution.invert_case(random_punctuation)
    assert estado == -32
    assert res1 is None

    # Error por string vacio
    estado, res1 = tarea_1_example_solution.invert_case("")
    assert estado == -48
    assert res1 is None


# Prueba 2
# Verifica casos de exito de la funcion
def test_casos_exito_inversor():
    ascii_range = string.ascii_letters
    estado, res1 = tarea_1_example_solution.invert_case(ascii_range)
    assert estado == 0
    assert res1 == ascii_range.swapcase()


# Prueba 3
# Verifica los casos de error de la funcion de numeros primos
def test_casos_error_primos():
    estado, result = tarea_1_example_solution.numero_primo("Cafe")
    assert estado == -64
    assert result is None

    estado, result = tarea_1_example_solution.numero_primo(True)
    assert estado == -64
    assert result is None

    estado, result = tarea_1_example_solution.numero_primo(3.7)
    assert estado == -64
    assert result is None

    estado, result = tarea_1_example_solution.numero_primo(None)
    assert estado == -64
    assert result is None

    estado, result = tarea_1_example_solution.numero_primo(133)
    assert estado == -80
    assert result is None


# Prueba 4
# Verifica los casos de exito de la funcion de números primos
def test_casos_exito_primos():
    max_sol = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    estado, result = tarea_1_example_solution.numero_primo(100)
    assert estado == 0
    assert result == max_sol

    estado, result = tarea_1_example_solution.numero_primo(23)
    assert estado == 0
    assert result == max_sol[0:9]

    estado, result = tarea_1_example_solution.numero_primo(0)
    assert estado == 0
    assert result == []
