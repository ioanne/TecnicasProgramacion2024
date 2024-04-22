# # Creamos la clase Auto
# class Auto:
#     def __init__(self, color, marca, modelo):
#         print("Inicializando el objeto Auto")
#         self.color = color
#         self.marca = marca
#         self.modelo = modelo


# # Instanciar la clase Auto
# auto = Auto("rojo", "Ford", "Fiesta")

# print(auto)

# print(auto.color)
# print(auto.marca)
# print(auto.modelo)


# auto.color = "Azul"

# Pilares de la programacion orientada a objetos
# Herencia
# Encapsulamiento
# Polimorfismo
# Abstraccion


class Vehiculo:
    CANTIDAD_RUEDAS = None

    def __init__(self, color, marca, modelo, rodado):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.rodado = rodado

    def acelerar(self):
        return "Acelerando"

    def frenar(self):
        return "Frenando"


class Auto(Vehiculo):
    CANTIDAD_RUEDAS = 4

    def __init__(self, color, marca, modelo, rodado, puertas):
        super().__init__(color, marca, modelo, rodado)
        self.puertas = puertas

    def acelerar(self):
        # Sobreescribiendo el metodo acelerar del padre
        return "Acelerando el auto"

    def frenar(self):
        freno = super().frenar()
        return f"{freno} el auto"
        # Extendiendo el metodo frenar del padre


class Moto(Vehiculo):
    CANTIDAD_RUEDAS = 2


class Triciclo(Vehiculo):
    CANTIDAD_RUEDAS = 3


class Cuatriciclo(Vehiculo):
    CANTIDAD_RUEDAS = 4


auto = Auto(color="rojo", marca="Ford", modelo="Fiesta", rodado=15, puertas=4)

print(auto.color)

print(auto.acelerar())
print(auto.frenar())
