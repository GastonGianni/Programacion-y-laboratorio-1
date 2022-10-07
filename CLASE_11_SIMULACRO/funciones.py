'''
    SET DE DATOS

        {
			"id": 1,
			"nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
			"poder": 4,
			"fortaleza":["agua"],
			"debilidad":["fuego"]
		},

    ENUNCIADOS 

    1)Listar los últimos N pokemones. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
    2)Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar de manera ascendente ("asc" o descendente ("desc")
    3)Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de manera ascendente o descendente 
    4)Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo), Preguntar qué promedio quiere calcular este esas posibles keys y filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: "mayor" o "menor") se deberá listar en consola aquellos que cumplan con tener mayores o menores cantidades en la lista de dicha key según corresponda.
    5) Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer, muchos de ellos poseen más de un tipo, con lo cual habrá que darle a elegir al usuario entre todos los tipos que existen en el json) una vez seleccionado listar en consola los que posean dicho tipo. (Usando RegEx para la búsqueda).
    Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, deberá listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).
    6)Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]
'''

from ast import Pass
import json
import re
import validaciones

def importar_json(path_file:str)-> list:
    '''
    Funcion que abre un archivo .json en modo lectura 

    Recibe como parametro el path del archivo.

    Retorna una lista o un diccionario depende del formato. En caso de error retorna -1.
    '''
    retorno = -1

    if validaciones.validar_json(path_file):
        with open(path_file, 'r') as archivo:
            archivo = json.load(archivo)
            retorno = archivo
    return retorno

def imprimir_menu():
    '''
    Funcion que imprime en consola un menu de opciones
    '''
    menu = "\n1)Listar los ultimos N pokemones\n2)Ordenar y listar pokemones por poder\n3)Ordenar y listar pokemones por ID\n4)Calcular promedio y filtrar pokemones\n5)Listar pokemones por tipo\n6)Exportar CSV\n7)Salir"

    print(menu)

def ingresar_respuesta(lista_recibida):
    '''
    Función que genera un input para ingresar una respuesta.

    Recibe como parametro una lista que será pasada como argumento a cada función ejecutada en diferentes opciones.
    '''
    lista_seleccionada = []
    while True:
        imprimir_menu()
        respuesta = input("\nRespuesta > ")
        if validaciones.validar_entero(respuesta):
            if respuesta == "1":
                valor_ingresado = input("Imprimir ultimos > ")
                lista_seleccionada = listar_pokemones(lista_recibida,valor_ingresado)
            elif respuesta == "2":
                metodo_ingresado = input("De que forma desea ordenar? ('Asc' o 'Desc') > ")
                lista_seleccionada = ordenar_y_listar(lista_recibida, "poder", metodo_ingresado)
            elif respuesta == "3":
                metodo_ingresado = input("De que forma desea ordenar? ('Asc' o 'Desc') > ")
                lista_seleccionada = ordenar_y_listar(lista_recibida, "id", metodo_ingresado)
            elif respuesta == "4":
                clave_recibida = input("Clave?('Tipo','Evoluciones','Fortaleza','Debilidad')")
                condicion_recibida = input("Mayores o menores al promedio? > ")
                obtener_promedio_y_filtrar(lista_recibida,clave_recibida,condicion_recibida)
            elif respuesta == "5":
                pass
            elif respuesta == "6":
                pass
            elif respuesta == "7":
                break
            else:
                print("\nOpción fuera de rango")
        else:
            print("\nError, ingrese un numero")

def listar_pokemones(lista_recibida:list, valor_ultimos:str)->list:
    '''
    Funcion que itera una lista y crea una copia de los ultimo N elementos.

    Recibe como parametro la lista a iterar y el valor N (valor_ultimos)

    Imprime los elementos formateados por su nombre y retorna la copia de la lista generada.

    En caso de error retorna -1
    '''
    retorno = -1
    valor_ultimos = validaciones.validar_valor_ingresado(lista_recibida,valor_ultimos)

    if type(lista_recibida) == list and len(lista_recibida) > 0 and valor_ultimos > 0:
        copia_lista = lista_recibida[len(lista_recibida)-valor_ultimos:]
        for elemento in copia_lista:
            print("\nNombre: {0}".format(elemento["nombre"]))
        retorno = copia_lista
    else:
        print("\nDatos incorrectos!")

    return retorno

def list_sort(lista_recibida:list, clave_ingresada:str, metodo_ingresado:str)->list:
    '''
    Funcion que ordena de una lista los valores de una clave, de forma ascendente o descendente.

    Recibe como parametro la lista, la clave y el metodo ("asc" o "desc").

    Retorna una copia de la lista original ordenada. En caso de error retorna -1.
    '''
    retorno = -1

    if type(lista_recibida) == list and type(clave_ingresada) == str and re.search('^asc$|^desc$',metodo_ingresado, re.I):
        copia_lista = lista_recibida[:]
        lista_izq = []
        lista_der = []
        if len(copia_lista) <= 1:
            retorno = lista_recibida
        else:
            pivote = copia_lista[0]
            for elemento in copia_lista[1:]:
                if re.search('^asc$', metodo_ingresado, re.I):
                    if elemento[clave_ingresada] > pivote[clave_ingresada]:
                        lista_der.append(elemento)
                    else:
                        lista_izq.append(elemento)
                elif re.search('^desc$', metodo_ingresado, re.I):
                    if elemento[clave_ingresada] > pivote[clave_ingresada]:
                        lista_izq.append(elemento)
                    else:
                        lista_der.append(elemento)
            lista_izq = list_sort(lista_izq,clave_ingresada,metodo_ingresado)
            lista_der = list_sort(lista_der,clave_ingresada,metodo_ingresado)
            lista_izq.append(pivote)
            retorno = lista_izq + lista_der
    else:
        print("\nDatos incorrectos!")

    return retorno

def ordenar_y_listar(lista_recibida:list,clave_ingresada:str,metodo_ingresado:str):
    '''
    Funcion que genera una copia de una lista y la ordena en base al valor de una clave.
    Puede ordenarla de forma ascendente o descendente.
    Recibe por parametro la lista a ordenar, la clave y el metodo ("Asc" o "Desc")

    Retorna la copia de la lista ordenada e imprime sus elementos formateados. En caso de error retorna -1
    '''
    lista_ordenada = list_sort(lista_recibida,clave_ingresada,metodo_ingresado)
    if type(lista_ordenada) == list:
        for elemento in lista_ordenada:
            print('Nombre: {0} | {1} --> {2}'.format(elemento["nombre"], clave_ingresada.capitalize(), elemento[clave_ingresada]))
    
    return lista_ordenada

def calcular_promedio_clave(lista_recibida:list, clave_recibida:str) -> float:
    '''
    Funcion que recorre una lista y genera un promedio del tamaño de una clave.

    Recibe la lista y la clave como parametros.

    Retorna un flotante con el promedio obtenido. Si existe algun error retorna -1
    '''
    promedio = -1
    acumulador = 0
    if type(lista_recibida) == list and clave_recibida in lista_recibida:
        for elemento in lista_recibida:
            acumulador += len(elemento[clave_recibida])
        promedio = acumulador / len(lista_recibida)
    return promedio
    
def obtener_promedio_y_filtrar(lista_recibida:list, clave_recibida:str, condicion_recibida:str)->list:
    ''''''

    lista_a_retornar = []
    mensaje = "\nDatos incorrectos!"
    if type(lista_recibida) == list and re.search("^tipo$|^evoluciones$|^fortaleza$|^debilidad$|", clave_recibida,re.I):
        copia_lista = lista_recibida[:]
        promedio = calcular_promedio_clave(copia_lista,clave_recibida)
        mensaje = ""
        clave_recibida = clave_recibida.lower()
        if promedio > 0:
            print(f"Promedio: {promedio}")
            for elemento in copia_lista:
                if re.search("^mayor$", condicion_recibida, re.I):
                    if len(elemento[clave_recibida]) > promedio:
                        lista_a_retornar.append(elemento)
                        mensaje += "Nombre: {} | {} --> {}".format(elemento["nombre"], clave_recibida.capitalize,elemento[clave_recibida])
                elif re.search("^menor$", condicion_recibida, re.I):
                    if len(elemento[clave_recibida]) < promedio:
                        lista_a_retornar.append(elemento)
                        mensaje += "Nombre: {} | {} --> {}".format(elemento["nombre"], clave_recibida.capitalize,elemento[clave_recibida])
        else:
            mensaje = "\nDatos Incorrectos!"
    print(mensaje)
    return lista_a_retornar
    
