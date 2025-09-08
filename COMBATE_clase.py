import pandas as pd
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista, Enemy, leer_personaje
from arma import Arma, arma_inicial
from habilidad import Habilidad_Caballero, Habilidad_Mago, Habilidad_Berserker, Habilidad_Exorcista, Habilidad_Alquimista, carga_habilidades, carga_lista_habilidades
from gestion_personaje import PerfilPersonaje, PerfilArma
import sys
from musica import musica_fondo, detener_musica
class RedirectOutput:
    def __init__(self, label):
        self.label = label

    def write(self, text):
        if self.label.winfo_exists():
            self.label.config(text=self.label.cget("text") + text)

    def flush(self):
        pass
"""RedirectOutput
La clase RedirectOutput es una clase personalizada que se utiliza para redirigir la salida estándar (stdout)
a un widget Label de Tkinter. Esto permite que los mensajes que normalmente se imprimirían en la consola se
muestren en la interfaz gráfica de usuario.
label: El widget Label de Tkinter donde se mostrarán los mensajes redirigidos.
Inicializa la instancia con el Label proporcionado.
write(self, text):
Este método se llama cada vez que se escribe algo en la salida estándar (stdout).
Parámetros:
text: El texto que se va a escribir en la salida estándar.
Actualiza el texto del Label concatenando el nuevo texto al texto existente en el Label.
flush(self):
Este método es necesario para la compatibilidad con Python 3, pero no hace nada en este caso.
Parámetros:
Ninguno.
No realiza ninguna acción, pero es necesario para que la clase sea compatible con el sistema de flujo de salida de Python.
"""

class Combate:
    def __init__(self, root, personaje_jugador):
        self.root = root
        self.personaje_jugador = personaje_jugador
        self.enemigo_cpu = Enemy(personaje_jugador)
        self.habilidad_jugador = carga_habilidades(personaje_jugador, self.enemigo_cpu.enemigo)
        self.habilidad_enemigo = carga_habilidades(self.enemigo_cpu.enemigo, personaje_jugador)
        self.lista_hab = carga_lista_habilidades(personaje_jugador)
        self.perfil_jugador = PerfilPersonaje(personaje_jugador.nombre)
        self.perfil_jugador.leer_personaje()
        self.numero_turno = 0
        self.turno_jugador = False
        self.accion_a_realizar = None
        self.habilidad_a_realizar = False
        self.vida_jugador = True
        self.enemigo_cpu.enemigo.subir_nivel(personaje_jugador.nivel)
        self.stats_jugador = [
                                self.personaje_jugador.nivel, #0
                                self.personaje_jugador.fuerza, #1
                                self.personaje_jugador.inteligencia, #2
                                self.personaje_jugador.karma, #3
                                self.personaje_jugador.defensa, #4
                                self.personaje_jugador.vida #5
                            ]
        self.setup_ui()#self.setup_ui() es un método que configura la interfaz de usuario de la ventana de combate,
        #creando y organizando todos los widgets necesarios. Al llamar a este método en el constructor (__init__), 
        # se asegura que la interfaz de usuario esté lista cuando se crea una instancia de la clase
#----musica de fondo--------------
        #self.musica = musica_fondo(2)
    # Inicializar pygame
    #pygame.mixer.init()
    # Cargar y reproducir música
    #pygame.mixer.music.load("DarkSouls_Character_Creation.mp3")
    #pygame.mixer.music.play(-1)  # El argumento -1 hace que la música se repita indefinidamente

    def setup_ui(self):
        self.root.title("Combate")
        self.root.geometry("800x560")

        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.grid(row=0, column=1, padx=10, pady=10)

        frame_combate = tk.Frame(frame, bg="brown", padx=10, pady=10)
        frame_combate.grid(row=0, column=1, sticky="ew")

        self.label_nombre_jugador = tk.Label(frame_combate, text=f"{self.personaje_jugador.nombre}")
        self.label_nombre_jugador.grid(row=1, column=0, sticky="w")

        self.label_nombre_enemigo = tk.Label(frame_combate, text=f"{self.enemigo_cpu.enemigo.nombre}")
        self.label_nombre_enemigo.grid(row=0, column=2, sticky="w")

        self.label_narrador = tk.Label(self.root, text=f"{self.personaje_jugador.nombre} se enfrenta a {self.enemigo_cpu.enemigo.nombre}\n", anchor="n", justify="left")
        self.label_narrador.grid(row=0, column=2, sticky="w")

        sys.stdout = RedirectOutput(self.label_narrador)

        self.sprite_usar(self.personaje_jugador.oficio, self.label_nombre_jugador)
        self.sprite_usar(self.enemigo_cpu.enemigo.oficio, self.label_nombre_enemigo)

        self.lista = tk.Listbox(self.root, font=("Verdana", 16, "bold"), bg="blue", fg="white", width=20, height=5)
        opciones = ["Atacar", "Protegerse", "Habilidad"]
        for opcion in opciones:
            self.lista.insert(tk.END, opcion)
        self.lista.bind("<<ListboxSelect>>", self.mostrar_seleccion)
        self.lista.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")

        self.menu_hab = tk.Listbox(self.root, font=("Verdana", 16, "bold"), fg="black", width=32, height=5)
        for habilidad in self.lista_hab:
            self.menu_hab.insert(tk.END, habilidad)
        self.menu_hab.bind("<<ListboxSelect>>", self.mostrar_habilidad)

        self.label_opcion = tk.Label(self.root, text=f"Seleccionaste: Ninguna\n")
        self.label_opcion.grid(row=6, column=0, columnspan=2, pady=1)

        self.boton_accion = tk.Button(self.root, text="Adelante!", command=self.accion_elegida, width=20, height=3)
        self.boton_accion.grid(row=6, column=0, columnspan=2, pady=15, sticky="ew")
    
    def volver(self):
        self.root.destroy()

    def sprite_usar(self, oficio_personaje, label_personaje):
        if oficio_personaje == "Caballero":
            from sprites import imagen_caballero_tk
            label_personaje.config(image=imagen_caballero_tk, compound='top')
        elif oficio_personaje == "Mago":
            from sprites import imagen_mago_tk
            label_personaje.config(image=imagen_mago_tk, compound='top')
        elif oficio_personaje == "Berserker":
            from sprites import imagen_berserker_tk
            label_personaje.config(image=imagen_berserker_tk, compound='top')
        elif oficio_personaje == "Exorcista":
            from sprites import imagen_exorcista_tk
            label_personaje.config(image=imagen_exorcista_tk, compound='top')
        elif oficio_personaje == "Alquimista":
            from sprites import imagen_alquimista_tk
            label_personaje.config(image=imagen_alquimista_tk, compound='top')

    def sprite_muerte(self, label_personaje):
        from sprites import imagen_muerte_tk
        label_personaje.config(image=imagen_muerte_tk, compound='top')

    def despejar_mensajes(self):
        texto = self.label_narrador.cget("text")
        self.label_narrador.config(text="") # Las siguientes 3 lineas limpian la etiqueta solo si acumula cierto numero de caracteres, si se usa comentar esta linea
        #num_caracteres = len(texto)
        #if num_caracteres > 100:
        #    self.label_narrador.config(text="")

    def accion_ataque(self):
        self.despejar_mensajes()
        self.personaje_jugador.atacar(self.enemigo_cpu.enemigo)
        self.turno_jugador = True
        self.muerte_personaje()


    def accion_proteger(self):
        self.despejar_mensajes()
        self.personaje_jugador.proteccion()
        self.turno_jugador = True
        self.muerte_personaje()

    def accion_habilidad(self):
        self.despejar_mensajes()
        if not self.habilidad_a_realizar:
            print("No se selecciono ninguna habilidad")
        else:
            self.habilidad_a_realizar()
        self.muerte_personaje()

    def muerte_personaje(self):
        if self.personaje_jugador.vida <= 0 or self.enemigo_cpu.enemigo.vida <= 0:
            if self.personaje_jugador.vida > self.enemigo_cpu.enemigo.vida:
                personaje_ganador = self.personaje_jugador.nombre
                personaje_perdedor = self.enemigo_cpu.enemigo.nombre
                self.sprite_muerte(self.label_nombre_enemigo)
                detener_musica()
                musica_fondo(5)
            else:
                personaje_ganador = self.enemigo_cpu.enemigo.nombre
                personaje_perdedor = self.personaje_jugador.nombre
                self.sprite_muerte(self.label_nombre_jugador)
                if self.personaje_jugador.nivel > 1:
                    self.perfil_jugador.subir_niveles(-1) # Si el jugador pierde se le resta 1 nivel
                detener_musica()
                musica_fondo(4)
                self.vida_jugador = False       
            self.label_narrador.config(text="")
            self.label_narrador.config(text=f"El combate ha terminado, {personaje_ganador} es el ganador. \n {personaje_perdedor} MUELTO.")
            self.boton_accion.config(text="Volver", command=self.volver)
    def accion_elegida(self):
        self.muerte_personaje()
        if  self.vida_jugador:
            if self.accion_a_realizar == "Atacar":
                self.muerte_personaje()
                self.accion_ataque()
                self.turno_enemigo()
                
            elif self.accion_a_realizar == "Protegerse":
                self.muerte_personaje()
                self.accion_proteger()
                self.turno_enemigo()
                
            elif self.accion_a_realizar == "Habilidad":
                self.muerte_personaje()
                self.accion_habilidad()
                self.turno_enemigo()
            self.numero_turno += 1
            if self.numero_turno >= 10:
                self.perfil_jugador.subir_niveles(1) # Si pasa 10 trnos en combate el jugador sube 1 nivel
                self.numero_turno = 0
    
    def reestablecer_stats(self): # Reestablece los stats originales para anular las alteraciones por medio de habilidades durante el combate
        self.personaje_jugador.fuerza = self.stats_jugador[1]
        self.personaje_jugador.inteligencia = self.stats_jugador[2]
        self.personaje_jugador.karma = self.stats_jugador[3]
        self.personaje_jugador.defensa = self.stats_jugador[4]
        self.personaje_jugador.vida = self.stats_jugador[5]
        if self.personaje_jugador.nivel > self.stats_jugador[0]: # Si el jugador subió de nivel durante el combate esto ajusta su nivel y eleva sus stats acorde a los niveles subidos
            diferencia_nivel = self.personaje_jugador.nivel - self.stats_jugador[0]
            self.personaje_jugador.nivel = self.stats_jugador[0]
            self.perfil_jugador.subir_niveles(diferencia_nivel)
           

    def turno_enemigo(self):
        self.enemigo_cpu.accion_enemigo()
        self.muerte_personaje()

    def mostrar_seleccion(self, event):
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            valor = self.lista.get(indice)
            if valor == "Atacar":
                self.label_opcion.config(text=f"Ataca directamente al enemigo.\n")
                self.menu_hab.grid_remove()
            elif valor == "Protegerse":
                self.label_opcion.config(text=f"Toma una posición defensiva,\n mitigando el daño enemigo.")
                self.menu_hab.grid_remove()
            elif valor == "Habilidad":
                self.label_opcion.config(text=f"Seleccionar una de las\nhabilidades para usar.")
                self.menu_hab.grid(row=3, column=2, columnspan=2, pady=15, sticky="ew")
            self.accion_a_realizar = valor

    def mostrar_habilidad(self, event):
        seleccion = self.menu_hab.curselection()
        if seleccion:
            indice = seleccion[0]
            if indice == 0 and hasattr(self.habilidad_jugador, "hab1"):
                self.habilidad_a_realizar = getattr(self.habilidad_jugador, "hab1")
            elif indice == 1 and hasattr(self.habilidad_jugador, "hab2"):
                self.habilidad_a_realizar = getattr(self.habilidad_jugador, "hab2")
            elif indice == 2 and hasattr(self.habilidad_jugador, "hab3"):
                self.habilidad_a_realizar = getattr(self.habilidad_jugador, "hab3")



if __name__ == "__main__":
    root = tk.Tk()
    personaje_jugador = leer_personaje("Guts")
    app = Combate(root, personaje_jugador)
    root.mainloop()

"""
if __name__ == "__main__":
Este condicional verifica si el nombre del módulo (__name__) es "__main__". 
En Python, cuando un script se ejecuta directamente, el valor de __name__ es "__main__". 
Si el script se importa como un módulo en otro script, el valor de __name__ será el nombre 
del archivo del script sin la extensión .py.
"""