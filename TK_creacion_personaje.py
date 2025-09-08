import tkinter as tk
from tkinter import messagebox
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista
from PIL import Image, ImageTk # biblioteca PIL (Pillow) para cargar y mostrar la imagen. pip install pillow
#import pygame #pip install pygame
import os

def abrir_ventana_creacion_personaje(parent, callback):
    creacion_aprobada = False
#----musica de fondo--------------
    #from musica import musica_fondo, detener_musica
    #musica_fondo(1)

    # Crear la ventana secundaria
    root = tk.Toplevel(parent)
    root.title("Creacion de nuevo personaje")  # .title(): Establece el título de la ventana
    root.geometry("800x700")  # .geometry(): Establece las dimensiones de la ventana principal

    # Crear un marco para organizar widgets
    frame = tk.Frame(root, padx=10, pady=10)  # tk.Frame(): Crea un contenedor para agrupar widgets
    frame.grid(row=0, column=1, padx=10, pady=10)  # .grid(): Organiza el marco en la ventana principal

#----imagen de fondo--------------
    # Cambiar el color de fondo de la ventana
    #root.config(bg="brown")
    # Cargar la imagen de fondo
    #imagen_fondo = Image.open("fondo.jpg")
    #imagen_fondo = imagen_fondo.resize((800, 700), Image.LANCZOS)  # Redimensionar la imagen al tamaño de la ventana
    #imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    # Crear un Label para la imagen de fondo
    #label_fondo = tk.Label(frame, image=imagen_fondo_tk)
    #label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
#----------------------------------------



    # Etiqueta principal
    label_bienvenida = tk.Label(root, text="Creación de nuevo personaje", font=("Arial", 16), fg="black")
    label_bienvenida.grid(row=0, column=1, pady=10) # .pack(): Coloca la etiqueta dentro del marco

    # Entrada de texto
    label_nombre = tk.Label(root, text="Escribe el nombre de tu personaje:")  # tk.Label(): Crea una etiqueta para mostrar texto
    label_nombre.grid(row=1, column=1)  # sticky indica la alineacion en .grid (sticky="ew" para centrar)

    entrada_nombre = tk.Entry(root, width=30)  # tk.Entry(): Crea un campo de entrada para texto
    entrada_nombre.grid(row=2, column=1, sticky="ew")  # .pack(): Coloca el campo de entrada dentro del marco

    # Variable para almacenar la opción seleccionada
    opcion_seleccionada = tk.StringVar()
    opcion_seleccionada.set("Sin seleccion")  # Valor predeterminado

    # Etiqueta para indicar la seleccion de clase 
    label_clases = tk.Label(root, text="Selecciona la clase de tu personaje:") # tk.Label(): Muestra el resultado del saludo
    label_clases.grid(row=4, column=1, sticky="ew")

    # Crear el menú desplegable
    menu_desplegable = tk.OptionMenu(root, opcion_seleccionada, "Sin seleccion", "Caballero", "Mago", "Berserker", "Exorcista", "Alquimista")
    menu_desplegable.grid(row=5, column=1)

    # Etiqueta para indicar si se ingreso todo lo solicitado
    label_verificacion = tk.Label(root, text="") # tk.Label(): Muestra el resultado del saludo
    label_verificacion.grid(row=6, column=1, sticky="ew")

    # Metodo para cerrar ventana
    def cerrar_ventana():#       pygame.mixer.music.stop()
        root.destroy()

# ------ ESTO ES IMPORTANTE SI QUIERO PONER MUSICA DE FONDO EN LAS VENTANAS -----
    # Función para detener la música y cerrar la ventana
#    def on_closing():
#        pygame.mixer.music.stop()
#        root.destroy()

    # Sobrescribir el protocolo de cierre de la ventana
#    root.protocol("WM_DELETE_WINDOW", on_closing)
#--------------------------------------------------------------------------------

    def creacion_personaje():
        if opcion_seleccionada.get() == "Caballero":
            nuevo_personaje = Caballero(entrada_nombre.get())

        if opcion_seleccionada.get() == "Mago":
            nuevo_personaje = Mago(entrada_nombre.get())

        if opcion_seleccionada.get() == "Berserker":
            nuevo_personaje = Berserker(entrada_nombre.get())

        if opcion_seleccionada.get() == "Exorcista":
            nuevo_personaje = Exorcista(entrada_nombre.get())

        if opcion_seleccionada.get() == "Alquimista":
            nuevo_personaje = Alquimista(entrada_nombre.get())

        if nuevo_personaje:
            nuevo_personaje.registrar_personaje()
            label_personaje_creado = tk.Label(root, text=f"Personaje {nuevo_personaje.nombre} de clase {nuevo_personaje.oficio} creado correctamente", font=("Arial", 9, "bold"), fg="green")
            label_personaje_creado.grid(row=8, column=1, pady=1)
            # Actualizar la variable compartida con los atributos del personaje
            # Llamar a la función de callback con el objeto personaje
            callback(nuevo_personaje)

    def confirmar_seleccion():
        label_verificacion.config(text=f"")       
        if opcion_seleccionada.get() == "Sin seleccion":
            label_verificacion.config(text=f"Ninguna clase seleccionada", fg="red")
        if entrada_nombre.get() == "":
            label_verificacion.config(text=f"Debes escribir un nombre",  fg="red")
        if opcion_seleccionada.get() == "Sin seleccion" and entrada_nombre.get() == "":
            label_verificacion.config(text=f"No has dado un nombre ni asingado ninguna clase", fg="red")
        if opcion_seleccionada.get() != "Sin seleccion" and entrada_nombre.get() != "":
            #aqui va el metodo que genera el personaje en gestion_personaje.py
            creacion_personaje()
            root.after(2000, cerrar_ventana)  # Espera 3 segundos antes de cerrar la ventana

            # Etiqueta para indicar si se ingreso todo lo solicitado
            #label_personaje_creado = tk.Label(root, text=f"Personaje {entrada_nombre.get()} de clase {opcion_seleccionada.get()} creado correctamente", font=("Arial", 9, "bold"), fg="green")
            #label_personaje_creado.grid(row=8, column=1, pady=1)
            #Se utiliza el método after de Tkinter para programar la llamada a cerrar_ventana después de 3000 milisegundos (3 segundos).
            #root.after(2000, cerrar_ventana)  # Espera 3 segundos antes de cerrar la ventana

    # Botón para confirmar selección
    boton_confirmar = tk.Button(root, text="Confirmar", command=confirmar_seleccion, width=20, height=2)
    boton_confirmar.grid(row=7, column=1, pady=15, sticky="ew")

    # Botón para confirmar selección
    if creacion_aprobada:
        boton_crear = tk.Button(root, text="Crear personaje", command=confirmar_seleccion, width=20, height=3)
        boton_crear.grid(row=5, column=1, columnspan=2, pady=15, sticky="ew")


   # Función para actualizar la opción seleccionada (para usarse al hacer click en las etiquetas de las clases)
    def seleccionar_clase(clase):
        opcion_seleccionada.set(clase)


    ################################  DESCRIPCION DE CLASES ####################
    # --------------  DESCRIPCIONES -------------------
# Obtener la ruta del directorio actual (Necesario a la hora de cargar archivos externos
#  esto a la hora de convertir los script en un ejecutable preservando el acceso a los archivos al estar en la misma carpeta)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # --------------  DESCRIPCIONES -------------------
    # Construir las rutas a los archivos de texto
    caballero_desc_path = os.path.join(current_dir, "textos", "Caballero_descripcion.txt")
    mago_desc_path = os.path.join(current_dir, "textos", "Mago_descripcion.txt")
    berserker_desc_path = os.path.join(current_dir, "textos", "Berserker_descripcion.txt")
    exorcista_desc_path = os.path.join(current_dir, "textos", "Exorcista_descripcion.txt")
    alquimista_desc_path = os.path.join(current_dir, "textos", "Alquimista_descripcion.txt")

    with open(caballero_desc_path, "r") as file:
            desc_caballero = file.read()
        #Esta parte del código abre el archivo "archivo.txt" en modo lectura ("r") 
        # y lee todo su contenido en la variable contenido.
    with open(mago_desc_path, "r") as file:
            desc_mago = file.read()

    with open(berserker_desc_path, "r") as file:
            desc_berserker = file.read()

    with open(exorcista_desc_path, "r") as file:
            desc_exorcista = file.read()

    with open(alquimista_desc_path, "r") as file:
            desc_alquimista = file.read()


    # --------------  IMAGENES -------------------
    # Importadas desde sprites.py
    from sprites import imagen_caballero_tk, imagen_mago_tk, imagen_berserker_tk, imagen_exorcista_tk, imagen_alquimista_tk

    # --------------  CREANDO LAS ETIQUETAS -------------------
    """
    ----------CONFIGURACIONES DE SIDE Y ANCHOR:
    "top": Coloca el widget en la parte superior del contenedor.
    "bottom": Coloca el widget en la parte inferior del contenedor.
    "left": Coloca el widget en el lado izquierdo del contenedor.
    "right": Coloca el widget en el lado derecho del contenedor.
    Opciones para anchor
    El parámetro anchor determina cómo se alineará el widget dentro de su espacio asignado. Las opciones disponibles son:

    "n": Norte (parte superior central).
    "s": Sur (parte inferior central).
    "e": Este (parte derecha central).
    "w": Oeste (parte izquierda central).
    "ne": Noreste (esquina superior derecha).
    "nw": Noroeste (esquina superior izquierda).
    "se": Sureste (esquina inferior derecha).
    "sw": Suroeste (esquina inferior izquierda).
    "center": Centro (valor predeterminado).
    ---------------------------------------------------
    ---------OPCIONES PARA compound
    Las opciones disponibles para compound son:
    "top": La imagen se muestra encima del texto.
    "bottom": La imagen se muestra debajo del texto.
    "left": La imagen se muestra a la izquierda del texto.
    "right": La imagen se muestra a la derecha del texto.
    "center": La imagen se muestra en el centro del texto.
    "none": Solo se muestra la imagen (valor predeterminado si se proporciona una imagen).

    """

    label_caballero = tk.Label(root, text=f"Caballero\n{desc_caballero}", image=imagen_caballero_tk, compound='top')
    label_caballero.image = imagen_caballero_tk  # Mantener una referencia a la imagen para evitar que sea recolectada por el garbage collector
    #label_caballero.pack(side="left", anchor="nw")
    label_caballero.grid(row=10, column=0, padx=10, pady=10, sticky='s')
    label_caballero.bind("<Button-1>", lambda e: seleccionar_clase("Caballero")) # selecciona dicha clase al hacer click en la etiqueta

    label_mago = tk.Label(root, text=f"Mago\n{desc_mago}", image=imagen_mago_tk, compound="top")
    label_mago.image = imagen_mago_tk  # Mantener una referencia a la imagen para evitar que sea recolectada por el garbage collector
    #label_mago.pack(side="bottom", anchor="sw")
    label_mago.grid(row=11, column=2, padx=10, pady=10, sticky='s')
    label_mago.bind("<Button-1>", lambda e: seleccionar_clase("Mago")) # selecciona dicha clase al hacer click en la etiqueta

    label_berserker = tk.Label(root, text=f"Berserker\n{desc_berserker}", image=imagen_berserker_tk, compound="top")
    label_berserker.image = imagen_berserker_tk  # Mantener una referencia a la imagen para evitar que sea recolectada por el garbage collector
    #label_berserker.pack(side="bottom", anchor="n")
    label_berserker.grid(row=10, column=2, padx=10, pady=10, sticky='s')
    label_berserker.bind("<Button-1>", lambda e: seleccionar_clase("Berserker")) # selecciona dicha clase al hacer click en la etiqueta

    label_exorcista = tk.Label(root, text=f"Exorcista\n{desc_exorcista}", image=imagen_exorcista_tk, compound="top")
    label_exorcista.image = imagen_exorcista_tk  # Mantener una referencia a la imagen para evitar que sea recolectada por el garbage collector
    #label_exorcista.pack(side="bottom", anchor="s")
    label_exorcista.grid(row=11, column=0, padx=10, pady=10, sticky='s')
    label_exorcista.bind("<Button-1>", lambda e: seleccionar_clase("Exorcista")) # selecciona dicha clase al hacer click en la etiqueta

    label_alquimista = tk.Label(root, text=f"Alquimista\n{desc_alquimista}", image=imagen_alquimista_tk, compound="top")
    label_alquimista.image = imagen_alquimista_tk  # Mantener una referencia a la imagen para evitar que sea recolectada por el garbage collector
    #label_alquimista.pack(side="bottom", anchor="ne")
    label_alquimista.grid(row=10, column=1, padx=10, pady=10, sticky='s')
    label_alquimista.bind("<Button-1>", lambda e: seleccionar_clase("Alquimista")) # selecciona dicha clase al hacer click en la etiqueta
