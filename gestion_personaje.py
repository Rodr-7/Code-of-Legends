import pandas as pd
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista
from arma import Arma, arma_inicial
import os

current_dir = os.path.dirname(os.path.abspath(__file__))# Obtener la ruta del directorio actual (Necesario a la hora de cargar archivos externos
#  esto a la hora de convertir los script en un ejecutable preservando el acceso a los archivos al estar en la misma carpeta)
csv_path = os.path.join(current_dir, "datos", "personajes.csv") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')
csv_path_arm = os.path.join(current_dir, "datos", "armas.csv") # usamos la ruta del directorio actual para cargar todo archivo externo (asumiendo que están en una subcarpeta llamada 'datos')        
                    
#------------------  CLASE PARA INICIALIZAR ARMAS DE PERSONAJES REGISTRADOS  --------------------------
class PerfilArma:
    def __init__(self, nombre_arma, arma=None, archivocsv=csv_path_arm):
        self.nombre_arma = nombre_arma
        self.arma = arma
        self.archivocsv = archivocsv
        pass

    def leer_arma(self):   
        df = pd.read_csv(self.archivocsv)  # Leer el archivo CSV
        fila = df.loc[df['Nombre'] == self.nombre_arma]  # Buscar la fila con el nombre del arma
        if not fila.empty:
            fila = fila.iloc[0]  # iloc sirve para obtener las fila que coinciden, en este caso solo la primera que coincida
            try:
                arma = Arma(fila['Nombre'], fila['Potencia'], fila['Arcano'], fila['Proteccion'], fila['Categoria'])
                self.arma = arma
                print(f"Arma {self.arma.nombre} leída correctamente")
            except KeyError as error:
                print(f"Error al leer arma: {error}")
        else:
            print("No se encontró el arma")

    def actualizar_csv(self):
        if self.arma:
            try:
                df = pd.read_csv(self.archivocsv)
                df.loc[df['Nombre'] == self.arma.nombre, ['Nombre', 'Potencia', 'Arcano', 'Proteccion', 'Categoria']] = [ # Aqui se reemplazan los valores de la fila que coincida con el nombre del arma
                    self.arma.nombre,
                    self.arma.potencia,
                    self.arma.arcano,
                    self.arma.proteccion,
                    self.arma.categoria,
                ]
                df.to_csv(self.archivocsv, index=False)
            except FileNotFoundError as error:
                print(f"Error: {error}")



    def __str__(self):
        return self.arma.__str__()


#------------------------------------------   CLASE PARA INICIALIZAR PERSONAJE PREVIAMENTE CREADO   --------------------------
class PerfilPersonaje: 
    def __init__(self, nombre_personaje, personaje=None,archivocsv=csv_path):
        self.nombre_personaje = nombre_personaje
        self.personaje = personaje
        self.archivocsv = archivocsv
        pass

    def leer_personaje(self):   
        df = pd.read_csv(self.archivocsv)  # Leer el archivo CSV
        fila = df.loc[df['Nombre'] == self.nombre_personaje]  # Buscar la fila con el nombre del personaje
        if not fila.empty:
            fila = fila.iloc[0]  # iloc sirve para obtener las fila que coinciden, en este caso solo la primera que coincida
            try:
                if fila['Oficio'] == "Caballero": #----------   Creando Caballero
                    personaje = Caballero(fila['Nombre'])
                    if fila['Nivel'] > 1:
                        personaje.subir_nivel(fila['Nivel']-1)
                elif fila['Oficio'] == "Mago": #----------   Creando Mago
                    personaje = Mago(fila['Nombre'])
                    if fila['Nivel'] > 1:
                        personaje.subir_nivel(fila['Nivel']-1)
                elif fila['Oficio'] == "Berserker": #----------   Creando Berserker
                    personaje = Berserker(fila['Nombre'])
                    if fila['Nivel'] > 1:
                        personaje.subir_nivel(fila['Nivel']-1)
                elif fila['Oficio'] == "Exorcista": #----------   Creando Exorcista
                    personaje = Exorcista(fila['Nombre'])
                    if fila['Nivel'] > 1:
                        personaje.subir_nivel(fila['Nivel']-1)
                elif fila['Oficio'] == "Alquimista": #----------   Creando Alquimista
                    personaje = Alquimista(fila['Nombre'])
                    if fila['Nivel'] > 1:
                        personaje.subir_nivel(fila['Nivel']-1)
                if fila['Arma'] != "Palo": #--------------------- RESTAURANDO ARMA PREVIAMENTE EQUIPADA
                    arma_equipada = fila['Arma']
                    mi_arma = PerfilArma(arma_equipada)
                    mi_arma.leer_arma()
                    personaje.equipar_arma(mi_arma.arma)
                self.personaje = personaje
                print(f"Personaje {self.personaje.nombre} leído correctamente")
                print(f" {self.personaje.nombre} tiene equipada {self.personaje.arma.nombre} como arma")
            except KeyError as error:
                print(f"Error al leer personaje: {error}")
        else:
            print("No se encontró el personaje")

    def actualizar_csv(self):
        if self.personaje:
            try:
                df = pd.read_csv(self.archivocsv)
                df.loc[df['Nombre'] == self.personaje.nombre, ['Nivel', 'Fuerza', 'Inteligencia', 'Karma', 'Defensa', 'Vida', 'Arma']] = [ # Aqui se reemplazan los valores de la fila que coincida con el nombre del personaje
                    self.personaje.nivel,
                    self.personaje.fuerza,
                    self.personaje.inteligencia,
                    self.personaje.karma,
                    self.personaje.defensa,
                    self.personaje.vida,
                    self.personaje.arma.nombre
                ]
                df.to_csv(self.archivocsv, index=False)
            except FileNotFoundError as error:
                print(f"Error: {error}")

    def subir_niveles(self, niveles):
        self.personaje.nivel = self.personaje.nivel + niveles
        self.personaje.fuerza = self.personaje.fuerza + niveles
        self.personaje.inteligencia = self.personaje.inteligencia + niveles
        self.personaje.karma = self.personaje.karma + niveles
        self.personaje.defensa += niveles
        self.personaje.vida += niveles*10
        self.actualizar_csv()

    def __str__(self):
        return self.personaje.__str__()




#----------------------------------------------------  COMINEZO BUCLE DE GESTION DE PERSONAJE -------------------------------------------------
"""
#class GestionPersonaje:
#def init_personaje:

salir_gestion= False
oficios = ["Caballero", "Mago", "Berserker", "Exorcista", "Alquimista"]
nombre=""
oficio_elec=""
data_per = pd.read_csv('personajes.csv')
while not salir_gestion:
    data_per = pd.read_csv('personajes.csv')
    print("Bienvenido a la gestion de personajes")
    print("0. Continuar personaje")   
    print("1. Crear personaje")
    print("2. Ver personajes")
    print("3. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "0":  #-----REALIZAR CARGA DE PERSONAJE A TRAVES DE LA CLASE PERFIL PERSONAJE
        personaje_elegido = input("Ingrese nombre del personaje que deseas retomar: ")
        mi_personaje = PerfilPersonaje(personaje_elegido)
        mi_personaje.leer_personaje()
        print(mi_personaje.personaje)

#----------------------------------------------------  PROCESO CREACION NUEVO PERSONAJE  -------------------------------------------------


    elif opcion == "1":
        nombre = input("Ingrese el nombre del personaje: ")
        print("Oficios disponibles:")
        for i in oficios:
            print(f"{i}")
        oficio_elec = input("Ingrese el oficio del personaje: ")
        while oficio_elec not in oficios:
            print("Oficio indicado no existe. Oficios disponibles: ")
            for i in oficios:
                print(f"{i}")    
            oficio_elec = input("Ingrese el oficio del personaje: ")
        if oficio_elec == "Caballero":
            nuevo_personaje = Caballero(nombre)
            print(f"Personaje {nombre} creado como {oficio_elec}")

        if oficio_elec == "Mago":
            nuevo_personaje = Mago(nombre)
            print(f"Personaje {nombre} creado como {oficio_elec}")

        if oficio_elec == "Berserker":
            nuevo_personaje = Berserker(nombre) #requiere arma secundaria pero ya debiera estar establecida
            print(f"Personaje {nombre} creado como {oficio_elec}")

        if oficio_elec == "Exorcista":
            nuevo_personaje = Exorcista(nombre)
            print(f"Personaje {nombre} creado como {oficio_elec}")

        if oficio_elec == "Alquimista":
            nuevo_personaje = Alquimista(nombre)
            print(f"Personaje {nombre} creado como {oficio_elec}")
        nuevo_personaje.registrar_personaje() # ---------------  AQUI TERMINA POR REGISTRARSE EL PERSONAJE EN EL CSV

#---------------------------------------------------  OTRAS OPCIONES ------------------------------
    elif opcion == "2":
        print(data_per)
    elif opcion == "3":
        salir_gestion = True
    else:
        print("Opcion no valida")
        continue

"""

#----------------------------------------------------  PRUEBAS  ---------------------------------------------------------------------------------------------------------------------------------
"""
mi_personaje = PerfilPersonaje("Guts")
mi_personaje.leer_personaje()
mi_personaje.subir_niveles(-80)
print(mi_personaje.personaje)

mi_arma = PerfilArma("Uchigatana")
mi_arma.leer_arma()
print(mi_arma.arma)

mi_personaje.personaje.arma = mi_arma.arma
mi_personaje.actualizar_csv()
"""