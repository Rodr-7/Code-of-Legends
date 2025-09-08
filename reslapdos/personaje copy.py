import pandas as pd
import random
from arma import Arma, arma_inicial
from stats_oficios import stats_caballero, stats_mago, stats_berserker, stats_exorcista, stats_alquimista
class Personaje:

    def __init__(self, nombre, oficio, nivel, fuerza, inteligencia, karma, defensa, vida, arma=arma_inicial, proteger=False):
        self.oficio = oficio
        self.nombre = nombre
        self.nivel = nivel
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.karma = karma
        self.defensa = defensa
        self.vida = vida
        self.arma = arma
        self.proteger = proteger
#       self.registrar_personaje()  # Registrar la instancia al crearla
    
    def registrar_personaje(self):
        data = {
            'Nombre': [self.nombre],
            'Oficio': [self.oficio],
            'Nivel': [self.nivel],
            'Fuerza': [self.fuerza],
            'Inteligencia': [self.inteligencia],
            'Karma': [self.karma],
            'Defensa': [self.defensa],
            'Vida': [self.vida],
            'Arma': [self.arma.nombre]
        }
        df = pd.DataFrame(data)
        try:
            df_existente = pd.read_csv('personajes.csv')
            # Generar un nuevo Nombre único
            numeracion = 1
            nombre_original = self.nombre           
            while self.nombre in df_existente['Nombre'].values:
                self.nombre = nombre_original
                self.nombre = f"{self.nombre}{numeracion}"
                numeracion += 1
                data['Nombre'] = [self.nombre]
                df = pd.DataFrame(data)            
            df = pd.concat([df_existente, df], ignore_index=True)
        except FileNotFoundError as error:
            print(f"Error: {error}")
            pass
        df.to_csv('personajes.csv', index=False)

    def __str__(self):         
        return (
            f"{self.nombre} ({self.oficio}) - Nivel {self.nivel}\n"
            f"Vida: {self.vida}\n"
            f"Fuerza: {self.fuerza}\n"
            f"Inteligencia: {self.inteligencia}\n"
            f"Karma: {self.karma}\n"
            f"Defensa: {self.defensa}\n"
            f"Arma Equipada: {self.arma.nombre}\n")
    
    def ver_atributos(self):
        print(self.nombre, ":", sep="")
        print("·Nivel:", self.nivel)
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Karma:", self.karma)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)
        print("·Arma:", self.arma)

    def subir_nivel(self, nivel): # subida de nivel, todos los atributos aumentan +1 por cada nivel
        self.nivel = self.nivel + nivel
        self.fuerza = self.fuerza + nivel
        self.inteligencia = self.inteligencia + nivel
        self.karma = self.karma + nivel
        self.defensa = self.defensa + nivel
        self.vida += nivel*10


    def equipar_arma(self, arma):
        if not isinstance(arma, Arma):  # Verifica que sea un objeto de tipo Arma
            print(f"{self.nombre} no puede equipar {arma}. No es un arma válida.")
            return
        self.arma = arma
        print(f"{self.nombre} ha equipado el arma: {arma.nombre}")


    def muerte(self):
        return self.vida <= 0 #Verifica si el personaje está muerto
    
    def proteccion(self):
        if self.muerte():
            print(f"{self.nombre} ya no puede hacer nada ¡Ya esta muerto!")
        else:
            self.proteger = True
            print(f"{self.nombre} ha cambiado a posicion defensiva")

#--------------------------- ATAQUE ---------------------------
    def atacar(self, enemigo, danio, enemy_resist):
        if self.proteger:
            print(f"{self.nombre} a cambiado a posicion de ataque.")
        self.proteger = False
        if self.muerte():
            print(f"{self.nombre} ya no puede hacer nada ¡Ya esta muerto!")
        else:
            if enemigo.muerte():
                print(f"{enemigo.nombre} ya está muerto. No puedes atacarlo.")
                return
            
            else:
                danio-= enemy_resist
                if enemigo.proteger:# ----------------- Definicion de daño si el enemigo se protege
                    danio = danio - enemigo.arma.proteccion
                    print(enemigo.nombre, "se esta protegiendo") 
                if danio > 0:
                    enemigo.vida -= danio
                    print(self.nombre, "ha realizado", danio, "puntos de daño a", enemigo.nombre)
                    if enemigo.muerte():
                        enemigo.vida = 0
                        print(enemigo.nombre, "ha muerto")
                    else:
                        print("Vida restante de", enemigo.nombre, ": ",enemigo.vida)   
                else:
                    print("No se produjo daño")


#################################################################   SUBCLASES DE PERSONAJE   ###################################################
#-----------------------------------------------------  CABALLERO  ----------------------------------------------------------------------
class Caballero(Personaje):
    
    def __init__(self, nombre):#Stats predeterminados de la clase en base a la lista de stats de la clase
        super().__init__(nombre, oficio="Caballero", nivel=1, fuerza=stats_caballero[0], inteligencia=stats_caballero[1], karma=stats_caballero[2], defensa=stats_caballero[3], vida=stats_caballero[4], arma=arma_inicial) #valores preestablecidos de la clase Caballero

        
#----------------------------  ATAQUE DE LA CLASE -------------------------------------
    def atacar(self, enemigo):
        super().atacar(enemigo, danio=(self.fuerza + self.arma.potencia), enemy_resist=enemigo.defensa)



#----------------------------  HABILIDADES DE LA CLASE ----------------------------------
    def hab_cab1(self): #voluntad de acero, aumenta ataque y defensa un 20%
        self.fuerza = round(self.fuerza + (self.fuerza*0.2))
        if (self.fuerza*0.2) < 0:
            self.fuerza = self.fuerza + 1
        self.defensa = round(self.defensa + (self.defensa*0.2))
        if (self.defensa*0.2) < 0:
            self.defensa = self.defensa + 1
        print(f"{self.nombre} ha usado Voluntad de Acero:")
        return f"La fuerza de {self.nombre} ha aumentado a {self.fuerza}, y su defensa ha aumentado a {self.defensa}"
    
    def hab_cab2(self): #penitencia vindicadora, aumenta karma en un 20% y reduce ataque en un 10%
        self.karma = round(self.karma + (self.karma*0.2))
        if (self.karma*0.2) < 0:
            self.karma = self.karma + 1
        self.fuerza = round(self.fuerza - (self.fuerza*0.1))
        if (self.fuerza*0.1) < 0:
            self.fuerza = self.fuerza + 1
        if self.fuerza < 0:
            self.fuerza = 0
        print(f"{self.nombre} ha usado Penitencia Vindicadora:")
        return f"El karma de {self.nombre} ha aumentado a {self.karma}, pero su fuerza ha disminuido a {self.fuerza}"


#------------------------------------------------------------------------------------------
#-----------------------------------------------------  MAGO  ----------------------------------------------------------------------
class Mago(Personaje):
    
    def __init__(self, nombre):#Stats predeterminados de la clase en base a la lista de stats de la clase
        super().__init__(nombre, oficio="Mago", nivel=1, fuerza=stats_mago[0], inteligencia=stats_mago[1], karma=stats_mago[2], defensa=stats_mago[3], vida=stats_mago[4], arma=arma_inicial) #valores preestablecidos de la clase Mago

    def __str__(self):
        # Llamamos al __str__ de la clase base (Personaje) y lo ampliamos con información específica
        personaje_str = super().__str__()
        return f"{personaje_str} | Tipo: Mago"


#----------------------------  ATAQUE DE LA CLASE -------------------------------------
    def atacar(self, enemigo):
        super().atacar(enemigo, danio=(self.inteligencia + self.arma.arcano), enemy_resist=enemigo.karma)


#----------------------------  HABILIDADES DE LA CLASE ----------------------------------
    def hab_mag1(self): #Meditacion , aumenta inteligencia y karma un 20%
        self.inteligencia = round(self.inteligencia + (self.inteligencia*0.2))
        if (self.inteligencia*0.2) < 0:
            self.inteligencia = self.inteligencia + 1
        self.karma = round(self.karma + (self.karma*0.2))
        if (self.karma*0.2) < 0:
            self.karma = self.karma + 1
        print(f"{self.nombre} ha usado Meditacion:")
        return f"La inteligenca de {self.nombre} ha aumentado a {self.inteligencia}, y su Karma ha aumentado a {self.karma}"
    
    def hab_mag2(self): # Escudo Arcano , aumenta defensa en un 20% y reduce inteligencia en un 10%
        self.defensa = round(self.defensa + (self.defensa*0.2))
        if (self.defensa*0.2) < 0:
            self.defensa = self.defensa + 1
        self.inteligencia = round(self.inteligencia - (self.inteligencia*0.1))
        if (self.inteligencia*0.1) < 0:
            self.inteligencia = self.inteligencia + 1
        if self.inteligencia < 0:
            self.inteligencia = 0
        print(f"{self.nombre} ha usado Escudo Arcano:")
        return f"La defensa de {self.nombre} ha aumentado a {self.defensa}, pero su inteligencia ha disminuido a {self.inteligencia}"

#------------------------------------------------------------------------------------------
#-----------------------------------------------------  BERSERKER  ----------------------------------------------------------------------
class Berserker(Personaje):
    
    def __init__(self, nombre):#Stats predeterminados de la clase en base a la lista de stats de la clase
        super().__init__(nombre, oficio="Berserker", nivel=1, fuerza=stats_berserker[0], inteligencia=stats_berserker[1], karma=stats_berserker[2], defensa=stats_berserker[3], vida=stats_berserker[4], arma=arma_inicial) #valores preestablecidos de la clase Berserker
    
        
#----------------------------  ATAQUE DE LA CLASE -------------------------------------
    def atacar(self, enemigo): #BERSERKER OBTIENEN UN 10% DE SU VIDA COMO BONUS DE DAÑO
        super().atacar(enemigo, danio=(self.fuerza + self.arma.potencia + round(self.vida*0.05)), enemy_resist=enemigo.defensa)

#----------------------------  HABILIDADES DE LA CLASE -------------------------------------
    def hab_bers1(self): #Frenesi de Furia , aumenta fuerza en un 40%  pero disminuye defensa y karma en un 30%
        self.fuerza = round(self.fuerza + (self.fuerza*0.4))
        if (self.fuerza*0.4) < 1:
            self.fuerza = self.fuerza + 1
        self.defensa = round(self.defensa - (self.defensa*0.3))
        if (self.defensa*0.2) < 1:
            self.defensa = self.defensa - 1
        if self.defensa < 0:
            self.defensa = 0
        self.karma = round(self.karma - (self.karma*0.3))
        if (self.karma*0.2) < 1:
            self.karma = self.karma - 1
        if self.karma < 0:
            self.karma = 0
        print(f"{self.nombre} ha usado Frenesi de Furia:")
        print(f"La fuerza de {self.nombre} ha aumentado a {self.fuerza}, pero su defensa ha disminuido a {self.defensa} y su karma a {self.karma}")
        print(" !!! GRIFFITH !!!!")
#------------------------------------------------------------------------------------------
    def hab_bers2(self): #Redencion , aumenta karma en un 20% y  defensa en un 5%
        self.karma = round(self.karma + (self.karma*0.2))
        if (self.karma*0.2) < 1:
            self.karma = self.karma + 1    
        self.defensa = round(self.defensa + (self.defensa*0.05)) #NO SUBE LOS STAS DEBIDO AL REDONDEO (0.4 ES REDONDEADO A 0)
        if (self.defensa*0.05) < 1:
            self.defensa = self.defensa + 1
        print(f"{self.nombre} ha usado Redencion:")
        print(f"El karma de {self.nombre} ha aumentado a {self.karma},  su defensa ha aumentado a {self.defensa}")
 
#------------------------------------------------------------------------------------------
#-----------------------------------------------------  EXORCISTA  ----------------------------------------------------------------------
class Exorcista(Personaje):  
    
    def __init__(self, nombre):#Stats predeterminados de la clase en base a la lista de stats de la clase
        super().__init__(nombre, oficio="Exorcista", nivel=1, fuerza=stats_exorcista[0], inteligencia=stats_exorcista[1], karma=stats_exorcista[2], defensa=stats_exorcista[3], vida=stats_exorcista[4], arma=arma_inicial) #valores preestablecidos de la clase Exorcista

    def __str__(self):
        # Llamamos al __str__ de la clase base (Personaje) y lo ampliamos con información específica
        personaje_str = super().__str__()
        return f"{personaje_str} | Tipo: Exorcista"

        
#----------------------------  ATAQUE DE LA CLASE -------------------------------------
    def atacar(self, enemigo): #EXORCISTA OBTIENEN UN 50% DE SU KARMA COMO BONUS DE DAÑO, EL ENEMIGO RECIBE EL DAÑO REPARTIDO ENTRE KARMA Y DEFENSA 
        super().atacar(enemigo, danio=round(self.fuerza + (self.karma*0.5) + self.arma.potencia), enemy_resist=round(enemigo.karma*0.5 + enemigo.defensa*0.5))


#----------------------------  HABILIDADES DE LA CLASE ----------------------------------




#------------------------------------------------------------------------------------------
#-----------------------------------------------------  ALQUIMISTA  ----------------------------------------------------------------------
class Alquimista(Personaje):
    
    def __init__(self, nombre):#Stats predeterminados de la clase en base a la lista de stats de la clase
        super().__init__(nombre, oficio="Alquimista", nivel=1, fuerza=stats_alquimista[0], inteligencia=stats_alquimista[1], karma=stats_alquimista[2], defensa=stats_alquimista[3], vida=stats_alquimista[4], arma=arma_inicial) #valores preestablecidos de la clase Exorcista

    def __str__(self):
        # Llamamos al __str__ de la clase base (Personaje) y lo ampliamos con información específica
        personaje_str = super().__str__()
        return f"{personaje_str} | Tipo: Alquimista"


#----------------------------  ATAQUE DE LA CLASE -------------------------------------
    def atacar(self, enemigo):# ALQUMISTA DIRIGE EL DAÑO AL STAT MAS BAJO
        super().atacar(enemigo, danio=round(self.arma.potencia + (self.inteligencia*0.5) + self.fuerza), enemy_resist=min(enemigo.defensa, enemigo.karma))


#----------------------------  HABILIDADES DE LA CLASE -------------------------------------
        #TRANSMUTACION: SELF.ATAQUE Y SELF.POTENCIA.ARMA = A LOS DEL ENEMIGO
    def hab_alq1(self, enemigo): #TRANSMUTACION: SELF.ATAQUE Y SELF.POTENCIA.ARMA = A LOS DEL ENEMIGO
        self.arma.potencia = enemigo.arma.potencia
        

############################  GENERADOR DE PERSONAJE ENEMIGO (GENERACION ALEATORIA POR DEFECTO)####################################
class Enemy:
    def __init__(self, objetivo, enemigo=None,
                 oficios= [Caballero, Mago, Berserker, Exorcista, Alquimista], #Lista de oficios entre los que se designara al enemigo al azar

                 nombres = [    #Lista de nombres entre los que se designara al enemigo al azar
                "Mario",
                "Link",
                "Lara Croft",
                "Master Chief",
                "Kratos",
                "Geralt",
                "Ezio",
                "Samus",
                "Solid Snake",
                "Cloud Strife",
                "Tony Stark",
                "Luke Skywalker",
                "Harry Potter",
                "Frodo Baggins",
                "Katniss Everdeen",
                "Jon Snow",
                "Daenerys Targaryen",
                "Walter White",
                "Rick Grimes",
                "Eleven",
                "Neo",
                "Trinity",
                "John Wick",
                "Maximus",
                "Aragorn",
                "Legolas",
                "Hermione Granger",
                "Batman",
                "Superman",
                "Wonder Woman"
            ]):
        self.objetivo = objetivo
        self.enemigo = enemigo
        self.oficios = oficios
        self.nombres = nombres
        self.generar_enemigo_random() # ---- POR DEFECTO SE GENERA UN ENEMIGO ALEATORIO AL INSTANCIAR

# --------------------- Este metodo generar_enemigo NO esta funcionando, 
# lo mejor sera instanciar el personaje y luego darlo como valor para el atributo enemigo de la clase Enemy
    def generar_enemigo(self, oficio, nombre): # -----------------GENERAR ENEMIGO MANUALMENTE
        try:
            # Buscar la clase correspondiente al oficio
            clase_oficio = next((cls for cls in self.oficios if cls.__name__ == str(oficio)), None)
            # esto es una comprensión de generador.
            # cls.__name__ obtiene el nombre de la clase como una cadena.
            # y filtra las clases cuyo nombre coincide con el nombre del oficio proporcionad

            if clase_oficio is None:
                raise ValueError(f"Oficio '{oficio}' de enemigo no encontrado en la lista de oficios.")
            else:
            # Crear una instancia del enemigo con el nombre dado
                personaje_enemigo = clase_oficio(nombre)
            self.enemigo = personaje_enemigo
        except Exception as error:
            return f"Error al generar enemigo: {error}"

    def generar_enemigo_random(self):   # --------------------GENERACION AUTOMATICA DE ENEMIGO 
        personaje_enemigo = random.choice(self.oficios)(random.choice(self.nombres))
        self.enemigo = personaje_enemigo

    def accion_enemigo(self):
        #Las acciones DEBEN definirse como funciones LAMBDA para que se ejecuten solo cuando se llamen
        # De lo contrario estas se ejecutan al momento de declararse la lista
        acciones_enemigas = [lambda: self.enemigo.atacar(self.objetivo), lambda: self.enemigo.atacar(self.objetivo), lambda: self.enemigo.proteccion()]
        random.choice(acciones_enemigas)()

    def cambio_objetivo(self, nuevo_objetivo):
        self.objetivo = nuevo_objetivo
        return f"{self.enemigo.nombre} será el contrincante de {self.objetivo.nombre}"
    
    def nivelar_enemigo(self):
        nivel_enemigo = self.objetivo.nivel - 2
        self.enemigo.subir_nivel(nivel_enemigo)

    def __str__(self):
        return (
            f"{self.enemigo}\n"
            f"{self.enemigo.nombre} será el contrincante de {self.objetivo.nombre}")


"""
prota = Caballero("Link")
prota.subir_nivel(6)
villano = Enemy(prota)
print(villano)
villano.generar_enemigo(Exorcista, "pedro")
print(villano)
"""

############################  FUNCION INSTANCIADORA DE PERSONAJES YA EXISTENTES ####################################
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
#enemigo1 = Enemy(personaje1)
#enemigo1.enemigo.subir_nivel(3)
#print(enemigo1.enemigo)
#personaje1 = leer_personaje("Cloud")
#print(personaje1)
##############################################################################################################

#----------------------------------------------------  PRUEBAS  ---------------------------------------------------------------------------------------------------------------------------------
#personaje1= Caballero("Cloud")
#print(personaje1)
#personaje1.registrar_personaje()
"""
katana= Arma("uchigatana",40,0,2,"Espada")

personaje1= Alquimista("Edward")
print(personaje1)
personaje2= Berserker("Guts")
print(personaje2)

personaje1.atacar(personaje2)
personaje2.proteger = True
personaje1.atacar(personaje2)
#personaje1.equipar_arma(katana)
personaje1.atacar(personaje2)
personaje2.atacar(personaje1)
personaje1.atacar(personaje2)
personaje2.atacar(personaje1)
personaje2.atacar(personaje1)
personaje1.atacar(personaje2)
personaje1.atacar(personaje2)
"""
"""
personaje2.hab_bers1()
print(personaje2)
personaje2.hab_bers2()
print(personaje2)
"""
"""
katana= Arma_fisica("uchigatana",40,0,2)
personaje1= Caballero("juan",4)
personaje2= Mago("pedro")
print(personaje1)
print(personaje2)
"""



"""
personaje1.subir_nivel(3)
personaje1.ver_atributos()
personaje1.equipar_arma2(katana)
personaje1.ver_atributos()
print(personaje1)
"""
