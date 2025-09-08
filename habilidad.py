from personaje import Personaje, Caballero, Mago, Berserker, Exorcista, Alquimista, Enemy, leer_personaje
import random
# deben instanciarse al inicio del script donde se usaran
#-----------------------------------------------------  HABILIDAD  ----------------------------------------------------------------------
class Habilidad:
    def __init__(self, usuario, objetivo, oficio):
        self.usuario = usuario
        self.objetivo = objetivo
        self.oficio = oficio     

    def __str__(self):
        return f"Usuario: {self.usuario.nombre}\nOficio del usuario: {self.oficio }\nObjetivo del usuario: {self.objetivo.nombre}"
    
#----------------------------  HABILIDADES DE CLASE: CABALLERO ----------------------------------
class Habilidad_Caballero(Habilidad):
    def __init__(self, usuario, objetivo):
        super().__init__(usuario, objetivo, oficio="Caballero" )
        self.usuario = usuario
        self.objetivo = objetivo
       
    def hab1(self): #voluntad de acero, aumenta ataque y defensa un 20%
        self.usuario.fuerza = round(self.usuario.fuerza + (self.usuario.fuerza*0.2))
        if (self.usuario.fuerza*0.2) < 0:
            self.usuario.fuerza = self.usuario.fuerza + 1
        self.usuario.defensa = round(self.usuario.defensa + (self.usuario.defensa*0.2))
        if (self.usuario.defensa*0.2) < 0:
            self.usuario.defensa = self.usuario.defensa + 1
        print(f"{self.usuario.nombre} ha usado Voluntad de Acero:")
        print(f"La fuerza de {self.usuario.nombre} ha aumentado a {self.usuario.fuerza}, y su defensa ha aumentado a {self.usuario.defensa}.\n")
    
    def hab2(self): #penitencia vindicadora, aumenta karma en un 20% y reduce ataque en un 10%
        self.usuario.karma = round(self.usuario.karma + (self.usuario.karma*0.2))
        if (self.usuario.karma*0.2) < 0:
            self.usuario.karma = self.usuario.karma + 1
        self.usuario.fuerza = round(self.usuario.fuerza - (self.usuario.fuerza*0.1))
        if (self.usuario.fuerza*0.1) < 0:
            self.usuario.fuerza = self.usuario.fuerza + 1
        if self.usuario.fuerza < 0:
            self.usuario.fuerza = 0
        print(f"{self.usuario.nombre} ha usado Penitencia Vindicadora:")
        print(f"El karma de {self.usuario.nombre} ha aumentado a {self.usuario.karma}, pero su fuerza ha disminuido a {self.usuario.fuerza}.\n")

#------------------------------------------------------------------------------------------
#----------------------------  HABILIDADES DE CLASE: MAGO ----------------------------------
class Habilidad_Mago(Habilidad):
    def __init__(self, usuario, objetivo):
        super().__init__(usuario, objetivo, oficio="Mago")
        self.usuario = usuario
        self.objetivo = objetivo
    
    def hab1(self): #Meditacion , aumenta inteligencia y karma un 20%
        self.usuario.inteligencia = round(self.usuario.inteligencia + (self.usuario.inteligencia*0.2))
        if (self.usuario.inteligencia*0.2) < 0:
            self.usuario.inteligencia = self.usuario.inteligencia + 1
        self.usuario.karma = round(self.usuario.karma + (self.usuario.karma*0.2))
        if (self.usuario.karma*0.2) < 0:
            self.usuario.karma = self.usuario.karma + 1
        print(f"{self.usuario.nombre} ha usado Meditacion:\nLa inteligenca de {self.usuario.nombre} ha aumentado a {self.usuario.inteligencia}, y su Karma ha aumentado a {self.usuario.karma}.\n")
    
    def hab2(self): # Escudo Arcano , aumenta defensa en un 20% y reduce inteligencia en un 10%
        self.usuario.defensa = round(self.usuario.defensa + (self.usuario.defensa*0.2))
        if (self.usuario.defensa*0.2) < 0:
            self.usuario.defensa = self.usuario.defensa + 1
        self.usuario.inteligencia = round(self.usuario.inteligencia - (self.usuario.inteligencia*0.1))
        if (self.usuario.inteligencia*0.1) < 0:
            self.usuario.inteligencia = self.usuario.inteligencia + 1
        if self.usuario.inteligencia < 0:
            self.usuario.inteligencia = 0
        print(f"{self.usuario.nombre} ha usado Escudo Arcano:\nLa defensa de {self.usuario.nombre} ha aumentado a {self.usuario.defensa}, pero su inteligencia ha disminuido a {self.usuario.inteligencia}.\n")

#------------------------------------------------------------------------------------------
#----------------------------  HABILIDADES DE CLASE: BERSERKER ----------------------------------
class Habilidad_Berserker(Habilidad):
    def __init__(self, usuario, objetivo):
        super().__init__(usuario, objetivo, oficio="Berserker")
        self.usuario = usuario
        self.objetivo = objetivo
    
    def hab1(self): #Frenesi de Furia , aumenta fuerza en un 40%  pero disminuye defensa y karma en un 30%
        self.usuario.fuerza = round(self.usuario.fuerza + (self.usuario.fuerza*0.4))
        if (self.usuario.fuerza*0.4) < 1:
            self.usuario.fuerza = self.usuario.fuerza + 1
        self.usuario.defensa = round(self.usuario.defensa - (self.usuario.defensa*0.3))
        if (self.usuario.defensa*0.2) < 1:
            self.usuario.defensa = self.usuario.defensa - 1
        if self.usuario.defensa < 0:
            self.usuario.defensa = 0
        self.usuario.karma = round(self.usuario.karma - (self.usuario.karma*0.3))
        if (self.usuario.karma*0.2) < 1:
            self.usuario.karma = self.usuario.karma - 1
        if self.usuario.karma < 0:
            self.usuario.karma = 0
        print(f"{self.usuario.nombre} ha usado Frenesí de Furia:")
        print(f"La fuerza de {self.usuario.nombre} ha aumentado a {self.usuario.fuerza}, pero su defensa ha disminuido a {self.usuario.defensa} y su karma a {self.usuario.karma}")
        print(f" !!! GRIFFITH !!!!\n")
#------------------------------------------------------------------------------------------
    def hab2(self): #Redencion , aumenta karma en un 20% y  defensa en un 5%
        self.usuario.karma = round(self.usuario.karma + (self.usuario.karma*0.2))
        if (self.usuario.karma*0.2) < 1:
            self.usuario.karma = self.usuario.karma + 1    
        self.usuario.defensa = round(self.usuario.defensa + (self.usuario.defensa*0.05)) #NO SUBE LOS STAS DEBIDO AL REDONDEO (0.4 ES REDONDEADO A 0)
        if (self.usuario.defensa*0.05) < 1:
            self.usuario.defensa = self.usuario.defensa + 1
        print(f"{self.usuario.nombre} ha usado Redencion:")
        print(f"El karma de {self.usuario.nombre} ha aumentado a {self.usuario.karma},  su defensa ha aumentado a {self.usuario.defensa}.\n")
 
#------------------------------------------------------------------------------------------
#----------------------------  HABILIDADES DE CLASE: EXORCISTA ----------------------------------
class Habilidad_Exorcista(Habilidad):
    def __init__(self, usuario, objetivo):
        super().__init__(usuario, objetivo, oficio="Exorcista")
        self.usuario = usuario
        self.objetivo = objetivo

    def hab1(self): #Justicia karmica: aumenta el karma un 20% por cada stat del usuario que sea menor que su respectivo del objetivo
        lista_stats_usuario = [self.usuario.fuerza, self.usuario.inteligencia, self.usuario.defensa, self.usuario.karma]
        lista_stats_objetivo = [self.objetivo.fuerza, self.objetivo.inteligencia, self.objetivo.defensa, self.objetivo.karma]
        print(f"{self.usuario.nombre} ha usado Justicia Karmica.\nEl universo ha sido llamado a traer equilibrio.")
        for i in range(len(lista_stats_usuario)):
            if lista_stats_usuario[i] < lista_stats_objetivo[i]:
                if self.usuario.karma < 1:
                    self.usuario.karma = 1
                self.usuario.karma = round(self.usuario.karma + round(self.usuario.karma*0.2))
                print(f"El karma de {self.usuario.nombre} ha aumentado a {self.usuario.karma} para menguar la disparidad.\n")

    def hab2(self): # Maldicion: reduce el karma del usuario en un 90% y baja todos los stats del objetivo en un 30%
        print(f"{self.usuario.nombre} ha usado Maldicion.")
        if self.usuario.karma > 2:
            self.objetivo.fuerza =- round(self.objetivo.fuerza*0.3)
            self.objetivo.inteligencia =- round(self.objetivo.inteligencia*0.3)
            self.objetivo.defensa =- round(self.objetivo.defensa*0.3)
            self.objetivo.karma =- round(self.objetivo.karma*0.3)
            self.usuario.karma =- round(self.usuario.karma *0.9)
            if self.usuario.karma < 1:
                self.usuario.karma = 1
            print(f"{self.usuario.nombre} ha maldecido a {self.objetivo.nombre}.")
            print(f"Todas las estadisticas de {self.objetivo.nombre} han disminuido en un 30%")
            print(f"El karma de {self.usuario.nombre} ha disminuido a {self.usuario.karma}.\n")
        else:
            print(f"Pero el karma de {self.usuario.nombre} es insuficiente.\n")

#------------------------------------------------------------------------------------------
#----------------------------  HABILIDADES DE CLASE: ALQUIMISTA ----------------------------------
class Habilidad_Alquimista(Habilidad):
    def __init__(self, usuario, objetivo):
        super().__init__(usuario, objetivo, oficio="Alquimista")
        self.usuario = usuario
        self.objetivo = objetivo

    def hab1(self): #Transmutacion: equipara lo stats  del usuario con el del objetivo si estos son mas bajos
        print(f"{self.usuario.nombre} ha usado Transmutacion.\nLas estadisticas de {self.usuario.nombre} han sido alteradas para adaptarse a {self.objetivo.nombre}")
        if self.usuario.fuerza < self.objetivo.fuerza:
            self.usuario.fuerza = self.objetivo.fuerza - 1
            print(f"La fuerza de {self.usuario.nombre} ahora es {self.usuario.fuerza}")

        if self.usuario.inteligencia < self.objetivo.inteligencia:
            self.usuario.inteligencia = self.objetivo.inteligencia - 1
            print(f"La inteligencia de {self.usuario.nombre} ahora es {self.usuario.inteligencia}")

        if self.usuario.defensa < self.objetivo.defensa:
            self.usuario.defensa = self.objetivo.defensa - 1
            print(f"La defensa de {self.usuario.nombre} ahora es {self.usuario.defensa}")

        if self.usuario.karma < self.objetivo.karma:
            self.usuario.karma = self.objetivo.karma - 1
            print(f"El karma de {self.usuario.nombre} ahora es {self.usuario.karma}")

    
    def hab2(self): #Equivalencia: Cambia los stats del usuario y del objetivo por un promedio entre ambos 
        prom_fuerza = round((self.usuario.fuerza + self.objetivo.fuerza)/2)
        if prom_fuerza < 1:
            prom_fuerza = 1
        prom_inteligencia = round((self.usuario.inteligencia + self.objetivo.inteligencia)/2)
        if prom_inteligencia < 1:
            prom_inteligencia = 1
        prom_defensa = round((self.usuario.defensa + self.objetivo.defensa)/2)
        if prom_defensa < 1:
            prom_defensa = 1
        prom_karma = round((self.usuario.karma + self.objetivo.karma)/2)
        if prom_karma < 1:
            prom_karma = 1
        self.usuario.fuerza = prom_fuerza
        self.usuario.inteligencia = prom_inteligencia
        self.usuario.defensa = prom_defensa
        self.usuario.karma = prom_karma
        self.objetivo.fuerza = prom_fuerza
        self.objetivo.inteligencia = prom_inteligencia
        self.objetivo.defensa = prom_defensa
        self.objetivo.karma = prom_karma
        print(f"{self.usuario.nombre} ha usado Equivalencia.\nLas estadisticas de {self.usuario.nombre} y {self.objetivo.nombre} han cambiado!")
        print(f"La fuerza de {self.usuario.nombre} y {self.objetivo.nombre} ahora es {prom_fuerza}")
        print(f"La inteligencia de {self.usuario.nombre} y {self.objetivo.nombre} ahora es {prom_inteligencia}")
        print(f"La defensa de {self.usuario.nombre} y {self.objetivo.nombre} ahora es {prom_defensa}")
        print(f"El karma de {self.usuario.nombre} y {self.objetivo.nombre} ahora es {prom_karma}")
        print(self.usuario)
        print(self.objetivo)


#------------------------------------------------------------------------------------------
#------ HABILIDADES LISTADAS ----------------------
hab_cab = ["Voluntad de Acero", "Penitencia Vindicadora"]
hab_mag = ["Meditacion", "Escudo Arcano"]
hab_bers = ["Frenesí de Furia", "Redencion"]
hab_exo = ["Justicia karmica", "Maldicion"]
hab_alq = ["Transmutacion", "Equivalencia"]

#----   Funcion encargada de instanciar las habilidades, otorgandole un usuario y objetivo   -------------------------------------------------------------------------------------
def carga_habilidades(usuario, objetivo):
    if usuario.oficio == "Caballero":
        return Habilidad_Caballero(usuario, objetivo) 
    elif usuario.oficio == "Mago":
        return Habilidad_Mago(usuario, objetivo) 
    elif usuario.oficio == "Berserker":
        return Habilidad_Berserker(usuario, objetivo) 
    elif usuario.oficio == "Exorcista":
        return Habilidad_Exorcista(usuario, objetivo) 
    elif usuario.oficio == "Alquimista":
        return Habilidad_Alquimista(usuario, objetivo)
    else:
        return "sin habilidad"

#----   Funcion encargada de crear la lista de las habilidades correspondientes a un usuario, para poder ser visualizadas    -------------------------------------------------------------------------------------
def carga_lista_habilidades(usuario):
    if usuario.oficio == "Caballero":
        return hab_cab 
    elif usuario.oficio == "Mago":
        return hab_mag 
    elif usuario.oficio == "Berserker":
        return hab_bers
    elif usuario.oficio == "Exorcista":
        return hab_exo 
    elif usuario.oficio == "Alquimista":
        return hab_alq
    else:
        return "sin habilidad"


"""
lista_hab_cab = [Habilidad_Caballero.hab_cab1, Habilidad_Caballero.hab_cab2]
lista_hab_mag = [Habilidad_Mago.hab_cab1, Habilidad_Mago.hab_cab2]
hab_bers_met = [Habilidad_Berserker.hab_bers1, Habilidad_Berserker.hab_bers2]
lista_hab_exo = [Habilidad_Exorcista.hab_cab1,Habilidad_Exorcista.hab_cab2]
lista_hab_alq = [Habilidad_Alquimista.hab_cab1, Habilidad_Alquimista.hab_cab2]



"""