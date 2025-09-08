##################################################################################
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # biblioteca PIL (Pillow) para cargar y mostrar la imagen. pip install pillow
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista, leer_personaje
from arma import Arma, arma_inicial
import os
def abrir_ventana_seleccion_personaje(parent, callback):
    #------------------------------------------------  VENTANA  ------------------------------------------
    # Crear la ventana secundaria
    root =  tk.Toplevel(parent)
    # root = tk.Toplevel(parent)
    root.title("Seleccin de personaje")  # .title(): Establece el título de la ventana
    root.geometry("280x220")  # .geometry(): Establece las dimensiones de la ventana principal

    # Crear un marco para organizar widgets
    frame = tk.Frame(root, padx=10, pady=10)  # tk.Frame(): Crea un contenedor para agrupar widgets
    frame.grid(row=0, column=1, padx=10, pady=10)  # .grid(): Organiza el marco en la ventana principal

    # Etiqueta principal
    label_bienvenida = tk.Label(root, text="Selecciona tu personaje", font=("Arial", 16), fg="black")
    label_bienvenida.grid(row=0, column=3, pady=10) # .pack(): Coloca la etiqueta dentro del marco
    
    # Variable para almacenar la opción seleccionada
    opcion_seleccionada = tk.StringVar()
    opcion_seleccionada.set("Sin seleccion")  # Valor predeterminado

    # Crear el menú desplegable  # IMPORTAR LISTA DE PERSONAJES EXISTENTES
    current_dir = os.path.dirname(os.path.abspath(__file__))# Obtener la ruta del directorio actual (Necesario a la hora de cargar archivos externos
    csv_path = os.path.join(current_dir, "datos", "personajes.csv") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
    df = pd.read_csv(csv_path)  # Leer el archivo CSV
    lista_per = df['Nombre'].tolist()    # Convertir las filas de una sola columna en una lista
    menu_desplegable = tk.OptionMenu(root, opcion_seleccionada, *lista_per)
    menu_desplegable.grid(row=5, column=3)

    label_personaje = tk.Label(root, text="", font=("Arial", 12), fg="black")
    label_personaje.grid(row=6, column=3, pady=10)

    def actualizar_label(*args): 
        #*args se utiliza en las definiciones de funciones para permitir
        # que la función acepte un número variable de argumentos posicionales. 
        # Esto significa que puedes pasar cualquier cantidad de argumentos a la función,
        #  y estos se agruparán en una tupla dentro de la función.
        select_personaje()

        # Asociar la función a la variable de opción seleccionada
    opcion_seleccionada.trace_add("write", actualizar_label)
    #  COMO FUNCIONA TRACE_ADD
    #variable.trace(mode, callback)
    #variable: La variable de control que deseas monitorear (por ejemplo, StringVar).
    #mode: El modo en el que deseas monitorear los cambios. Puede ser "w" (escritura), "r" (lectura) o "u" (eliminación).
    #callback: La función que se llamará cuando ocurra el cambio. Esta función debe aceptar tres argumentos: el nombre de la variable, el índice y el modo.
    #------------------------------------------   FUNCION PARA INICIALIZAR PERSONAJE PREVIAMENTE CREADO (INCLUIDA SU ARMA)  --------------------------
    
    # Metodo para cerrar ventana
    def cerrar_ventana():
        root.destroy()
    

    def select_personaje():
        personaje = leer_personaje(opcion_seleccionada.get())
        if personaje:
            callback(personaje)
        else:
            print("Falló la carga del personaje")

    def confirmar_seleccion():
        select_personaje()
        cerrar_ventana()

    boton_abrir = tk.Button(root, text="Elegir este Personaje", command=confirmar_seleccion)
    boton_abrir.grid(row=10, column=3)

