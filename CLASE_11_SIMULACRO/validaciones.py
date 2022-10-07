import re


#---VALIDACIONES---#

def validar_json(path_file)->bool:
    '''
    Funcion que valida si existe la extension .json en una url.

    Recibe el path del archivo a validar.

    Retorna True si el archivo es .json o False en caso contrario.
    '''
    retorno = False
    validacion = re.search('\.json$',path_file)
    if validacion:
        retorno = True
    return retorno

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

def validar_valor_ingresado(lista_recibida:list, valor:str)->int:
    '''
    Funcion que valida si el valor ingresado supera el tamaño de una lista.

    Recibe como parametro la lista y el valor (String con caracteres numéricos)

    En el caso que el valor ingresado sea menor o igual al tamaño de la lista retorna el valor transformado a entero.

    En caso contrario retorna 0.
    '''
    retorno = 0
    if validar_entero(valor):
        valor = int(valor)
        if valor <= len(lista_recibida):
            retorno = valor

    return retorno
            
