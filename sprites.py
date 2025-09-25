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

# -------------------------------- Seccion nueva para animaciones ----------------------------------------------
# === Animación ligera para Labels (Tkinter) ===
from pathlib import Path

# Mapea oficio -> imagen estática ya cargada (fallback)
_OFICIO_STATIC = {
    "Caballero": imagen_caballero_tk,
    "Mago": imagen_mago_tk,
    "Berserker": imagen_berserker_tk,
    "Exorcista": imagen_exorcista_tk,
    "Alquimista": imagen_alquimista_tk,
}

def _load_frames_from_dir(frames_dir: Path, resize_to=(100, 100), pattern="frame_*.png"): # Carga todos los frames de una carpeta
    files = sorted(frames_dir.glob(pattern)) # Ordenar para asegurar el orden correcto de los frames
    if not files: # No hay frames
        return []
    frames = []
    for f in files: # Cargar cada frame
        im = Image.open(f)
        if resize_to:
            im = im.resize(resize_to, Image.LANCZOS) # Redimensionar la imagen si es necesario
        frames.append(ImageTk.PhotoImage(im))
    return frames # Devuelve lista de PhotoImage

def play_animation_on_label(label, frames, fps=12): # Reproduce una lista de PhotoImage en bucle dentro de un Label
    """
    Reproduce una lista de PhotoImage en bucle dentro de un Label.
    Devuelve una función stop() para detener la animación.
    """
    if not frames:
        return lambda: None
    delay = max(1, int(2000 / max(1, fps))) # Retraso entre frames en ms
    state = {"i": 0, "after": None, "alive": True}

    def tick():
        if not state["alive"] or not label.winfo_exists():
            return
        label.config(image=frames[state["i"]], compound="top")
        state["i"] = (state["i"] + 1) % len(frames)
        state["after"] = label.after(delay, tick)

    tick()

    def stop():
        state["alive"] = False
        if state.get("after"):
            try:
                label.after_cancel(state["after"])
            except Exception:
                pass

    return stop

def animate_oficio_on_label(oficio: str, label, fps=12):
    """
    Si hay frames en ./imagenes/<Oficio>_frames/frame_*.png, anima.
    Si no, deja la imagen estática original.
    Adjunta stop en label._stop_anim para poder detener luego.
    """
    # Detener animación anterior si la hubiera
    if hasattr(label, "_stop_anim") and callable(label._stop_anim):
        label._stop_anim()

    frames_dir = Path(current_dir) / "imagenes" / f"{oficio}_frames"
    frames = _load_frames_from_dir(frames_dir, resize_to=(100, 100))
    if frames:
        label._stop_anim = play_animation_on_label(label, frames, fps=fps)
    else:
        # Fallback a imagen estática
        img = _OFICIO_STATIC.get(oficio)
        if img:
            label.config(image=img, compound="top")
        label._stop_anim = lambda: None

def set_static_dead_on_label(label):
    """Muestra sprite de muerte y detiene cualquier animación previa."""
    if hasattr(label, "_stop_anim") and callable(label._stop_anim):
        label._stop_anim()
    label.config(image=imagen_muerte_tk, compound="top")
