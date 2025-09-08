import os
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