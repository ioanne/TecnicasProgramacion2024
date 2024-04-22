# Variables

nombre = "Juan"
edad = 25
estatura = 1.75
diccionario = {"nombre": nombre, "edad": edad, "estatura": estatura}  # Mutable

tupla = (nombre, edad, estatura)  # Inmutable

lista = [nombre, edad, estatura]  # Mutable

# Desempaquetando
nombre, edad, estatura = tupla
nombre, edad, estatura = lista

# No se pueden tener valores repetidos.
conjunto = {nombre, edad, estatura}

valor1 = 1
valor2 = 2

valor1 - valor2

# + - * / // % **

# Comentario de una linea

"""Comentario
de 
muchas 
lineas
se llama
DOCString"""

# Siempre antes de almacenar
# se va a evualuar lo que se tenga que evaluar
# se almacena un resultado.
operacion = 1 / 5


# Desempaquetado
v1, v2, v3 = 1, 2, 3


valores = [1, 3, 4, 5, 6, 7, 8, 9]  # Mutable
valores_anteriores = valores
valores.pop(3)

id(valores)
id(valores_anteriores)

# https://docs.python.org/es/3/library/copy.html

from copy import copy

valores = [1, 3, 4, 5, 6, 7, 8, 9]  # Mutable
valores_anteriores = copy(valores)
valores.pop(3)

id(valores)
id(valores_anteriores)


def nombre_funcion(param1, param2):
    # Variable que declaro dentro de una funcion
    # Vive y muere dentro de la función.
    variable_funcion = 1


nombre_funcion(1, 2)
nombre_funcion(1, param2=1)
nombre_funcion(param2=2, param1=1)

fooo = 5
print(fooo)  # Salida 5


def foo():
    global fooo
    fooo = 1


print(fooo)  # Salida 1


# No usar valores por defecto mutables
def nueva_funcion(valor=[]):
    valor.append(valor)
    return valor
