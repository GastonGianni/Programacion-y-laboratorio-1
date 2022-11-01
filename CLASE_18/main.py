# GETTERS Y SETTERS
class Personaje():
    '''
    Documentación
    '''
    def __init__(self, nombre="") -> None:
        self.__nombre = nombre

    @property # PARA UN GETTER
    def nombre(self): #Getter
        return self.__nombre
    
    @property
    def edad(self):
        return self.calcular_edad()

    @nombre.setter # PARA UN SETTER
    def nuevo_nombre(self,value):
        self.__nombre = value


personaje_1 = Personaje("Pepe")
personaje_2 = Personaje("Juana")
personaje_1.nuevo_nombre = "Pablo"
print(personaje_1.nombre)








