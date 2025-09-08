import pandas as pd
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista
from arma import Arma, arma_inicial
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
        self.generar_enemigo()

    def generar_enemigo(self):
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



prota = Caballero("Link")
prota.subir_nivel(6)
print(prota)
villano = Enemy(prota)
villano.nivelar_enemigo()
print(villano)
villano.ataque_enemigo()
