#---- FUNCIONES GENERALES ----#

def stark_normalizar_datos(lista:list, clave: str):
    '''
    La funcion se encarga de recorrer una lista y convertir al tipo de dato correcto el valor de la claves.
    (Solo si la key representa datos numericos)

    Recibe como parametro la lista a recorrer y la clave

    Imprime un mensaje "Datos Normalizados" si al menos un dato fue modificado. En caso contrario imprime "Error. Lista de heroes vacía"
    '''
    retorno = "Error. Lista de heroes vacía"

    if type(lista) == type([]) and len(lista) > 0 and type(clave) == type(""):
      for elemento in lista:
        elemento[clave] == float(elemento[clave])

      retorno = 'Datos normalizados'

      print(retorno)

def obtener_nombre(dic: dict) -> str:
  '''
  Funcion que recorre un diccionario, obtiene un nombre y lo formatea a un string.

  Recibe como parametro el diccionario a recorrer

  Retorna un string con el nombre formateado o "Error" en ese caso.
  '''

  retorno = "Error"

  if type(dic) == type({}):
      retorno = "Nombre: {0}".format(dic["nombre"])
  
  return retorno

def imprimir_dato(string: str):

  if type(string) == type(''):
    print(string)
  else:
    print("Error, no es un string")

def stark_imprimir_nombre_heroes(lista: list):
  '''
  Funcion que imprime en consola los nombres de una lista

  Recibe como parametro la lista

  Retorna la lista en consola.
  '''
  for elemento in lista:
    nombre = obtener_nombre(elemento)

    imprimir_dato(nombre)

def obtener_nombre_y_dato(dic: dict, clave: str) -> str:
  '''
  Funcion que recorre un diccionario y obtiene un nombre y el valor de una de sus clave.

  Recibe como parametro el diccionario y la clave

  Retorna un string con el nombre, su clave y el valor.
  '''

  retorno = "Error"

  if type(dic) == type({}) and type(clave) == type(""):
    dic[clave] = float(dic[clave])
    retorno = "Nombre: {0} | {1}: {2:.2f}".format(dic["nombre"], clave, dic[clave])

    return retorno

def stark_imprimir_nombres_alturas(lista: list):
  '''
  Funcion que recorre una lista e imprime nombre y altura de cada elemento.

  Recibe como parametro la lista a iterar.

  Imprime el mensaje en consola con los datos obtenidos. En caso contrario retorna "Error"
  '''
  retorno = "Error"
  if type(lista) == type([]) and len(lista) > 0:
    retorno = ""
    for elemento in lista:
      retorno += obtener_nombre_y_dato(elemento, "altura") + "\n"

    print(retorno)

def calcular_max(lista: list, clave: str)-> dict:
  '''
  Funcion que itera una lista y obtiene el maximo de una clave entre todos sus elementos.

  Recibe como parametro la lista a iterar y la clave a comparar.

  Retorna un diccionario con el elemento obtenido. O "Error" En ese caso.
  '''
  retorno = "Error"

  if type(lista) == type([]) and len(lista) > 0 and type(clave) == type(""):
    retorno = lista[0]
    retorno[clave] = float(retorno[clave])
    for elemento in lista:
      elemento[clave] = float(elemento[clave])
      if elemento[clave] > retorno[clave]:
        retorno = elemento

    return retorno

def calcular_min(lista: list, clave: str)-> dict:
  '''
  Funcion que itera una lista y obtiene el maximo de una clave entre todos sus elementos.

  Recibe como parametro la lista a iterar y la clave a comparar.

  Retorna un diccionario con el elemento obtenido. O "Error" En ese caso.
  '''
  retorno = "Error"

  if type(lista) == type([]) and len(lista) > 0 and type(clave) == type(""):
    retorno = lista[0]
    retorno[clave] = float(retorno[clave])
    for elemento in lista:
      elemento[clave] = float(elemento[clave])
      if elemento[clave] < retorno[clave]:
        retorno = elemento

    return retorno

def calcular_max_min_dato(lista: list, clave: str, tipo: str) -> dict:
  """
  Funcion que recorre una lista y obtiene un elemento maximo o minimo comparando una clave especifica.

  Recibe como parametro la lista a iterar, la clave a comparar y el tipo de operacion. "Maximo" o "Minimo".

  Retorna un diccionario con el elemento obtenido. O "Error" en ese caso
  """
  retorno = "Error"

  if type(lista) == type([]) and len(lista) > 0 and type(clave) == type("") and type(tipo) == type(""):
      if tipo == "Maximo":
        retorno = calcular_max(lista, clave)
      elif tipo == "Minimo":
        retorno = calcular_min(lista, clave)
    
  return retorno

def stark_calcular_imprimir_heroe(lista: list, clave: str, tipo: str):
  """
  Funcion que calcula e imprime un elemento maximo o minimo de una lista comparando una clave especifica.

  Recibe como parametro la lista a iterar, la clave a comparar y el tipo de operacion. "Maximo" o "Minimo".

  Imprime en consola el nombre y la altura del elemento seleccionado.
  """

  if type(lista) == type([]) and len(lista) > 0 and type(clave) == type("") and type(tipo) == type(""):
      if tipo == "Maximo":
        retorno = calcular_max(lista, clave)
      elif tipo == "Minimo":
        retorno = calcular_min(lista, clave)

      retorno = obtener_nombre_y_dato(retorno, clave)

      imprimir_dato(retorno)

def sumar_dato_heroe(lista: list, clave:str) -> int:
  '''
  Funcion encargada de sumar datos recorriendo una lista.

  Recibe como parametro la lista a iterar y la clave donde se encuentra el valor a sumar.

  Retorna un entero o un flotante, en el caso de error retorna "Error".
  '''

  retorno = "Error"

  if type(lista[0]) == type({}) and len(lista[0]) > 0:
    retorno = 0
    for elemento in lista:
      elemento[clave] = float(elemento[clave])
      retorno += elemento[clave]
  
  return retorno

def dividir(dividendo: float, divisor: float) -> float:
  '''
  Funcion encargada de realizar una division.

  Recibe como parametro el dividendo, y su divisor

  Retorna el resultado de la operacion.
  ''' 
  if type(dividendo) == type(1.1) and type(divisor) == type(1.1) and divisor != 0:
    retorno = dividendo / divisor
  else:
    retorno = 0

  return retorno

def calcular_promedio(lista: list, clave:str) -> int:
  '''
  Funcion que recorre una lista, obtiene valores numericos de una clave y obtiene un promedio total
  
  Recibe como parametro la lista a recorrer y la clave con el valor numerico.

  Retorna el promedio total.
  '''
  promedio = "Error"

  suma_total = sumar_dato_heroe(lista, clave)

  i = 0.0

  for elemento in lista:
    i += 1

  promedio = dividir(suma_total, i)
  
  return promedio

def stark_calcular_imprimir_promedio_altura(lista: list):
  '''
  Funcion encargada de imprimir un promedio de altura recorriendo una lista.

  Recibe como parametro la lista a iterar.

  Imprime en consola el promedio total. En el caso que la lista este vacia, retorna "Error, lista vacia".
  '''
  mensaje = "Error, lista vacia"

  if len(lista) > 0 and type(lista) == type([]):
    promedio = calcular_promedio(lista, "altura")
    mensaje = "La altura promedio es: {0:.2f}".format(promedio)

  imprimir_dato(mensaje)

def imprimir_menu():
  '''
  Funcion que imprime un menu
  '''

  menu = "\nMenu: \n1) Nombre de cada superheroe \n2) Nombre y Altura \n3) Superheroe mas alto \n4) Superheroe mas bajo \n5) Altura promedio de los superheroes \n6) Nombre de los superheroes(indicadores maximos y minimos) \n7) Superheroe mas pesado y menos pesado  \n8) Salir \n"

  imprimir_dato(menu)

def validar_entero(string: str)-> int:
  '''
  Funcion encargada de validar un entero. 

  Recibe un string como parametro, y lo castea a un entero.

  Si el tipo del string se paso a entero retorna True, en caso contrario retorna False.
  '''
  validacion = string.isdigit()

  if validacion == True:
    string = int(string)
    retorno = True
  else:
    retorno = False
  return retorno

def stark_menu_principal():
  respuesta = imprimir_menu()

  respuesta = input("Respuesta > ")

  retorno = validar_entero(respuesta)

  if retorno == True:
    retorno = int(respuesta)
  else:
    retorno = "Error. Ingrese un numero"

  return retorno
