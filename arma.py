import pandas as pd
import random
import os

current_dir = os.path.dirname(os.path.abspath(__file__))# Obtener la ruta del directorio actual (Necesario a la hora de cargar archivos externos
#  esto a la hora de convertir los script en un ejecutable preservando el acceso a los archivos al estar en la misma carpeta)
csv_path_arm = os.path.join(current_dir, "datos", "armas.csv") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')

class Arma:

    def __init__ (self, nombre, potencia, arcano, proteccion, categoria):
        self.nombre = nombre
        self.categoria = categoria
        self.potencia = potencia
        self.arcano = arcano
        self.proteccion = proteccion
        self.poder = self.potencia + self.arcano
        self.id_arma = f"A{random.randint(1, 1000)}{random.choice(self.nombre)}"  # Generar un ID aleatorio entre 1000
#        self.registrar_arma()  # Registrar la instancia al crearla


    def registrar_arma(self):
        data = {
            'ID_arma': [self.id_arma],
            'Nombre': [self.nombre],
            'Categoria': [self.categoria],
            'Potencia': [self.potencia],
            'Arcano': [self.arcano],
            'Proteccion': [self.proteccion],
            'Poder': [self.poder]
        }
        df = pd.DataFrame(data)
        try:
            df_existente = pd.read_csv(csv_path_arm)
            # Generar un nuevo ID único            
            while self.id_arma in df_existente['ID_arma'].values:
                self.id_arma = f"A{random.randint(1, 1000)}{random.choice(self.nombre)}"
                data['ID_arma'] = [self.id_arma]
                df = pd.DataFrame(data)
            # Generar un nuevo Nombre único            
            while self.nombre in df_existente['Nombre'].values:
                self.nombre = f"{self.nombre} ({random.randint(1, 100)})"
                data['Nombre'] = [self.nombre]
                df = pd.DataFrame(data) 
            df = pd.concat([df_existente, df], ignore_index=True)
        except FileNotFoundError as error:
            print(f"Error: {error}")
            pass
        df.to_csv(csv_path_arm, index=False)


    def __str__(self):
        return f"{self.nombre} ({self.categoria}): Potencia {self.potencia} | Arcano {self.arcano} | Proteccion {self.proteccion} | Poder {self.poder}"

    def ver_arma(self):
        print(self.nombre, ":", sep="")
        print("·Categoria:", self.categoria)
        print("·Potencia:", self.potencia)
        print("·Arcano:", self.arcano)
        print("·Proteccion:", self.proteccion)
        print("·Poder:", self.poder," | ")

# CADA CATEGORIA DE ARMA TENDRA UNO DE SUS STATS FIJOS(EJ: TODAS LAS ESPADAS TENDRAN 1 DE PROTECCION)
# Armas de fuerza-------------

arma_inicial=Arma("Palo",1,1,1,"Baston") #Arma inicial para todo personaje-----
#espada = Arma("Espada Maestra",10,10,10,"Espada")
#espada.registrar_arma()
#arma_inicial.ver_arma()
"""
katana= Arma_fisica("uchigatana","espada",40,0,2)
katana.ver_arma()

arma_marcial1 = Arma_marcial("nunchakus","chacos", 5, 0, 4)
arma_marcial1.ver_arma()
"""