"""
La aerolínea "VuelaAlto" desea implementar un nuevo sistema para gestionar los vuelos y la venta de boletos.
Para este ejercicio, deben desarrollar un programa en Python utilizando programación orientada a objetos que
simule el proceso de reservación de vuelos y la venta de boletos con precios variados según el destino.

Requerimientos:

Clases Principales:
Aerolínea: Esta clase debe contener el nombre de la aerolínea y una lista de aviones.
Avión: Debe tener un identificador único, modelo y una lista de vuelos disponibles.
Vuelo: Esta clase representa un vuelo específico y debe contener el destino, la fecha, la capacidad máxima y el precio base del boleto.
Pasajero: Debe tener un nombre, apellido y un método para comprar un boleto.

Clases Adicionales:
Todas las que crean necesarias.

Relaciones:
Composición: Utiliza la composición para representar la relación entre la Aerolínea y los Aviones (un avión no existe sin una aerolínea).
Agregación: Implementa una relación de agregación entre Avión y Vuelo,
indicando que un vuelo puede existir sin necesidad de un avión específico, pero un avión puede tener varios vuelos asignados.

Funcionalidades a Implementar:
Agregar aviones a la aerolínea: La aerolínea debe poder añadir aviones a su flota.
Programar vuelos: Los aviones deben poder tener varios vuelos programados a diferentes destinos.
Comprar boletos: Los pasajeros deben poder comprar boletos para un vuelo específico.
El precio del boleto puede variar según el destino y otros factores que decidas incluir (como demanda o temporada).
"""

# Con herencia no estamos estamos relacionando nada
# En la herencia heredamos atributos y comportamiento


# Agregación


class Aerolinea:
    """Relacion: "Agregación de aviones"""

    def __init__(self, nombre, lista_aviones):
        self.nombre = nombre
        # Agregación
        self.aviones = []
        for avion in lista_aviones:
            self.aviones.append(Avion(**avion))


class Avion:
    def __init__(self, id, modelo, capacidad, carga_maxima):
        self.id = id
        self.modelo = modelo
        self.capacidad = capacidad
        self.carga_maxima = carga_maxima


class Vuelo:
    def __init__(self, destino, fecha, precio_base, precio_tope):
        self.destino = destino
        self.fecha = fecha
        self.precio_base = precio_base
        self.precio_tope = precio_tope


class Itinerario:
    """Relacionamos un avion con un vuelo"""

    def __init__(self, vuelo, avion):
        self.vuelo = Vuelo(**vuelo)
        self.avion = Avion(**avion)


class Pasajero:
    """Composición de Pasajero y Itinerario"""

    def __init__(self, nombre, apellido, documento, nacionalidad, itinerario):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.nacionalidad = nacionalidad
        self.itinerario = Itinerario(**itinerario)


avion = {"id": 1, "modelo": "Boeing 777", "capacidad": 120, "carga_maxima": 90000}
aerolinea = {"nombre": "LATAM", "lista_aviones": [avion]}
vuelo = {
    "destino": "Hawaii",
    "fecha": "6 de mayo de 2024",
    "precio_base": 100,
    "precio_tope": 150,
}
itinerario = {"vuelo": vuelo, "avion": avion}
pasajero = {
    "nombre": "Juan",
    "apellido": "Perez",
    "documento": 123,
    "nacionalidad": "Argentina",
    "itinerario": itinerario,
}


_pasajero = Pasajero(**pasajero)
_itinerario = Itinerario(**itinerario)
_vuelo = Vuelo(**vuelo)
_aerolinea = Aerolinea(**aerolinea)
_avion = Avion(**avion)


class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año


diccionario = {"marca": "Ford", "modelo": "Focus", "año": 2020}

auto = Auto(
    marca=diccionario["marca"], modelo=diccionario["modelo"], año=diccionario["año"]
)
auto2 = Auto(marca="Chevrolet", modelo="Cruze", año=2020)
auto3 = Auto(**diccionario)
print(auto3)


"""El equivalente de hacer esto:


Auto(marca=diccionario["marca"], modelo=diccionario["modelo"])

es esto:
auto3 = Auto(**diccionario)

"""
