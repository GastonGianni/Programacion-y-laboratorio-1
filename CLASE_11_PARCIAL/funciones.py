'''
SET DE DATOS.
    {
        'nombre': 'Howard the Duck', 
        'identidad': 'Howard (Last name unrevealed)', 
        'altura': 79.35, 
        'peso': 18.45, 
        'fuerza': 2, 
        'inteligencia': ''
    },
    
'''
import re
import json
import validaciones

def importar_json(path_file:str)->list:
    '''
    Funcion que importa un archivo .JSON y lo abre en modo lectura.

    Recibe como parametro el path del archivo.

    Retorna una lista con sus elementos. Retorna un error si el archivo no es formato .json
    '''
    retorno = "Error, el archivo no es formato .JSON"

    if validaciones.validar_json(path_file):
        with open(path_file, "r") as file:
            lista_json = json.load(file)
            retorno = lista_json["heroes"]
    
    return retorno 

def imprimir_menu():
    '''
    Funcion que imprime en consola un menu de opciones.
    '''
    menu = "\n1)Listar los primeros N héroes\n2)Ordenar y listar héroes por altura\n3)Ordenar y listar héroes por fuerza\n4)Calcular promedio y filtrar héroe\n5)Listar héroes por tipo de inteligencia\n6)Exportar CSV\n7)Salir"

    print(menu)

def ingresar_respuesta(lista_recibida):
    '''
    Función que genera un input para ingresar una respuesta.

    Recibe como parametro una lista que será pasada como argumento a cada función ejecutada en diferentes opciones.
    '''
    while True:
        imprimir_menu()
        respuesta = input("\nRespuesta > ")
        if validaciones.validar_entero(respuesta):
            if respuesta == "1":
                valor_maximo = input("Cuantos héroes desea imprimir? >")
                listar_heroes(lista_recibida,valor_maximo)
            elif respuesta == "2":
                print(f"\n{respuesta}")
            elif respuesta == "3":
                print(f"\n{respuesta}")
            elif respuesta == "4":
                print(f"\n{respuesta}")
            elif respuesta == "5":
                print(f"\n{respuesta}")
            elif respuesta == "6":
                print(f"\n{respuesta}")
            elif respuesta == "7":
                break
            else:
                print("\nOpción fuera de rango")
        else:
            print("\nError, ingrese un numero")

def listar_heroes(lista_recibida:list, valor_max:int):
    '''
    Funcion que itera una lista, genera una una copia con N cantidad de elementos ingresados por el usuario (valor_max).

    Recibe la lista y el valor maximo (tipo "int" que no puede superar el tamaño de la lista).

    Imprime el valor de la clave "nombre" de cada elemento y retorna la copia de la lista.
    
    '''

    if validaciones.validar_entero(valor_max) and validaciones.validar_lista(lista_recibida):
        valor_max = int(valor_max)
        if valor_max > len(lista_recibida):
            print("\nError, el valor es mayor que el tamaño de la lista")
        else:
            copia_lista = lista_recibida[:valor_max]
            for elemento in copia_lista:
                print("\n{}".format(elemento["nombre"]))
            return copia_lista
    else:
        print("\nError")

def sort_list(lista_recibida:list, metodo:str) -> list:
    '''
    Funcion que recorre una lista, genera una copia y la ordena de manera ascendente o descendente.

    Recibe como parametro la lista y el metodo ["Asc" o "Desc"]

    Retorna la la copia de la lista ordenada.
    '''    
    


