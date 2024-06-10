"""
Diseña e implementa un sistema completo de gestión de turnos en línea que
permita a los usuarios buscar, registrar y administrar turnos.
Los turnos pueden ser corte, barba, tintura, etc. El sistema debe
incluir funcionalidades avanzadas como recomendación de precio, gestión
de pago, etc.
"""

"""
Leemos el enunciado.
1) Crear todas las clases necesarias.
2) Agregarle todos los atributos necesarios.
3) Hacer herencia / composición dependiendo si es necesario.
4) Crear todos los metodos que se van a usar en las clases.
"""

class GestionTurno:
    """
    Todos los turnos tienen una duración X y se debe calcular
    en base a la hora y la duración del mismo."""
    def __init__(self, usuario):
        self.usuario = usuario
        self.turnos: list[Turno] = []

    def obtener_turno(self, fecha, hora):
        for turno in self.turnos:
            if fecha == turno.fecha and turno.hora == hora:
                return turno

    def pedir_turno(self, fecha, hora, servicio):
        turno = self.obtener_turno(fecha, hora)
        if not turno:
            # Verificar el servicio
            # Creamos el turno
            return self.turnos.append(
                Turno(fecha, hora, servicio) # Creas el objeto de turno
            ) # Agregación

    def cambiar_turno(self, turno, fecha=None, hora=None):
        # Creamos un nuevo turno
        # Borramos el turno existente
        pass

    def buscar_turno(self, usuario, fecha, hora):
        # Busqueda de turno por fecha y hora exacta.
        pass


class Turno:
    def __init__(self, fecha, hora, servicio):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio


class Servicio:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion


class Tarjeta:
    cuotas_sin_interes = [3]


class Visa(Tarjeta):
    """Las variables de clase se definen a nivel de clase
    y representan un estado en comun"""
    nombre = "Visa"


class Amex(Tarjeta):
    cuotas_sin_interes = [3, 6]
    nombre = "American Express"


class MasterCard(Tarjeta):
    cuotas_sin_interes = [3, 6, 12]
    nombre = "Master Card"


class MedioPago:
    def __init__(self, tarjeta):
        self.tarjeta = tarjeta

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class GestionPago:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario


    def pagar(self, medio_pago: MedioPago, cuotas: int = None):
        pass


    def calcular_interes(self, medio_pago: MedioPago, cuotas: int = 1):
        pass




# Creamos / obtenemos un usuario
usuario = Usuario("Juan")
gestion_turno = GestionTurno(usuario)
gestion_turno.pedir_turno("2020-01-01", "12:00")

fecha = "2020-01-01"
hora = "12:00"
turno = gestion_turno.obtener_turno(fecha, hora)
gestion_turno.cambiar_turno(turno, "2020-05-01", "1:00")