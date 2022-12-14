import re
import json

def importar_json(url: str) -> list:
    """
    Funcion que importa un archivo .json y lo retorna como una lista

    Se pasa la url como parametro. (string)

    """
    with open(url) as archivo:
        data = json.load(archivo)

    return data["heroes"]

# 1- Listar los primeros N héroes. El valor de N será ingresado por el usuario (Validar que no supere max. de lista)
def validar_entero(string_recibido)->int:

    if re.search("^[0-9]+$", string_recibido) is None:
        print("\n///INGRESE UN NUMERO///\n")
        return False
    else:
        return int(string_recibido)

def listar_heroes(lista_recibida: list, valor_max:str = "1") -> list:

    """
    Función que recorre una lista e imprime la cantidad de elementos hasta la cantidad maxima ingresada (Valor 1 por defecto).

    Recibe como parametros la lista a iterar (no debe estar vacía) y el valor maximo (no debe superar el tamaño maximo de la lista ingresada)

    Imprime la lista y la Retorna.

    Si existe un error imprime en consola "Error"
    """

    valor_max = validar_entero(valor_max)
    if valor_max == False:
        return

    retorno = "Error"
    if len(lista_recibida) > 0 and type(lista_recibida) == list and valor_max > 0 and valor_max <= len(lista_recibida):
        copia_lista = lista_recibida[:]
        lista_a_retornar = []
        mensaje = ""
        for elemento in copia_lista[0:valor_max]:
            lista_a_retornar.append(elemento)
            mensaje += "{0}\n".format(elemento["nombre"])
        
        retorno = lista_a_retornar
        print(f"\n{mensaje}")

    elif len(lista_recibida) < 1:
        retorno = "Error. lista vacía"
    elif valor_max > len(lista_recibida):
        print("\nValor maximo supera el tamaño de la lista!\n")

    return retorno

# 2- Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

# FUNCIONES DE ORDENAMIENTO.

def sort_list_asc(lista_a_ordenar:list, key:str):

    copia_lista = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        pivot = copia_lista[0]
        for elemento in copia_lista[1:]:
            if(elemento[key] > pivot[key]):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

        lista_izq = sort_list_asc(lista_izq,key)
        lista_der = sort_list_asc(lista_der,key)
        lista_izq.append(pivot)

    return lista_izq + lista_der

def sort_list_desc(lista_a_ordenar:list, key:str):

    copia_lista = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        pivot = copia_lista[0]
        for elemento in copia_lista[1:]:
            if(elemento[key] < pivot[key]):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

        lista_izq = sort_list_desc(lista_izq,key)
        lista_der = sort_list_desc(lista_der,key)
        lista_izq.append(pivot)

    return lista_izq + lista_der

def ordenar_heroes_por_altura(lista_recibida: list, metodo:str)-> list:
    '''
    Funcion que itera una lista y ordena a sus elementos segun su clave "altura".

    La lista puede ser ordenada de forma Ascendente o Descendente.

    Recibe como parametro la lista a iterar y el metodo de ordenamiento ("asc" o "desc").

    Imprime y retorna la lista ordenada. Si hubo algun error imprime "Error".

    '''

    lista_a_retornar = "Error"
    metodo_validado = re.search('^asc$|^desc$', metodo, re.IGNORECASE)

    if metodo_validado == None:
        print("Error, ingrese metodo correcto")
    else:
        
        if len(lista_recibida) > 0 and type(lista_recibida) == list:
            copia_lista = lista_recibida[:]
            mensaje = ""
            if re.search("desc", metodo, re.IGNORECASE) == None:
                alturas_ordenadas_asc = sort_list_asc(copia_lista, "altura")
                lista_a_retornar = []
                for elemento in alturas_ordenadas_asc:
                    lista_a_retornar.append(elemento)
                    mensaje += "Nombre: {0} | Altura: {1}\n".format(elemento["nombre"], elemento["altura"])
            else:
                alturas_ordenadas_desc = sort_list_desc(copia_lista, "altura")
                lista_a_retornar = []
                for elemento in alturas_ordenadas_desc:
                    lista_a_retornar.append(elemento)
                    mensaje += "Nombre: {0} | Altura: {1}\n".format(elemento["nombre"], elemento["altura"])

            print(mensaje)
            return lista_a_retornar

# 3- Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

def ordenar_heroes_por_fuerza(lista_recibida:list, metodo:str)-> list:
    '''
    Funcion que itera una lista y ordena a sus elementos segun su clave "fuerza".

    La lista puede ser ordenada de forma Ascendente o Descendente.

    Recibe como parametro la lista a iterar y el metodo de ordenamiento ("asc" o "desc").

    Imprime y retorna la lista ordenada. Si hubo algun error imprime "Error".

    '''

    lista_a_retornar = "Error"
    metodo_validado = re.search('asc|desc', metodo, re.IGNORECASE)

    if metodo_validado == None:
        print("Error, ingrese metodo correcto")
    else:
        
        if len(lista_recibida) > 0 and type(lista_recibida) == list:
            copia_lista = lista_recibida[:]
            if re.search("desc", metodo, re.IGNORECASE) == None:
                fuerzas_ordenadas_asc = sort_list_asc(copia_lista, "fuerza")
                lista_a_retornar = []
                for elemento in fuerzas_ordenadas_asc:
                    lista_a_retornar.append(elemento)
                    print("Nombre: {0} | Fuerza: {1}".format(elemento["nombre"], elemento["fuerza"]))
            else:
                fuerzas_ordenadas_desc = sort_list_desc(copia_lista, "fuerza")
                lista_a_retornar = []
                for elemento in fuerzas_ordenadas_desc:
                    lista_a_retornar.append(elemento)
                    print("Nombre: {0} | Fuerza: {1}".format(elemento["nombre"], elemento["fuerza"]))
            
            return lista_a_retornar

# 4- Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio 
# (preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

# FUNCION PROMEDIO 

def calcular_promedio_key(lista_recibida:list, key:str):
    copia_lista = lista_recibida[:]
    acumulador = 0
    for elemento in copia_lista:
        acumulador += elemento[key]

    promedio = acumulador / len(copia_lista)

    return promedio

def calcular_promedio_y_filtrar(lista_recibida: list, key:str, condicion: str):
    '''
    Funcion que recorre una lista y obtiene un promedio de la key ingresada como parametro.

    Filtra los elementos que tengan en su key un valor mayor o menor al promedio.

    Recibe como parametro la lista a iterar, la key de promedio, y la condicion ("Mayor" o "Menor")

    Retorna una lista con los elementos filtrados.
    '''

    key_validada = re.match("fuerza|altura|peso", key, re.IGNORECASE)
    condicion_validada = re.match("mayor|menor", condicion, re.IGNORECASE)

    if key_validada == None:
        print("Error, ingrese clave correcta (Fuerza, Altura, Peso)")
    else:
        key = key.lower()
        promedio_key = calcular_promedio_key(lista_recibida, key)
        if condicion_validada == None:
            print("Error, ingrese condicion correcta ('Mayor' o 'Menor')")
        else:
            condicion = condicion.lower()
            lista_a_retornar = []
            mensaje = ""
            for elemento in lista_recibida:
                if condicion == 'mayor' and elemento[key] > promedio_key:
                    lista_a_retornar.append(elemento)
                    mensaje += "Nombre: {0} | {1}: {2}\n".format(elemento["nombre"], key, elemento[key])
                elif condicion == 'menor' and elemento[key] < promedio_key:
                    lista_a_retornar.append(elemento)
                    mensaje += "Nombre: {0} | {1}: {2}\n".format(elemento["nombre"], key, elemento[key])
            print("Promedio: {0}\n".format(promedio_key))
            print(mensaje)

            return lista_a_retornar

# 5- Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.

def buscar_heroes_por_inteligencia(lista_recibida: list, tipo_inteligencia: str):
    '''
    Funcion que itera una lista y filtra sus elementos por el valor de la clave "inteligencia".

    Recibe como parametro la lista a iterar y el valor de la clave inteligencia ("Good", "Average", "High")

    Retorna la lista con los elementos que coincidan con el tipo de inteligencia ingresado.
    '''
    lista_a_retornar = []
    tipo_inteligencia_validado = re.search("^good$|^average$|^high$", tipo_inteligencia, re.IGNORECASE)

    if tipo_inteligencia_validado == None or len(lista_recibida) < 1:
        print("Error. Ingrese tipo de inteligencia correcto (Good, Average, High)")
    elif len(lista_recibida) > 1 and type(lista_recibida) == list:
        tipo_inteligencia = tipo_inteligencia.lower()
        copia_lista = lista_recibida[:]
        lista_a_retornar = []
        mensaje = ""
        for elemento in copia_lista:
                if elemento["inteligencia"] == tipo_inteligencia:
                    mensaje += ("Nombre: {0} | Inteligencia: {1}\n".format(elemento["nombre"], elemento["inteligencia"].capitalize()))
                    lista_a_retornar.append(elemento)
        print(f'\n{mensaje}\n')
    elif len(lista_recibida) == 1:
        lista_a_retornar = lista_recibida
        
    return lista_a_retornar

# 6-  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

def exportar_csv(lista_recibida: list):
    '''
    Funcion que toma una lista de diccionarios y exporta un archivo formato .CSV con sus elementos y claves.

    Recibe como parametro la lista a exportar y las claves (Por defecto la clave es "nombre").

    Si desea imprimir mas de una clave, separarlas por un "-" sin espacios (MAXIMO 2 CLAVES)

    Retorna el archivo "lista.CSV" en el directorio.
    '''
    with open("lista.CSV", "w") as archivo:
        if type(lista_recibida) == list and len(lista_recibida) > 0:
            copia_lista = lista_recibida[:]
            for elemento in copia_lista:
                elemento = str(elemento)
                elemento = re.sub("{|}|'", "", elemento)
                archivo.writelines("{}, \n".format(elemento))
        else:
            print("\n///ERROR, LISTA VACÍA///\n")