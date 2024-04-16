# # Variables
# nombre_de_variable = 20

# nombre = "Jose"

# decimales = 30.0

# listas = [1, "asds", [2,2], {'k': 'v'}]

# diccionarios = {
#     'clave': 'valor',
#     'clave2': 1,
#     'diccionario': {
#         'diccionario': {}
#     }
# }


# """
# Format string

# fString

# """
# def foo():
#     return "Hola che"
# print(f"Mi nombre es Juan Ingacio \nVos como te llamas? tabulado {foo()}")

# if nombre == 'Juan':
#     print(f'Hola {nombre}')
# elif nombre == 'Pedro':
#     print(f'Hola {nombre}')
# else:
#     print('Hola extraño')

# def foo():
#     return 'hola'

# print('hola ' + 'chau')
# print(2+2)
# print('*' * 12)

# type = 10
# print('chau')

# def foo(param, param2, param3=None):
#     pass

# def vector(param1, param2, param3=None):
#     if param3 is None:
#         return 'Vector de 2'
#     # Aca se empieza a trabajar como si fuera uno de 3
#     return 'Vector de 3'

# print(vector(1, 5))
# print(vector(1, 5, 6))

"""Resolviendo ejecicio"""
"""
Ejercicios:
Crear una función que va a recibir 4 parametros.
2 dos esos parametros tienen que ser obligatorios.
Y lo vamos a dividir a cada uno por un valor random entre 1 y 10 .
Debemos ejecutar la funcion de todas las maneras posibles
Se devolver, cada uno de los resultados
"""
from random import randint

def _dividir(parametro):
    if parametro is not None:
     return parametro / randint(1, 123)

def dividir_random(
        parametro1,
        parametro2,
        parametro3,
        parametro4=None
    ):
    return _dividir(parametro1), _dividir(parametro2), _dividir(parametro3), _dividir(parametro4)

print(dividir_random(3,4,5))
