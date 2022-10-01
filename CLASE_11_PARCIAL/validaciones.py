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

    Retorna True en ese caso o False si existe algun error.
    '''
    if type(path_recibido) == str and len(path_recibido) > 0:
        if re.search("\.json",path_recibido, re.I) == None:
            retorno = False
        else:
            retorno = True
    
    return retorno

# print(validar_json(".\CLASE_11_PARCIAL\data_stark.json"))