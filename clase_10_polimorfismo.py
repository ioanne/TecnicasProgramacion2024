class A:
    def __init__(self):
        pass

    def obtener_valor(self):
        return "A"


class B(A):
    def __init__(self):
        pass

    def obtener_valor(self):
        """Sobreescritura de la funcionalidad de la clase padre"""
        return "B"


class C(A):
    def __init__(self):
        pass

    def obtener_valor(self):
        """Extensión de la funcionalidad de la clase padre"""
        valor_a = super().obtener_valor()
        return f"{valor_a} C"
