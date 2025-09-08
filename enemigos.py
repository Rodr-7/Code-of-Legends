import pandas as pd
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista
from arma import Arma, arma_inicial
from carga_personaje import leer_personaje
import random

class Enemy:
    def __init__(self, objetivo, enemigo=None,
                 oficios= [Caballero, Mago, Berserker, Exorcista, Alquimista], #Lista de oficios entre los que se designara al enemigo al azar

                 nombres = [    #Lista de nombres entre los que se designara al enemigo al azar
                "Mario",
                "Link",
                "Lara Croft",
                "Master Chief",
                "Kratos",
                "Geralt",
                "Ezio",
                "Samus",
                "Solid Snake",
                "Cloud Strife",
                "Tony Stark",
                "Luke Skywalker",
                "Harry Potter",
                "Frodo Baggins",
                "Katniss Everdeen",
                "Jon Snow",
                "Daenerys Targaryen",
                "Walter White",
                "Rick Grimes",
                "Eleven",
                "Neo",
                "Trinity",
                "John Wick",
                "Maximus",
                "Aragorn",
                "Legolas",
                "Hermione Granger",
                "Batman",
                "Superman",
                "Wonder Woman"
            ]):
        self.objetivo = objetivo
        self.enemigo = enemigo
        self.oficios = oficios
        self.nombres = nombres
        self.generar_enemigo_random() # ---- POR DEFECTO SE GENERA UN ENEMIGO ALEATORIO AL INSTANCIAR

# --------------------- Este metodo generar_enemigo NO esta funcionando, 
# lo mejor sera instanciar el personaje y luego darlo como valor para el atributo enemigo de la clase Enemy
    def generar_enemigo(self, oficio, nombre): # -----------------GENERAR ENEMIGO MANUALMENTE
        try:
            # Buscar la clase correspondiente al oficio
            clase_oficio = next((cls for cls in self.oficios if cls.__name__ == str(oficio)), None)
            # esto es una comprensión de generador.
            # cls.__name__ obtiene el nombre de la clase como una cadena.
            # y filtra las clases cuyo nombre coincide con el nombre del oficio proporcionad

            if clase_oficio is None:
                raise ValueError(f"Oficio '{oficio}' de enemigo no encontrado en la lista de oficios.")
            else:
            # Crear una instancia del enemigo con el nombre dado
                personaje_enemigo = clase_oficio(nombre)
            self.enemigo = personaje_enemigo
        except Exception as error:
            return f"Error al generar enemigo: {error}"

    def generar_enemigo_random(self):   # --------------------GENERACION AUTOMATICA DE ENEMIGO 
        personaje_enemigo = random.choice(self.oficios)(random.choice(self.nombres))
        self.enemigo = personaje_enemigo

    def ataque_enemigo(self):
        #Las acciones DEBEN definirse como funciones LAMBDA para que se ejecuten solo cuando se llamen
        # De lo contrario estas se ejecutan al momento de declararse la lista
        acciones_enemigas = [lambda: self.enemigo.atacar(self.objetivo), lambda: self.enemigo.proteccion()]
        random.choice(acciones_enemigas)()

    def cambio_objetivo(self, nuevo_objetivo):
        self.objetivo = nuevo_objetivo
        return f"{self.enemigo.nombre} será el contrincante de {self.objetivo.nombre}"
    
    def nivelar_enemigo(self):
        nivel_enemigo = self.objetivo.nivel - 2
        self.enemigo.subir_nivel(nivel_enemigo)

    def __str__(self):
        return (
            f"{self.enemigo}\n"
            f"{self.enemigo.nombre} será el contrincante de {self.objetivo.nombre}")
