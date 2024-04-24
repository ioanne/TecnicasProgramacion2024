"""
En este desafío, te retamos a crear una estructura de clases
que represente la diversidad de animales existentes.
Además de los atributos básicos como nombre, edad y alimentación,
deberás pensar en otros atributos y métodos específicos para cada clase de animal.
Asimismo, tendrás que implementar funciones que les permitan a los animales desplazarse,
alimentarse y comunicarse de acuerdo a sus características únicas.
Aprovecha el principio de herencia para compartir características
comunes entre las clases y anímate a añadir atributos y métodos adicionales
que enriquezcan la representación de cada especie animal.
¡Demuestra tu creatividad al adaptar el comportamiento de cada animal
en las clases específicas!
"""

"""
Pilares de la programacion orientada a objetos
Herencia: Es la capacidad de una clase de heredar atributos y métodos de otra clase
Abstraccion: Es el proceso de aislar los detalles de implementación de un objeto
Polimorfismo: Es la capacidad de un objeto de comportarse de múltiples formas
Encapsulamiento: Es la capacidad de ocultar los detalles de implementación de un objeto
"""


# Abstraccion
class AnimalAbstracto:
    def __init__(self, nombre, edad, alimentacion):
        self.nombre = nombre
        self.edad = edad
        self.alimentacion = alimentacion

    def comer(self):
        pass

    def desplazarse(self):
        pass

    def comunicarse(self):
        pass


# Esto no hay que hacerlo.
animal_abstracto = (
    AnimalAbstracto()
)  # Es solo para mostrar que no se puede instanciar una clase abstracta


class Animal(AnimalAbstracto):
    def __init__(self, nombre, edad, alimentacion):
        super().__init__(nombre, edad, alimentacion)

    def comer(self):
        return "El animal esta comiendo"

    def desplazarse(self):
        return "El animal se desplaza"

    def comunicarse(self):
        return "El animal se comunica"


class Mamifero(Animal):
    def comer(self):
        return "El mamifero esta comiendo"

    def desplazarse(self):
        return "El mamifero se desplaza"

    def comunicarse(self):
        return "El mamifero se comunica"


class Ave(Animal):
    def comer(self):
        return "El ave esta comiendo"

    def desplazarse(self):
        return "El ave se desplaza"

    def comunicarse(self):
        return "El ave se comunica"


class Reptil(Animal):
    def comer(self):
        return "El reptil esta comiendo"

    def desplazarse(self):
        return "El reptil se desplaza"

    def comunicarse(self):
        return "El reptil se comunica"


class Pez(Animal):
    def comer(self):
        return "El pez esta comiendo"

    def desplazarse(self):
        return "El pez se desplaza"

    def comunicarse(self):
        return "El pez se comunica"


# Herencia multiple
class Mixto(Mamifero, Ave):
    pass
