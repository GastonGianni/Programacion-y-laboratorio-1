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
    lista_seleccionada = []
    while True:
        imprimir_menu()
        respuesta = input("\nRespuesta > ")
        if validaciones.validar_entero(respuesta):
            if respuesta == "1":
                valor_maximo = input("Cuantos héroes desea imprimir? >")
                lista_seleccionada = listar_heroes(lista_recibida,valor_maximo)
            elif respuesta == "2":
                metodo = input('Ingrese metodo de ordenamiento ("Asc" o "Desc") > ')
                lista_seleccionada = ordenar_heroes(lista_recibida, "altura", metodo)
            elif respuesta == "3":
                metodo = input('Ingrese metodo de ordenamiento ("Asc" o "Desc") > ')
                lista_seleccionada = ordenar_heroes(lista_recibida, "fuerza", metodo)
            elif respuesta == "4":
                clave = input('Ingrese clave ("Altura", "Peso" o "Fuerza") > ')
                metodo = input('Ingrese metodo ("Mayor" o "Menor") >')
                lista_seleccionada = listar_y_filtrar(lista_recibida,clave,metodo)
            elif respuesta == "5":
                tipo_inteligencia = input('Ingrese tipo de inteligencia ("Good", "Average" o "High")')
                lista_seleccionada = listar_heroes_por_inteligencia(lista_recibida, tipo_inteligencia)
            elif respuesta == "6":
                exportar_CSV(lista_seleccionada)
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

def sort_list(lista_recibida:list, clave_recibida:str, metodo:str) -> list:
    '''
    Funcion que recorre una lista, genera una copia y ordena el valor de una clave de manera ascendente o descendente.

    Recibe como parametro la lista, la clave y el metodo ["Asc" o "Desc"]

    Retorna la la copia de la lista ordenada o -1 si alguno de los datos es incorrecto.
    '''    
    retorno = -1
    
    if len(lista_recibida) <= 1:
        retorno = lista_recibida
    else: 
        copia_lista = lista_recibida[:]
        lista_izq = []
        lista_der = []
        pivote = copia_lista[0]
        clave_recibida = clave_recibida.lower()
        if validaciones.validar_clave_lista(lista_recibida,clave_recibida):
            if re.search("^asc$", metodo, re.I):
                for elemento in copia_lista[1:]:
                    if elemento[clave_recibida] <= pivote[clave_recibida]:
                        lista_izq.append(elemento)
                    else:
                        lista_der.append(elemento)

                lista_izq = sort_list(lista_izq, clave_recibida, metodo)
                lista_der = sort_list(lista_der, clave_recibida, metodo)
                lista_izq.append(pivote)

                retorno = lista_izq + lista_der
    
            elif re.search("^desc$", metodo, re.I):
                for elemento in copia_lista[1:]:
                    if elemento[clave_recibida] > pivote[clave_recibida]:
                        lista_izq.append(elemento)
                    else:
                        lista_der.append(elemento)

                lista_izq = sort_list(lista_izq, clave_recibida, metodo)
                lista_der = sort_list(lista_der, clave_recibida, metodo)
                lista_izq.append(pivote)

                retorno = lista_izq + lista_der
                
    return retorno

def ordenar_heroes(lista_recibida:list, clave_recibida:str, metodo:str) -> list:
    '''
    Funcion que ordena los valores de una key dentro de una lista.

    Recibe la lista, la clave a ordenar y el metodo ("Asc" o "Desc")

    Retorna e imprime la lista entera ordenada.
    '''
    retorno = sort_list(lista_recibida,clave_recibida,metodo)
    if retorno == -1:
        retorno = "Error"
        print(f'\n{retorno}')
    elif validaciones.validar_lista(lista_recibida) and validaciones.validar_string(clave_recibida) and validaciones.validar_string(metodo):
        for elemento in retorno:
            print('{0} | {1} --> {2}'.format(elemento["nombre"], clave_recibida.capitalize(), elemento[clave_recibida]))

    return retorno

def calcular_promedio_key(lista_recibida:list, key:str) -> float:
    '''
    Funcion que recorre una lista y genera un promedio de una clave.

    Recibe la lista y la clave como parametros.

    Retorna un flotante con el promedio obtenido.
    '''
    acumulador = 0
    for elemento in lista_recibida:
        acumulador += elemento[key]
    promedio = acumulador / len(lista_recibida)
    return promedio
                
def listar_y_filtrar (lista_recibida:list, clave_recibida:str, metodo:str) -> list:
    '''
    Funcion que itera una lista y obtiene un promedio de una clave.
    
    Filtra e imprime los elementos mayores o menores al promedio dependiendo el metodo ingresado("Mayor" o "Menor")

    Retorna e imprime la lista filtrada.
    '''
    mensaje = "\nDatos Incorrectos!"
    lista_a_retornar = []
    if validaciones.validar_lista(lista_recibida) and validaciones.validar_string(clave_recibida) and validaciones.validar_string(metodo) and re.search('^altura$|^peso$|^fuerza$', clave_recibida, re.I) and re.search('^mayor$|^menor$', metodo, re.I):
        metodo = metodo.lower()
        clave_recibida = clave_recibida.lower()
        mensaje = ""
        promedio = calcular_promedio_key(lista_recibida, clave_recibida)
        print(f'\nPromedio de {clave_recibida} -> {promedio}')
        if metodo == 'mayor':
            for elemento in lista_recibida:
                if elemento[clave_recibida] > promedio:
                    lista_a_retornar.append(elemento)
                    mensaje += '\nNombre: {0} || {1} --> {2}'.format(elemento["nombre"],clave_recibida, elemento[clave_recibida])
        else:
            for elemento in lista_recibida:
                if elemento[clave_recibida] < promedio:
                    lista_a_retornar.append(elemento)
                    mensaje += '\nNombre: {0} || {1} --> {2}'.format(elemento["nombre"],clave_recibida, elemento[clave_recibida])        
    
    print(mensaje)
    return lista_a_retornar     

def listar_heroes_por_inteligencia(lista_recibida:list, tipo_inteligencia:str)-> list:
    '''
    Funcion que itera una lista y filtra sus elementos por valor de la clave "inteligencia"

    Recibe como parametro la lista y el tipo de inteligencia ("good", "average", "high")

    Imprime y retorna la lista con los elementos filtrados.
    '''

    mensaje = "Datos incorrectos!"
    lista_a_retornar = []
    if validaciones.validar_lista(lista_recibida) and validaciones.validar_string(tipo_inteligencia) and re.search('^good$|^average$|^high$', tipo_inteligencia, re.I):
        tipo_inteligencia = tipo_inteligencia.lower()
        mensaje = ""
        for elemento in lista_recibida:
            if elemento["inteligencia"] == tipo_inteligencia:
                lista_a_retornar.append(elemento)
                mensaje += "\nNombre: {0} || Inteligencia --> {1}".format(elemento["nombre"], elemento["inteligencia"].capitalize())

    print(mensaje)
    return lista_a_retornar

def exportar_CSV(lista_recibida:list):
    '''
    Funcion que formatea una lista y la exporta como archivo lista.csv

    Recibe como parametro la lista.
    '''  
    if validaciones.validar_lista(lista_recibida) and len(lista_recibida) > 0:   
        with open("lista.csv", "w") as archivo:
            copia_lista = lista_recibida[:]
            for elemento in copia_lista:
                elemento = str(elemento)
                elemento = re.sub("{|}|'", "", elemento)
                archivo.writelines("{}, \n".format(elemento))
            print("\nArchivo 'lista.csv' creado en el directorio")
    else:
        print("\nDatos incorrectos!")
            



