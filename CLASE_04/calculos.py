# ---- BLOQUE DE FUNCIONES GENERALES ---- #
def recorrer_y_mostrar(lista:list,clave:str,valor: str, mostrar) -> dict:
    '''
    Funcion que recorre una lista y retorna sus elementos segun el valor de la clave.

    Recibe como parametro la lista (list) a recorrer, una clave (str), el valor excluyente de la clave (str) y que propiedad es la que se muestra (mostrar).

    Retorna un diccionario (-> dict) con los elementos o en el caso de haber algun error, retorna un string "Error"
    '''
    retorno = "Error"
    i = 0

    if type(lista) == type([]) and type(clave) == type(""):
        retorno = {}
        for elemento in lista:
            if elemento[clave] == valor:
                retorno[i] = elemento[mostrar]
                i += 1

        return retorno

def encontrar_primero(lista: list, clave: str, valor) -> dict:
    '''
    Funcion encargada de recorrer una lista y encontrar el primer valor con una caracteristica especifica.

    Recibe como parametro la lista (list) a recorrer, la clave (str) y el valor de la clave.

    Retorna un diccionario con el elemento encontrado o en el caso de haber algun error, retorna un string "Error"
    
    '''
    retorno = "error"
    if type(lista) == type([]) and type(clave) == type(""):
        retorno = {}
        for elemento in lista:
            if elemento[clave] == valor:
                retorno = elemento
                return retorno
                
def maximos_minimos(lista:list, clave: str, caract: str, valor,  tipo: str) -> dict:
    '''
    Funcion que recorre una lista y retorna un maximo o un minimo.

    Recibe como parametro la lista (list) a recorrer, una clave (str) a comparar, una caracteristica excluyente (str), el valor de la caracteristica excluyente y el tipo de operacion (str) que puede ser "Maximo" o "Minimo".

    Retorna un diccionario (-> dict) con los elementos o en el caso de haber algun error, retorna un string "Error"
    '''

    retorno = "Error"

    if type(lista) == type([]) and type(clave) == type("") and type(tipo) == type("") and type(caract) == type(""):
        retorno = encontrar_primero(lista, caract, valor)
        retorno[clave] = float(retorno[clave])
        for elemento in lista:
            elemento[clave] = float(elemento[clave])
            if elemento[clave] > retorno[clave] and elemento[caract] == retorno[caract] and tipo == "Maximo":
                retorno = elemento
            if elemento[clave] < retorno[clave] and elemento[caract] == retorno[caract] and tipo == "Minimo":
                retorno = elemento  
    return retorno

def calcular_promedios(lista: list, clave: str, caract: str, valor) -> int:
    '''
    Funcion encargada de recorrer una lista, acumular valores y calcular un promedio de estos.

    Recibe como parametro una lista a recorrer y una clave con el dato a comparar. Puede recibir una caracteristica excluyente (str) y su respectivo valor.

    Retorna un entero (str) con el promedio obtenido o en el caso de haber algun error, retorna un string "Error"
    '''

    retorno = "Error"

    if type(lista) == type([]) and type(clave) == type("") and type(caract) == type(""):
        acumulador = 0
        contador = 0
        for elemento in lista:
            elemento[clave] = float(elemento[clave])
            if elemento[caract] == valor:
                acumulador += elemento[clave]
                contador += 1
        
        retorno = acumulador / contador

        return retorno

def calcular_cantidad_por_tipo(lista: list, clave: str) -> dict:
    '''
    Funcion que se encarga de recorrer una lista e indicar que cantidad de elementos poseen una caracteristica especifica

    Recibe como parametro la lista a recorrer y la clave.

    Retorna un diccionario (dict) con cada clave y la cantidad de elementos como valor. O retorna "Error" en ese caso.
    '''

    retorno = "Error"

    if type(lista) == type([]) and type(clave) == type(""):
        retorno = {}
        for elemento in lista:
            elemento[clave] = elemento[clave].capitalize()
            if retorno.get(elemento[clave]) != None:
                retorno[elemento[clave]] += 1
            else:
                retorno[elemento[clave]] = 1

        return retorno

def listar_por_tipo(lista: list, clave: str, mostrar) -> dict:
    '''
    Funcion que se encarga de recorrer una lista y agrupar a los elementos basandose en su caracteristica

    Recibe como parametro la lista a recorrer, la clave y que propiedad se desea mostrar.

    Retorna un diccionario (dict) con los elementos agrupados segun su clave .O retorna "Error" en ese caso.
    '''
    retorno = "Error"


    if type(lista) == type([]) and type(clave) == type(""):
        retorno = {}
        for elemento in lista:
            elemento[clave] = elemento[clave].capitalize()
            if retorno.get(elemento[clave]) != None:
                retorno[elemento[clave]] += elemento[mostrar] + " - "
            else:
                retorno[elemento[clave]] = elemento[mostrar] + " - "

        return retorno        
