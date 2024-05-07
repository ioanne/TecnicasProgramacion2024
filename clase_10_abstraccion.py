"""Abstracción"""


class Abstracta:
    def __init__(self):
        pass

    def obtener_valor(self) -> str:
        """Este metodo se encarga de obtener el valor de la clase"""
        pass

    def calcular_valor(self, valor: int, valor_2: int) -> int:
        """Este metodo se encarga de calcular el valor de la clase"""
        pass

    def cualquier_otra_cosa(self) -> str:
        """Este metodo se encarga de hacer cualquier otra cosa"""
        pass


class B(Abstracta):
    def obtener_valor(self) -> str:
        return "B"

    def calcular_valor(self, valor: int, valor_2: int) -> int:
        return valor + valor_2

    def cualquier_otra_cosa(self) -> str:
        return "Cualquier otra cosa"
