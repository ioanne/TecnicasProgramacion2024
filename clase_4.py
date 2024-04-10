
def es_par(valor):
    """Devuelve True cuando es par
    de lo contrario, False."""
    return valor % 2 == 0

def es_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

# Void
def es_par(valor):
    if valor % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def foo():
    print('mensaje')



print(f"El resultado es: {es_par(2)}")
print(f"El resultado es: {es_par(15)}")
print(f"El resultado es: {es_par(17)}")
print(f"El resultado es: {es_par(22)}")

# mensaje = 'Hola mundo!'
print(f"Escribir nuestro mensaje {mensaje}")

# Capturando errores y resolviendo en tiempo de ejecución
valor = int(input("Ingresar numero entero: "))
print(f"El resultado es: {es_par(valor)}")


def foo():
    # Acá va el algoritmo de la funcion
    # nunca tiene que ir un input ni un print.
    pass


# Algoritmo del modulo / programa
# En el modulo, archivo principal, si vamos a poder usar
# print e input.


# Parametros en las funciones
def foo(valor, valor2, valor3 = 10, valor4 = 12):
    return (valor, valor2, valor3, valor4)

print(foo(1, 2))
print(foo(1, 2, 8, 9))
print(foo(1, 2, valor4=8))
print(foo(1, 2, valor3=7))
print(foo(valor=1, valor2=2, valor4=8))

primero, segundo, tercero, cuarto = foo(1,2,3,4)
print(primero)
print(segundo)
print(tercero)
print(cuarto)


"""
Ejercicios:
Crear una función que va a recibir 4 parametros.
2 dos esos parametros tienen que ser obligatorios.
Y lo vamos a dividir a cada uno por un valor random entre 1 y 10 .
Debemos ejecutar la funcion de todas las maneras posibles
Se devolver, cada uno de los resultados

Esta linea debe ir al comienzo del archivo.
from random import randint
así se usa:
valor_random = randint(1, 10)
print(valor_random)

"""

from random import randint

def dividir_random(valor, valor2, valor3, valor4):
    valor_random = randint(1, 10)
    # Código para valor

    valor_random = randint(1, 10)
    # Código para valor2

    valor_random = randint(1, 10)
    # Código para valor3


    valor_random = randint(1, 10)
    # Código para valor4
