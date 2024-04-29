""" Crear empleados, gerentes, directores"""


class EmpleadoAbstracto:
    pass


class Empleado(EmpleadoAbstracto):
    def __init__(self, nombre, apellido, edad, salario) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.salario}"


class Gerente(Empleado):
    pass


class Director(Empleado):
    pass


class DepartamentoInformatica:
    # Composición
    # La composición es una relación entre dos clases donde una clase contiene un objeto de otra clase.
    def __init__(self, director):
        self.director = Director(**director)


class Empresa:
    def __init__(self):
        self.base_datos_empleados = [
            {"nombre": "Juan", "apellido": "Perez", "edad": 30, "salario": 1000},
            {"nombre": "Maria", "apellido": "Gomez", "edad": 40, "salario": 2000},
            {"nombre": "Pedro", "apellido": "Gonzalez", "edad": 50, "salario": 3000},
        ]  # Imaginamos que tenemos empleados en una base de datos

    @property
    def empleados(self):
        self._empleados = []
        for empleado in self.base_datos_empleados:
            self._empleados.append(
                Empleado(
                    nombre=empleado["nombre"],
                    apellido=empleado["apellido"],
                    edad=empleado["edad"],
                    salario=empleado["salario"],
                )
            )
        return self._empleados


empresa = Empresa()
print(empresa.empleados)
print(empresa.empleados)
print(empresa.empleados)
print(empresa.empleados)
print(empresa)
