# # Type hints


# # Tipos de datos complejos
#     # Diccionario dict
#     # Lista list
#     # Tupla tuple
#     # Conjuntos set

# # Tipos de datos basicos
#     # String str
#     # Numeros entero int
#     # Numeros flotante float
#     # Booleano bool

# variable1: dict = {}

# def nombre_funcion(parametro1: str, parametro2: str) -> str:
#     return parametro1 + parametro2


# def funcion_diccionario(parametro1: dict) -> dict:
#     """DOCString de la funcion"""
#     return parametro1


# def funcion_lista(parametro1: list[int]) -> list[int]:
#     return parametro1


# def foo(parametro: str) -> dict[dict[dict[dict]]]:
#     pass

# diccionario: dict = {
#     'clave': {
#         'clave': {
#             'clave': {

#             }
#         }
#     }
# }

# diccionario2 = {
#     'clave1': {},
#     'clave1': []
# }

# print(diccionario)

# print(diccionario2)

# print(funcion_diccionario(10))

# print(variable1)


# variable_z = 10

# def foo():
#     # hardcodeado
#     # FIJO
#     variable_z = 12
#     variable_y = 12
#     variable_x = 12
    
#     return variable_z, variable_y, variable_x


# print(foo())

# print(variable_z)





# Funcion promedio en nuestro modulo.
def promedio(lista):
    resultado = 0 # Definimos la variable resultado en 0
    for valor in lista: # Recorrermos los valores dentro de una lista
        resultado = resultado + valor # Sumamos al valor anterior el nuevo valor
    return resultado / len(lista) # calculamos el promedio dividiendo el resultado por la cantidad

# Algoritmo
valores = [] # Declaramos una lista de valores, vacia.
cantidad_valores = int(input('Cantidad maxima: '))
while len(valores) < cantidad_valores: # Creamos un ciclo repetitivo infinito con True
    ingreso = input('Ingresar valor: ') # Ingreso por teclado
    if ingreso == 'salir': # Condicion de salida
        break # Sintaxis para romper un bucle repetitivo.
    else:
        valores.append(int(ingreso)) # Almacena un valor entero en la lista


print(promedio(valores)) # Calcula el promedio dinamico

print(promedio([5,6,9,12])) # Calcula un promedio de numero fijos