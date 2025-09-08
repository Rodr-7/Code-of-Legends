import tkinter as tk
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista
import TK_creacion_personaje as creacion_personaje
import TK_seleccion_personaje as seleccion_personaje
from habilidad import Habilidad_Caballero, Habilidad_Mago, Habilidad_Berserker, Habilidad_Exorcista, Habilidad_Alquimista, carga_habilidades, carga_lista_habilidades
import pygame
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista, Enemy, leer_personaje
from arma import Arma, arma_inicial
from habilidad import Habilidad_Caballero, Habilidad_Mago, Habilidad_Berserker, Habilidad_Exorcista, Habilidad_Alquimista, carga_habilidades, carga_lista_habilidades
from gestion_personaje import PerfilPersonaje, PerfilArma
import sys
from COMBATE_clase import Combate
from PIL import Image, ImageTk # biblioteca PIL (Pillow) para cargar y mostrar la imagen. pip install pillow
from musica import musica_fondo, detener_musica
# Crear la ventana principal
root = tk.Tk()
root.title("Code of Legends")
root.geometry("630x560")


#------------------- MUSICA DE FONDO
musica_fondo(0)
#----------------------------------------------------------------
# VARIABLES COMPARTIDAS (IMPORTANTES PARA QUE LAS VENTANAS SECUNDARIAS PUEDAN DEVOLVER UN VALOR A LA VENTANA PRINCIPAL)
#personaje_creado = tk.StringVar()
#personaje = tk.StringVar()
ventana_combate = None # es necesario que exista esta variable previamente para programar la funcion vovler principal que restaura los vbotones de la ventana principal al cerrarse esta

personaje_select = None
# Función de callback para recibir el objeto personaje de ventanas secundarias
def recibir_personaje(personaje):
    global personaje_select
    if personaje:
        label_personaje.config(text=f"Personaje seleccionado:\n{personaje.nombre} ({personaje.oficio})\nNivel {personaje.nivel}", bg="#9bd6c6")
        personaje_select = personaje
# Función para encontrar y seleccionar un personaje ya creado
def abrir_ventana_seleccion():
    seleccion_personaje.abrir_ventana_seleccion_personaje(root, recibir_personaje)

# Función para abrir la ventana secundaria
def abrir_ventana_creacion():
    creacion_personaje.abrir_ventana_creacion_personaje(root, recibir_personaje)

# Función para iniciar combate
def abrir_combate():
    global personaje_select, ventana_combate
    if personaje_select is None:
        label_personaje.config(text=f"Ningún personaje \nseleccionado para usar.", bg="red")
        return
    else:
        ventana_combate = tk.Toplevel(root)
        ventana_combate.protocol("WM_DELETE_WINDOW", volver_principal)#En este código, la función volver_principal se ejecutará automáticamente cuando la ventana secundaria de combate se cierre.
        combate = Combate(ventana_combate, personaje_select)
        boton_abrir.grid_remove()
        boton_select_per.grid_remove()
        boton_crear_per.grid_remove()
        label_personaje.grid_remove()
        label_creditos.grid_remove()
        boton_volver.grid(row=5, column=3, pady=15, sticky="e")
        musica_fondo(2)

    #combate.abrir_ventana_combate(root, recibir_personaje)

def volver_principal():
    global boton_abrir, boton_select_per, boton_crear_per, label_personaje, boton_volver, ventana_combate, personaje_select
    boton_abrir.grid()
    boton_select_per.grid()
    boton_crear_per.grid()
    label_personaje.grid()
    label_creditos.grid()
    boton_volver.grid_remove()
    if personaje_select: # Esto actualiza el nivel del personaje mostrado en label_personaje tras cerrar la ventana combate
        personaje_select = leer_personaje(personaje_select.nombre)
        label_personaje.config(text=f"Personaje seleccionado:\n{personaje_select.nombre} ({personaje_select.oficio})\nNivel {personaje_select.nivel}", bg="#9bd6c6")
    if ventana_combate:
        ventana_combate.destroy()
        #detener_musica()
        musica_fondo(0)

#-------------------- FONDO VETNANA
# Cambiar el color de fondo de la ventana
root.config(bg="lightblue")

# Cargar la imagen de fondo
#imagen_fondo = Image.open("1351305.png")
#imagen_fondo = imagen_fondo.resize((800, 560), Image.LANCZOS)
#imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget Label para la imagen de fondo
from sprites import imagen_fondo_tk
label_fondo = tk.Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
root.imagen_fondo_tk = imagen_fondo_tk
#----------------------------------------------------------------

#-------------------- TITULO DEL JUEGO
# Cargar la imagen de titulo
#imagen_titulo = Image.open("titulo.png")
#imagen_titulo = imagen_titulo.resize((400, 100), Image.LANCZOS)
#imagen_titulo_tk = ImageTk.PhotoImage(imagen_titulo)

# Crear un widget Label para la imagen de fondo
from sprites import imagen_titulo_tk
label_titulo = tk.Label(root, image=imagen_titulo_tk)
label_titulo.grid(row=0,column=3, pady=0, sticky="ew")
root.imagen_titulo_tk = imagen_titulo_tk

# Botón para abrir la ventana secundaria -------> 
boton_abrir = tk.Button(root, text=f"\nComenzar partida\n", font=("Verdana", 16, "bold"), bg="#a4a4a4", command=abrir_combate)
boton_abrir.grid(row=1, column=3, pady=15,sticky="sn")
#boton_abrir.pack(pady=20)

# Botón para abrir la ventana secundaria -------> SELECCION DE PERSONAJE EXISTENTE
boton_select_per = tk.Button(root, text=f"\nSeleccionar\nPersonaje\n", command=abrir_ventana_seleccion)
boton_select_per.grid(row=3, column=1, pady=15)
#boton_select_per.pack(pady=20)

# Botón para abrir la ventana secundaria -------> CREACION DE NUEVO PERSONAJE
boton_crear_per = tk.Button(root, text="Nuevo Personaje", anchor="center", command=abrir_ventana_creacion)
boton_crear_per.grid(row=4, column=1, pady=15)
#boton_crear_per.pack(pady=20)


# Etiqueta para mostrar los atributos del personaje creado y seleccionado
label_personaje = tk.Label(root, text=f"Ningún personaje \nseleccionado para usar.", bg="red")
label_personaje.grid(row=3, column=3, pady=15)
#label_personaje.pack(pady=20)

boton_volver = tk.Button(root, text="Volver a menu principal", command=volver_principal)

label_creditos = tk.Label(root, text=f"Desarrollado por Rodr\n con amor ;)\nVersion 0.0.1", bg="#d1bea1")
label_creditos.grid(row=6, column=4, sticky="w")

# Mantener referencias a las imágenes

# Iniciar el bucle principal de la aplicación
root.mainloop()