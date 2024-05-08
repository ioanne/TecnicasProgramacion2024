

"""Imagina que estás trabajando en un programa de gestión de un sistema educativo.
Tu tarea es diseñar un conjunto de clases orientadas a objetos
para administrar estudiantes, profesores, asignaturas y calificaciones.
Debes crear clases como 'Estudiante', 'Profesor', 'Asignatura' y 'Calificacion'.
Implementa herencia para representar diferentes niveles de estudiantes,
como 'EstudianteRegular' y 'EstudianteAvanzado'.
Utiliza la composición, agregación para gestionar la relación entre estudiantes,
asignaturas y calificaciones, y asegúrate de que el diseño sea versátil
para futuras funcionalidades del sistema educativo.
"""


class Carrera:
    pass


class CarreraTecnicatura(Carrera):
    pass


class CarreraIngenieria(Carrera):
    pass


class Asignatura:
    def __init__(self, profesor):
        # Composición
        self.profesor = Profesor(**profesor)


class IngenieriaDeSoftware(CarreraIngenieria):
    def __init__(self, asignaturas):
        # Agregación
        self.asignaturas = []
        for asignatura in asignaturas:
            self.asignaturas.append(Asignatura(**asignatura))


class DomicilioLegal:
    pass


class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento


class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, domicilio):
        # Extendemos el metodo init
        super().__init__(self, nombre, apellido, fecha_nacimiento)
        # Composición
        self.domicilio = DomicilioLegal(**domicilio)


class EstudianteIngenieriaDeSoftware(Estudiante):
    # Composición a nivel de la clase
    carrera = IngenieriaDeSoftware()

    def __init__(self, asignaturas):
        super().__init__(self, asignaturas)


class Profesor(Persona):
    pass


class Calificacion:
    def __init__(self, asignatura, nota):
        self.asignatura = Asignatura(**asignatura)
        self._nota = nota
    
    def asignar_nota(self, nota: int | None):
        """ Setter """
        # If inline
        self._nota = nota if nota >= 1 and nota <= 10 else None

        # Esto es el equivalente a la linea anterior
        if nota >= 1 and nota <= 10:
            self._nota = nota
        else:
            self._nota = None

    @property
    def nota(self):
        return self._nota


class EstudianteRegular(Estudiante):
    def __init__(self, nombre, apellido, fecha_nacimiento, domicilio, materias_aprobadas):
        super().__init__(self, nombre, apellido, fecha_nacimiento, domicilio)
        self.materias_aprobadas = materias_aprobadas

class EstudianteAvanzado(EstudianteIngenieriaDeSoftware):
    pass
