import tkinter as tk
import sys
from PIL import Image, ImageTk # biblioteca PIL (Pillow) para cargar y mostrar la imagen. pip install pillow

# Crear la ventana principal
root = tk.Tk()
root.title("Code of Legends")
root.geometry("600x560")
#-------------------- FONDO VETNANA
# Cambiar el color de fondo de la ventana
root.config(bg="lightblue")

# Cargar la imagen de fondo
imagen_fondo = Image.open("1351305.png")
imagen_fondo = imagen_fondo.resize((800, 560), Image.LANCZOS)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
# Crear un widget Label para la imagen de fondo
label_fondo = tk.Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()