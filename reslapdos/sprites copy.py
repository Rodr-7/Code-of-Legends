import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # biblioteca PIL (Pillow) para cargar y mostrar la imagen. pip install pillow
import pygame #pip install pygame 
# --------------  IMAGENES -------------------
    #Caballero
    # Cargar la imagen
imagen = Image.open("Caballero.png")  # La ruta a la imagen  (asumiendo que las imágenes están en la misma carpeta que el archivo .py)
imagen = imagen.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_caballero_tk = ImageTk.PhotoImage(imagen)

    #Mago
    # Cargar la imagen
imagen2 = Image.open("Mago.png")  # La ruta a la imagen
imagen2 = imagen2.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_mago_tk = ImageTk.PhotoImage(imagen2)

    #Berserker
    # Cargar la imagen
imagen3 = Image.open("Berserker.png")  # La ruta a la imagen
imagen3 = imagen3.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_berserker_tk = ImageTk.PhotoImage(imagen3)

    #Exorcista
    # Cargar la imagen
imagen4 = Image.open("Exorcista.png")  # La ruta a la imagen
imagen4 = imagen4.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_exorcista_tk = ImageTk.PhotoImage(imagen4)

    #Alquimista
    # Cargar la imagen
imagen5 = Image.open("Alquimista.png")  # La ruta a la imagen
imagen5 = imagen5.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_alquimista_tk = ImageTk.PhotoImage(imagen5)

    # MUELTO
    # Cargar la imagen
imagen6 = Image.open("dead.jpeg")  # La ruta a la imagen
imagen6 = imagen6.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_muerte_tk = ImageTk.PhotoImage(imagen6)


# FONDO COMBATE
imagen7 = Image.open("fondo2.png")  # La ruta a la imagen
imagen7 = imagen7 
fondo_combat_tk = ImageTk.PhotoImage(imagen7)

