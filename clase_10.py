"""
Pilares de la Programación Orientada a Objetos
Abstracción
Herencia
Polimorfismo
Encapsulamiento
"""


class Vehiculo:
    pass


class Auto(Vehiculo):
    pass


class A:
    def __init__(self):
        self.a = "A"
        print("Inicializador de A")

    def get_value(self):
        return "A"

    def pepe_1(self):
        return "A"


class B:
    def __init__(self):
        self.b = "B"
        print("Inicializador de B")

    def get_value(self):
        return "B"

    def pepe_1(self):
        return "B"


class C:
    pass


class MixClassAB(A, B):
    pass


class MixClassBA(B, A):
    pass


class MixClassAC(A, C):
    pass


# Polimorfismo
mix_classab = MixClassAB()
print(mix_classab.get_value())
print(mix_classab.pepe_1())


mix_classba = MixClassBA()
print(mix_classba.get_value())
print(mix_classba.pepe_1())


class Animal:
    def __init__(self):
        pass

    def hablar(self):
        return "Sonido de animal"


class Perro(Animal):
    def hablar(self):
        """Sobreescritura de método hablar de la clase padre Animal"""
        return f"Guau"


class Gato(Animal):
    def hablar(self):
        """Sobreescritura de método hablar de la clase padre Animal"""
        return f"Miau"

    def correr(self):
        return "Corriendo"


class AnimalDesconocido(Animal):
    def hablar(self):
        """Extensión del método hablar de la clase Animal"""
        sonido = super().hablar()
        return f"{sonido} pero no sé qué animal es"


animales = [Perro(), Gato(), Perro(), Perro(), Gato(), AnimalDesconocido()]

for animal in animales:
    print(animal.hablar())
