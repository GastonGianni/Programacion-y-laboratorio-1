import re

#---FUNCIONES DE VALIDACION---#

def validar_string(string_recibido:str)-> bool:
    '''
    Funcion que valida si lo recibido por parametro es un string, y en ese caso, evalua que todos su caracteres sean alfabéticos (sin espacios).

    Recibe como parametro el string a validar.

    Retorna True si es un string de tipo alfabetico o False en caso contrario.
    '''
    retorno = False

    if type(string_recibido) == str and re.search("[^a-z]+", string_recibido, re.IGNORECASE) == None and len(string_recibido) > 0:
        retorno = True
    
    return retorno

#print(validar_string("hola10"))

def validar_entero(string_recibido:str)-> bool:
    '''
    Funcion que valida si lo recibido por parametro es un string, y en ese caso, evalua que todos su caracteres sean numeros enteros.

    Recibe como parametro el string numerico a validar.

    Retorna True si es un string con numeros enteros o False en caso contrario.
    '''
    retorno = False

    if type(string_recibido) == str and re.search("[^0-9]+", string_recibido) == None and len(string_recibido) > 0:
        retorno = True
    
    return retorno

# print(validar_entero("2a2"))

def validar_json(path_recibido:str)-> bool:
    '''
    Funcion que valida si el path recibido es de tipo string y si corresponde a un archivo con extension .JSON.

    Recibe como parametro el PATH (str)

    Retorna True si el archivo es tipo JSON o False en caso contrario.
    '''
    retorno = False
    if type(path_recibido) == str and len(path_recibido) > 0:
        if re.search("\.json$",path_recibido, re.I):
            retorno = True

    return retorno

# print(validar_json(".\CLASE_11_PARCIAL\data_stark.json"))

def validar_lista(lista_recibida:list) ->bool:
    '''
    Funcion que valida si lo ingresado por parametro es de tipo lista

    Retorna True en caso de serlo o False en caso contrario.
    '''
    retorno = False
    if type(lista_recibida) == list:
        retorno = True

    return retorno

# lista = []
# print(validar_lista(lista))

def validar_clave_lista(lista_recibida:list, clave_recibida:str) -> bool:
    '''
    Funcion que valida si dentro de una lista de diccionarios se encuentra una clave especifica.

    Recibe como parametro la lista y la clave (str)

    Retorna True si existe, False en caso contrario.
    '''
    retorno = False
    if validar_lista(lista_recibida) and validar_string(clave_recibida):
        copia_lista = lista_recibida[:]
        clave_recibida = clave_recibida.lower()
        for elemento in copia_lista:
            if clave_recibida in elemento:
                retorno = True
                break
    return retorno


        