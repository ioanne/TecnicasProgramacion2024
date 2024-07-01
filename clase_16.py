"""
Desarrolla un sistema de recomendación de películas que sugiera
películas a los usuarios en función de sus gustos previos y las calificaciones de otras películas.
Utiliza algoritmos de filtrado colaborativo o sistemas de recomendación
basados en contenido para generar recomendaciones personalizadas para cada usuario.
Considera también la implementación de funciones avanzadas como la detección de tendencias,
la recomendación de grupos y la retroalimentación del usuario.
"""

class Genero:
    pass


class Animado(Genero):
    nombre = "Animado"
    tipo = "animado"


class CienciaFiccion(Genero):
    nombre = "Ciencia Ficcion"
    tipo = "ciencia_ficcion"


class Pelicula:
    lista_generos = [
        Animado, CienciaFiccion
    ]

    # @classmethod
    # def _obtener_genero(cls, genero):
    #     for gen in cls.lista_generos:
    #         if gen.tipo == genero:
    #             return genero

    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = self._obtener_genero(genero)


class Usuario:
    def __init__(self, username):
        self.username = username
        self.peliculas_vistas = ListaPeliculas(self)

    def ve_pelicula(self, pelicula):
        self.peliculas_vistas.visualizar_pelicula(pelicula)


class ListaPeliculas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.peliculas = []
    
    def visualizar_pelicula(self, pelicula):
        """agregamos la pelicula"""
        self.peliculas.append(pelicula)


class FiltradoColaborativo:
    def __init__(self, username):
        # Composición
        self.usuario = Usuario(username)
        

    def filtrar(self):
        return "Filtrado colaborativo"
    

class DeteccionTendencia:
    def __init__(self, usuarios):
        self.usuarios

    def tendencia(self, peliculas_existentes):
        # Recorremos las peliculas existentes
        # Y obtenemos cual es la más vista.

        # Recorrer usuarios
        # Contamos las peliculas vistas por los usuarios
        # Como clave tenemos el nombre de la pelicula y como valor la cantidad de usuarios que la vio
        # Por cada usuario hacemos algo parecido a _contador_genero pero para peliculas
        # y luego hacemos algo parecido a _genero_mas_visto pero de peliculas mas vistas
        pass


class SistemaRecomendacion:
    def __init__(self, usuario, peliculas_existentes):
        self.usuario = usuario
        self.peliculas_existentes = peliculas_existentes

    # def _contador_genero(self):
    #     generos_vistos = {}
    #     for pelicula in self.usuario.peliculas_vistas.peliculas:
    #         if pelicula.genero in generos_vistos.keys():
    #             generos_vistos[pelicula.genero] += 1
    #         else:
    #             generos_vistos[pelicula.genero] = 1
    #     return generos_vistos      

    # def _genero_mas_visto(self, generos_vistos):
    #     genero_mas_visto = None
    #     mas_visto = 0

    #     for genero, cantidad in generos_vistos.items():
    #         if cantidad > mas_visto:
    #             # Esto es lo mas importante
    #             mas_visto = cantidad
    #             genero_mas_visto = genero
    #     return genero_mas_visto

    # def recomendar_peliculas(self):
    #     """
    #     Contanto el genero mas visto
    #     """
        
    #     cantidad_generos_vistos = self._contador_genero()
    #     # Objtener el genero más visto
        
    #     genero_mas_visto = self._genero_mas_visto(cantidad_generos_vistos)
            
    #     print(genero_mas_visto)

    #     # Recorrer las peliculas existentes
    #     # Omitir las que ya se vieron
    #     # Usar random para que nos de un numero aleatorio entre
    #     # 0 y -1 peliculas_existentes (animadas)
    
usuario = Usuario(username="Pedro")


pelicula = Pelicula(nombre="Shrek", genero="animado")
pelicula1 = Pelicula(nombre="Cars", genero="animado")
pelicula2 = Pelicula(nombre="Buscando a Nemo", genero="animado")
pelicula3 = Pelicula(nombre="Transformers", genero="ciencia_ficcion")

# hay mil peliculas mas

# Obtiene de una base datos
peliculas_existentes = [
    pelicula, pelicula1, pelicula2, pelicula3
]

usuario.ve_pelicula(pelicula1)
usuario.ve_pelicula(pelicula2)
usuario.ve_pelicula(pelicula3)

sistema_recomendacion = SistemaRecomendacion(usuario, peliculas_existentes)
pelicula_recomendada = sistema_recomendacion.recomendar_peliculas()
print(pelicula_recomendada)




class Puerta:
    pass


class PuertaBaul:
    pass


class Motor:
    pass


class Mecanico:
    def __init__(self, auto):
        self.auto = auto

    def poner_puerta(self):
        self.auto.append(Puerta())

    def poner_motor(self):
        self.auto.motor = Motor()



class AutoSedan:
    def __init__(self):
        self.motor = None
        self.puertas = []
        self.puerta_baul = None

    def arrancar(self):
        pass

    def acelerar(self):
        pass


auto = AutoSedan()
mecanico_trabajando = Mecanico(auto)

mecanico_trabajando.poner_puerta()
mecanico_trabajando.poner_puerta()
mecanico_trabajando.poner_puerta()
mecanico_trabajando.poner_puerta()

mecanico_trabajando.poner_motor()


