import re
import json
url_archivo = r'C:\Users\giann\Desktop\utn\Programacion y laboratorio 1\Repositorio GitHub\Programacion-y-laboratorio-1\CLASE_08\data_stark.json'

def importar_json(url: str):
    with open(url) as archivo:
        data = json.load(archivo)

    return data["heroes"] 

lista_personajes = importar_json(url_archivo)

#PARTE UNO

def imprimir_dato(string: str):

  if type(string) == type(''):
    print(string)
  else:
    print("Error, no es un string")

#-----------------------#

def imprimir_menu_desafio_5():
        menu = "\n A) Nombre de cada superheroe masculino\n B) Nombre de cada superheroe femenino\n C) Superheroe mas alto de genero masculino\n D) Superheroe más alto de género femenino\n E) Superheroe más bajo de género masculino\n F) Superheroe más bajo de género femenino\n G) Altura promedio de los superheroes masculinos\n H) Altura promedio de los superheroes femeninos\n I) Nombre de los superheroes asociados a los items anteriores \n J) Superheroes con cada tipo de color de ojos \n K) Superheroes con cada tipo de color de pelo\n L) Superheroes con cada tipo de inteligencia\n M) Superhéroes agrupados por color de ojos \n N) Superhéroes agrupados por color de pelo\n O) Superhéroes agrupados por tipo inteligencia\n Z) Salir\n"

        imprimir_dato(menu)
        
# imprimir_menu_desafio_5()

#-----------------------#

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    respuesta = input("Respuesta >")

    respuesta_valida = re.search('[a-oA-OzZ]', respuesta)
    
    if respuesta_valida == None:
        respuesta_valida = -1
    else:
        respuesta_valida = respuesta.upper()

    return respuesta_valida

# stark_menu_principal_desafio_5()

#-----------------------#

def stark_marvel_app_5(lista_heroes: list):

    while True:
        respuesta = stark_menu_principal_desafio_5()
        if respuesta == 'A':
            print(respuesta)
        elif respuesta == 'B':
            print(respuesta)
        elif respuesta == 'C':
            print(respuesta)
        elif respuesta == 'D':
            print(respuesta)
        elif respuesta == 'E':
            print(respuesta)
        elif respuesta == 'F':
            print(respuesta)
        elif respuesta == 'G':
            print(respuesta)
        elif respuesta == 'H':
            print(respuesta)
        elif respuesta == 'I':
            print(respuesta)
        elif respuesta == 'J':
            print(respuesta)
        elif respuesta == 'K':
            print(respuesta)
        elif respuesta == 'L':
            print(respuesta)
        elif respuesta == 'M':
            print(respuesta)
        elif respuesta == 'N':
            print(respuesta)
        elif respuesta == 'Ñ':
            print(respuesta)
        elif respuesta == 'O':
            print(respuesta)
        elif respuesta == 'Z':
            print(respuesta)
            break
        else:
            print(respuesta)
            break

# stark_marvel_app_5(lista_personajes)

#-----------------------#
        
def leer_archivo(archivo_str:str):
    archivo_valido = re.search(r'[.]+', archivo_str)
    if archivo_valido == None:
        print('Error')
    else:
        return importar_json(archivo_str)

# leer_archivo(url_archivo)

#-----------------------#

def guardar_archivo(nombre_archivo:str, contenido:str):
    retorno = False
    archivo_valido = re.search(r'[.]+', nombre_archivo)
    if archivo_valido == None:
        print('Error al crear el archivo {}'.format(nombre_archivo))
    else:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
            print("Se creo el archivo: {}".format(nombre_archivo))
            retorno = True

    return retorno

# print(guardar_archivo("archivo.json", "Archivo desde guardar_archivo"))
#-----------------------#

def capitalizar_palabras(string: str)-> str:
    lista_str = re.findall("[a-zA-Z]+", string)
    string_cap = ""
    for elemento in lista_str:
        string_cap += elemento.capitalize()
    
    return string_cap

# print(capitalizar_palabras(lista_personajes[16]["nombre"]))
    
#-----------------------#



def obtener_nombre_capitalizado(heroe:dict)-> str:
    retorno = capitalizar_palabras(heroe["nombre"])
    return retorno

# print(obtener_nombre_capitalizado(lista_personajes[0]))

#-----------------------#

def obtener_nombre_y_dato(heroe:dict, key:str):
    nombre = obtener_nombre_capitalizado(heroe)
    clave = capitalizar_palabras(key)
    retorno = "Nombre: {} | {}: {}".format(nombre, clave, heroe[key])

    print(retorno)

# obtener_nombre_y_dato(lista_personajes[4], "inteligencia")

#-----------------------# 

#PARTE DOS

def es_genero(heroe:dict,genero:str)-> bool:
    retorno = False
    genero = genero.upper()
    if genero == 'F' or genero == 'M' or genero == 'NB':
        if heroe["genero"] == genero:
            retorno = True
        
    return retorno

# print(es_genero(lista_personajes[10], "f"))

#-----------------------# 

def stark_guardar_heroe_genero(lista_heroes:list, genero:str):
    nombre = ""
    retorno = False
    genero = genero.capitalize()
    if genero == 'F' or genero == 'M' or genero == 'NB':
        for heroe in lista_heroes:
            if es_genero(heroe,genero) == True:
                nombre += obtener_nombre_capitalizado(heroe) + ","
        
        imprimir_dato(nombre)
        if genero == 'M':
            guardar_archivo("heroes_M.csv", nombre)
        elif genero == 'F':
            guardar_archivo("heroes_F.csv", nombre)
        else:
            guardar_archivo("heroes_NB.csv", nombre)
        
        retorno = True
    
    return retorno

# print(stark_guardar_heroe_genero(lista_personajes, "f"))

#-----------------------# 

#PARTE TRES
