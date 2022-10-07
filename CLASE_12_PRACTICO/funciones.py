'''
    SET DE DATOS.
    {
        "name": "Luke Skywalker",
		"height": "172",
		"mass": "77",
		"gender": "male"  
    }
	{
		"name": "C-3PO",
		"height": "167",
		"mass": "75",
		"gender": "n/a"
	},
'''

import json
import re

def cargar_json(path_file:str)-> list:
    '''
    Función que abre un archivo .json en modo lectura.

    Recibe como parametro el path del archivo.

    Retorna una lista con los datos del archivo.
    '''
    with open(path_file, 'r') as archivo:
        archivo = json.load(archivo)

    return archivo["results"]

def sort_list(lista_recibida:list, clave_recibida:str) -> list:
    '''
    Funcion que itera una lista y ordena sus elementos dependiendo el valor de una clave.

    Recibe la lista a iterar y la clave a comparar

    Retorna la lista ordenada
    '''
    
    lista_izq = []
    lista_der = []

    if len(lista_recibida) <= 1:
        retorno = lista_recibida
    else:
        pivote = lista_recibida[0]
        for elemento in lista_recibida[1:]:
            elemento[clave_recibida] = int(elemento[clave_recibida])
            pivote[clave_recibida] = int(pivote[clave_recibida])
            if elemento[clave_recibida] > pivote[clave_recibida]:
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
        
        lista_izq = sort_list(lista_izq, clave_recibida)
        lista_der = sort_list(lista_der, clave_recibida)
        lista_izq.append(pivote)
        retorno = lista_izq + lista_der

    return retorno

def listar_personajes_ordenados_altura(lista_recibida:list):
    '''
    Funcion que imprime en consola los personajes de una lista ordenados por su altura

    Recibe como parametro la lista a iterar.
    '''
    copia_lista = lista_recibida[:]
    lista_ordenada = sort_list(copia_lista, "height")
    for elemento in lista_ordenada:
        print("\nNombre: {0} | Altura: {1}".format(elemento["name"], elemento["height"]))

def buscar_primer_genero(lista_recibida:list, genero:str) -> dict:
    '''
    Funcion que busca de una lista el primero elemento con la clave genero ingresada.

    Recibe como parametro la lista y el genero ('male', 'female' o 'n/a')

    Retorna el elemento encontrado
    ''' 
    for elemento in lista_recibida:
        if elemento["gender"] == genero:
            return elemento

def mostrar_personaje_mas_alto_genero(lista_recibida:list):
    '''
    Función que imprime en consola el personaje con la clave altura mas grande de cada genero ('male', 'female' o 'n/a')

    Recibe como parametro la lista a iterar.
    '''  
    masculino_mas_alto = buscar_primer_genero(lista_recibida, 'male')
    femenino_mas_alto = buscar_primer_genero(lista_recibida, 'female')
    na_mas_alto = buscar_primer_genero(lista_recibida, 'n/a')

    for elemento in lista_recibida:
        if elemento['gender'] == 'male':
            if elemento["height"] > masculino_mas_alto["height"]:
                masculino_mas_alto = elemento
        elif elemento['gender'] == 'female':
            if elemento["height"] > femenino_mas_alto["height"]:
                femenino_mas_alto = elemento
        else:
            if elemento["height"] > na_mas_alto["height"]:
                na_mas_alto = elemento

    mensaje = "\nMasculino mas alto: {0} | altura: {1}".format(masculino_mas_alto["name"], masculino_mas_alto["height"],)    
    mensaje += "\nFemenino mas alto: {0} | altura: {1}".format(femenino_mas_alto["name"], femenino_mas_alto["height"],)
    mensaje += "\nN/A mas alto: {0} | altura: {1}".format(na_mas_alto["name"], na_mas_alto["height"],)           

    print(mensaje)

def buscador_personaje(lista_recibida:list, valor_buscado:str):
    '''
    Función que busca en una lista el string pasado por parametro.

    Si hay coincidencia lo imprime en consola.

    Si no existe coincidencia imprime un mensaje de error
    '''
    copia_lista = lista_recibida[:]
    mensaje = 'Personaje no encontrado'
    if type(lista_recibida) == list:
        mensaje = ""
        for elemento in copia_lista:
            if re.search(valor_buscado, elemento["name"], re.I):
                mensaje += ("\nPersonaje encontrado: {0}".format(elemento["name"]))
    print(f"{mensaje}\n")

def exportar_csv(lista_recibida:list):
    '''
    Funcion que exporta una lista como archivo .csv

    Recibe como parametro la lista
    '''   
    with open("lista.CSV", "w") as archivo:
        if type(lista_recibida) == list and len(lista_recibida) > 0:
            copia_lista = lista_recibida[:]
            for elemento in copia_lista:
                elemento = str(elemento)
                elemento = re.sub("{|}|'", "", elemento)
                archivo.writelines("{0}, \n".format(elemento))

