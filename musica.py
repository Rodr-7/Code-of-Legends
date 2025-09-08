import pygame
import os
import tkinter as tk
# Obtener la ruta del directorio actual (Necesario a la hora de cargar archivos externos
#  esto a la hora de convertir los script en un ejecutable preservando el acceso a los archivos al estar en la misma carpeta)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Lista de canciones
song_list = ["The Legend Of Zelda Wind Waker - Fairy Spring.mp3",   # 0 - Pantalla de titulo
            "DarkSouls_Character_Creation.mp3",  # 1 - Creacion de personaje
             "The_Witcher3-Wild_Hunt_OST-Silver_For_Monsters.mp3", # 2 a 3 - Batalla
             "Undertale_OST-Spider_Dance.mp3",
             "Dark Souls ' You Died ' Sound Effect.mp3", # 4 Muerte del jugador :(
             "Maxwell the Cat Theme.mp3" # 5 Victoria del jugador :)
             ]

def musica_fondo(numero_cancion):
    global current_dir, song_list
    # Reconocer cancion elegida
    cancion = song_list[numero_cancion]
    # Inicializar pygame
    pygame.mixer.init()
    # Cargar y reproducir música
    # Si la musica esta en la misma carpeta usar la siguiente linea:
    #musica_path = os.path.join(current_dir, cancion) # usamos la ruta del directoria actual para cargar todo archivo externo (asumiendo que las imágenes están en la misma carpeta que el archivo .py)
    
    # Si se movio la musica a una subcarpeta dedicada llamada "audio" se debe usar la siguiente linea en lugar de la anterior:
    musica_path = os.path.join(current_dir, "audio", cancion) # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que las canciones están en una subcarpeta llamada 'audio')
    pygame.mixer.music.load(musica_path)
    pygame.mixer.music.play(-1)  # El argumento -1 hace que la música se repita indefinidamente

def detener_musica():
    pygame.mixer.music.stop()


# Interfaz para pruebas
"""
root = tk.Tk()
root.title("Prueba muscia")
root.geometry("600x560")

entrada_nombre = tk.Entry(root, width=30)  # tk.Entry(): Crea un campo de entrada para texto
entrada_nombre.grid(row=0, column=0)
boton_musica = tk.Button(root, text="Iniciar musica", command=lambda: musica_fondo(int(entrada_nombre.get())))
boton_musica.grid(row=1, column=0)
boton_stop_musica = tk.Button(root, text="Detener musica", command=lambda: detener_musica())
boton_stop_musica.grid(row=1, column=1)

#root.mainloop()
"""