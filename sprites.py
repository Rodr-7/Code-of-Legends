import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # biblioteca PIL (Pillow) para cargar y mostrar la imagen. pip install pillow
import pygame #pip install pygame 
import os

current_dir = os.path.dirname(os.path.abspath(__file__))# Obtener la ruta del directorio actual (Necesario a la hora de cargar archivos externos

# --------------  IMAGENES -------------------
    #Caballero
    # Cargar la imagen
imagen_path_cab = os.path.join(current_dir, "imagenes", "Caballero.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen = Image.open(imagen_path_cab)  # La ruta a la imagen  (asumiendo que las imágenes están en la misma carpeta que el archivo .py)
imagen = imagen.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_caballero_tk = ImageTk.PhotoImage(imagen)

    #Mago
    # Cargar la imagen
imagen_path_mag = os.path.join(current_dir, "imagenes", "Mago.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen2 = Image.open(imagen_path_mag)  # La ruta a la imagen
imagen2 = imagen2.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_mago_tk = ImageTk.PhotoImage(imagen2)

    #Berserker
    # Cargar la imagen
imagen_path_bers = os.path.join(current_dir, "imagenes", "Berserker.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen3 = Image.open(imagen_path_bers)  # La ruta a la imagen
imagen3 = imagen3.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_berserker_tk = ImageTk.PhotoImage(imagen3)

    #Exorcista
    # Cargar la imagen
imagen_path_exo = os.path.join(current_dir, "imagenes", "Exorcista.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen4 = Image.open(imagen_path_exo) # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos'))  # La ruta a la imagen
imagen4 = imagen4.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_exorcista_tk = ImageTk.PhotoImage(imagen4)

    #Alquimista
    # Cargar la imagen
imagen_path_alq = os.path.join(current_dir, "imagenes", "Alquimista.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen5 = Image.open(imagen_path_alq)  # La ruta a la imagen
imagen5 = imagen5.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_alquimista_tk = ImageTk.PhotoImage(imagen5)

    # MUELTO
    # Cargar la imagen
imagen_path_dead = os.path.join(current_dir, "imagenes", "dead.jpeg") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen6 = Image.open(imagen_path_dead)  # La ruta a la imagen
imagen6 = imagen6.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_muerte_tk = ImageTk.PhotoImage(imagen6)

#------ Imagenes ventana principal ------------
    # Imagen de fondo pantalla principal
imagen_path_fondo = os.path.join(current_dir, "imagenes", "1351305.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen_fondo = Image.open(imagen_path_fondo)  # La ruta a la imagen
imagen_fondo = imagen_fondo.resize((800, 560), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    # Imagen de titulo pantalla principal
imagen_path_titulo = os.path.join(current_dir, "imagenes", "titulo.png") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
imagen_titulo = Image.open(imagen_path_titulo)  # La ruta a la imagen
imagen_titulo = imagen_titulo.resize((400, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_titulo_tk = ImageTk.PhotoImage(imagen_titulo)