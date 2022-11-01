# DUNDER
class Persona:
    def __init__(self, edad,nombre) -> None:
        self.__edad = edad
        self.__nombre = nombre
        self.__peso = 15
        self.__lista = ["hola","chau","tarde","noche"]

    def __str__(self) -> str:
        return 'Tengo {} años'.format(self.__edad)

    def __len__(self) -> str:
        return self.__peso

    def __getitem__(self,index) -> str:
        return self.__lista[index]

    def __setitem__(self,index,value) -> str:
        self.__lista[index] = value

    def __contains__(self,item):
        return item in self.__lista

    def __delitem__(self,index):
        return self._lista.pop(index)

    def __iter__(self):
        for index in self.__lista:
            yield index

persona1 = Persona(20,"Marty")
# print(persona1.edad)
# print(persona1)
# print(len(persona1))
# print(persona1[0])
# persona1[0] = 30 ---> # print(persona1[0])
# print("Marty" in persona1)
# del persona1[0] ---> #print(persona1[0])
# for i in persona1:
#     print(i)


# HERENCIA.
class Personaje(Persona):
    def __init__(self, edad, nombre) -> None:
        super().__init__(edad, nombre)


personaje_uno = Personaje(24,"Juan")

print(personaje_uno) # Tengo 24 años
