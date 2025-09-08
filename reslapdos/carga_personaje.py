import pandas as pd
from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista, Enemy
from arma import Arma, arma_inicial


def leer_personaje(nombre):
        df = pd.read_csv("personajes.csv")  # Leer el archivo CSV
        fila = df.loc[df['Nombre'] == nombre]  # Buscar la fila con el nombre del personaje
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
                    df = pd.read_csv("armas.csv")  # Leer el archivo CSV
                    fila = df.loc[df['Nombre'] == fila['Arma']]  # Buscar la fila con el nombre del arma
                    if not fila.empty:
                        fila = fila.iloc[0]  # iloc sirve para obtener las fila que coinciden, en este caso solo la primera que coincida
                        try:
                            arma = Arma(fila['Nombre'], fila['Potencia'], fila['Arcano'], fila['Proteccion'], fila['Categoria'])
                            print(f"Arma {arma.nombre} leída correctamente")
                            personaje.equipar_arma(arma)
                        except KeyError as error:
                            print(f"Error al leer arma: {error}")
                    else:
                        print("No se encontró el arma")                                
                if personaje:
                    print(f"Personaje {personaje.nombre} leído correctamente")
                    print(f" {personaje.nombre} tiene equipada {personaje.arma.nombre} como arma")
            except KeyError as error:
                print(f"Error al leer personaje: {error}")
        else:
            personaje = None
            print("No se encontró el personaje")
        if personaje:
            return personaje

#--------------- PRUEBA DE USO ---------------
#personaje1 = leer_personaje("Cloud")
#print(personaje1)


