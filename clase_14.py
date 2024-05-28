import abc


class VehiculoAbstracto(abc.ABC):

    @abc.abstractmethod
    def acelerar(self):
        pass
    
    @abc.abstractmethod
    def frenar(self):
        pass

    @abc.abstractmethod
    def arrancar(self):
        pass

    @abc.abstractmethod
    def apagar(self):
        pass

    @abc.abstractmethod
    def doblar(self, direccion):
        pass


class Vehiculo(VehiculoAbstracto):

    def arrancar(self):
        return "Arrancando"

    def apagar(self):
        return "Apagando"


class Auto(Vehiculo):
    ruedas = 4

    def __init__(self):
        self._velocidad = 19

    # Getter
    @property
    def velocidad(self):
        return self._velocidad

    # Setter
    def frenar(self):
        self._velocidad = self._velocidad - 1 if self._velocidad > 1 else 0
        return self._velocidad
    
    # Setter
    def acelerar(self):
        self._velocidad = self._velocidad + 1
        return self._velocidad

    def doblar(self, direccion):
        return f"Doblando hacia {direccion}"
    
    def arrancar(self):
        return super().arrancar() + " auto"
    
    def apagar(self):
        return super().arrancar() + " auto"


class Moto(Vehiculo):
    ruedas = 2

    def frenar(self):
        return "Frenando"
    
    def acelerar(self):
        return "Acelerando"

    def doblar(self, direccion):
        return f"Doblando hacia {direccion}"
    
    def arrancar(self):
        return super().arrancar() + " moto"
    
    def apagar(self):
        return super().arrancar() + " moto"


auto = Auto()
print(auto.velocidad)

auto.velocidad = 10

print(f'Aceleando a: {auto.acelerar()}')

print(f'Velocidad actual: {auto.velocidad}')

print(f'Frenando a: {auto.frenar()}')

print(f'Velocidad final: {auto.velocidad}')
