class Empleado:
    categoria = "Empleado"

    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    @property  # Decorador
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def obtener_edad(self):
        # Se obtiene la edad a partir de la fecha de nacimiento
        pass


# Instanciamos un objeto de la clase Empleado
# Lo almacenamos en la variable juan
juan = Empleado("Juan", "Bonini")
pedro = Empleado("Pedro", "Perez")

print(juan.nombre_completo)
print(pedro.nombre_completo)

print(id(juan.categoria))
print(id(pedro.categoria))
