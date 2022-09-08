from data_stark import lista_personajes

"""
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
"""
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



# ---- BLOQUE DE FUNCIONES ESPECIFICAS ---- #                
def mostrar_genero_masculino(lista):
    lista_masculinos = recorrer_y_mostrar(lista, "genero", "M", "nombre")
    mensaje = "Personajes Masculinos: \n"
    for masculino in lista_masculinos:
        mensaje += "{0}: {1} \n".format(masculino + 1, lista_masculinos[masculino])
    print(mensaje)

def mostrar_genero_femenino(lista):

    lista_femeninos = recorrer_y_mostrar(lista, "genero", "F", "nombre")
    mensaje = "Personajes Femeninos: \n"
    for femenino in lista_femeninos:
        mensaje += "{0}: {1} \n".format(femenino + 1, lista_femeninos[femenino])
    print(mensaje)

def mostrar_personaje_masculino_mas_alto(lista):
    masculino_mas_alto = maximos_minimos(lista,"altura","genero","M","Maximo")
    mensaje = "El personaje Masculino mas alto es: {0} | Siendo su altura: {1} cm".format(masculino_mas_alto["nombre"], masculino_mas_alto["altura"])
    print(mensaje)

def mostrar_personaje_femenino_mas_alto(lista):
    femenino_mas_alto = maximos_minimos(lista,"altura","genero","F","Maximo")
    mensaje = "El personaje Femenino mas alto es: {0} | Siendo su altura: {1} cm".format(femenino_mas_alto["nombre"],femenino_mas_alto["altura"])
    print(mensaje)

def mostrar_personaje_masculino_mas_bajo(lista):
    masculino_mas_bajo = maximos_minimos(lista,"altura","genero","M","Minimo")
    mensaje = "El personaje Masculino mas bajo es: {0} | Siendo su altura: {1} cm".format(masculino_mas_bajo["nombre"], masculino_mas_bajo["altura"])
    print(mensaje)

def mostrar_personaje_femenino_mas_bajo(lista):
    femenino_mas_bajo = maximos_minimos(lista,"altura","genero","F","Minimo")
    mensaje = "El personaje Femenino mas bajo es: {0} | Siendo su altura: {1} cm".format(femenino_mas_bajo["nombre"],femenino_mas_bajo["altura"])
    print(mensaje)

def mostrar_promedio_altura_masculino(lista):

    promedio_altura_masculino = calcular_promedios(lista, "altura", "genero", "M")
    mensaje = "El promedio de altura de los personajes Masculinos es: {0:.2f} Cm".format(promedio_altura_masculino)
    print(mensaje)

def mostrar_promedio_altura_femenino(lista):
    promedio_altura_femenino = calcular_promedios(lista, "altura", "genero", "F")
    mensaje = "El promedio de altura de los personajes Femeninos es: {0:.2f} Cm".format(promedio_altura_femenino)
    print(mensaje)

def mostrar_cantidad_por_color_ojos(lista):
    cantidad_color_ojos = calcular_cantidad_por_tipo(lista, "color_ojos")
    mensaje = "La cantidad de personajes por tipo de color de ojos es: \n"
    for e in cantidad_color_ojos:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e, cantidad_color_ojos[e])

    print(mensaje)

def mostrar_cantidad_por_color_pelo(lista):
    cantidad_color_pelo = calcular_cantidad_por_tipo(lista, "color_pelo")

    mensaje = "La cantidad de personajes por tipo de color de pelo es: \n"
    for e in cantidad_color_pelo:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e, cantidad_color_pelo[e])

    print(mensaje)

def mostrar_cantidad_por_inteligencia(lista):
    cantidad_inteligencia = calcular_cantidad_por_tipo(lista, "inteligencia")

    mensaje = "La cantidad de personajes por tipo de inteligencia es: \n"
    for e in cantidad_inteligencia:
        if e == '':
            mensaje += "No tiene"

        mensaje += "{0}: {1} \n".format(e, cantidad_inteligencia[e])

    print(mensaje)

def mostrar_lista_por_color_ojos(lista):
    lista_personajes_por_color_ojos = listar_por_tipo(lista, "color_ojos", "nombre")
    mensaje = "Personajes por color de ojos: \n"
    for e in lista_personajes_por_color_ojos:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e,lista_personajes_por_color_ojos[e])

    print(mensaje)

def mostrar_lista_por_color_pelo(lista):
    lista_personajes_por_color_pelo = listar_por_tipo(lista, "color_pelo", "nombre")
    mensaje = "Personajes por color de pelo: \n"
    for e in lista_personajes_por_color_pelo:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e,lista_personajes_por_color_pelo[e])

    print(mensaje)

def mostrar_lista_por_inteligencia(lista):
    lista_personajes_por_inteligencia = listar_por_tipo(lista, "inteligencia", "nombre")
    mensaje = "Personajes por inteligencia: \n"
    for e in lista_personajes_por_inteligencia:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e,lista_personajes_por_inteligencia[e])

    print(mensaje)

# ---- BLOQUE APP ---- #

def mostrar_menu(lista):
    while True:
        respuesta = input(
            "\n 1) Nombre de cada Superhéroe Masculino \n 2) Nombre de cada Superhéroe Femenino \n 3) Superheroe masculino mas alto \n 4) Superheroe femenino mas alto \n 5) Superheroe masculino mas bajo \n 6) Superheroe femenino mas bajo  \n 7) Promedio de altura de superheroes masculinos \n 8) Promedio de altura de superheroes femeninos  \n 9) Cuantos superheroes por tipo de color de ojos \n 10) Cuantos superheroes por tipo de color de pelo \n 11) Cuantos superheroes por tipo de inteligencia \n 12) Lista de superheroes por color de ojos  \n 13) Lista de superheroes por color de pelo  \n 14) Lista de superheroes por tipo de inteligencia \n 15) Salir \n Respuesta >"
        )
            
        if respuesta == "1":
            mostrar_genero_masculino(lista)
        elif respuesta == "2":
            mostrar_genero_femenino(lista)
        elif respuesta == "3":
            mostrar_personaje_masculino_mas_alto(lista)
        elif respuesta == "4":
            mostrar_personaje_femenino_mas_alto(lista)
        elif respuesta == "5":
            mostrar_personaje_masculino_mas_bajo(lista)
        elif respuesta == "6":
            mostrar_personaje_femenino_mas_bajo(lista)
        elif respuesta == "7":
            mostrar_promedio_altura_masculino(lista)
        elif respuesta == "8":
            mostrar_promedio_altura_femenino(lista)
        elif respuesta == "9":
            mostrar_cantidad_por_color_ojos(lista)
        elif respuesta == "10":
            mostrar_cantidad_por_color_pelo(lista)
        elif respuesta == "11":
            mostrar_cantidad_por_inteligencia(lista)
        elif respuesta == "12":
            mostrar_lista_por_color_ojos(lista)
        elif respuesta == "13":
            mostrar_lista_por_color_pelo(lista)
        elif respuesta == "14":
            mostrar_lista_por_inteligencia(lista)
        elif respuesta == "15":
            break

def avengers_app(lista):
    mostrar_menu(lista)


avengers_app(lista_personajes)






    
    







