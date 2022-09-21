import re
from data_stark import lista_personajes

'''
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
   "inteligencia": "average"
 },
'''

def extraer_iniciales(string: str) -> str:
  '''
  Funcion encargada de extraer las iniciales de un nombre tipo string.

  Recibe como parametro el string.

  Retorna la inicial seguida de un punto(.).

  Si el string contiene "the" al inicio, se omite de las iniciales, si contiene un guion "-" se reemplaza por un espacio.

  Retorna 'N/A' en caso de recibir un string vacío.
  '''
  
  inicial = "N/A"

  if len(string) > 0:
    if string.count("the") > 0:
      string = string.replace("the ", "")

    if string.count("-") > 0:
      string = string.replace("-", " ")

    if string.count(" ") > 0:
      lista1 = string.split(" ")
      inicial = ""
      for elemento in lista1:
        inicial += "{0}.".format(elemento[0:1].upper())
    else:
      inicial = "{0}.".format(string[0:1].upper())
  

  return inicial
    
# a = extraer_iniciales("")

# print(a)

#-------------------#

def definir_iniciales_nombre(dic: dict) -> bool:
  '''
  Funcion encargada de agregar una nueva clave llamada "iniciales" al diccionario (dic)

  Recibe como parametro el diccionario (Debe tener una clave "nombre").

  Retorna True si funciona o False en caso de haber algun error.
  '''
  
  retorno = False

  if type(dic) == type({}): 
    for clave in dic:
      if clave.count("nombre") > 0:
        inicial = extraer_iniciales(dic["nombre"])
        dic["iniciales"] = inicial
        retorno = True
        break

  return retorno

# a = definir_iniciales_nombre(lista_personajes)
# print(a)

#-------------------#

def agregar_iniciales_nombre(lista: list) -> bool:
  '''
  Funcion que itera una lista y por cada diccionario con la clave "nombre" genera un nuevo diccionario con sus iniciales.

  Recibe como parametro la lista a iterar.

  Retorna True si finaliza o False en caso de haber ocurrido un error.
  '''

  retorno = False

  if type(lista) == list and len(lista) > 0:
    for elemento in lista:
      retorno = definir_iniciales_nombre(elemento)
      if retorno == True: continue
      else:
        print('El origen de los datos no contiene el formato correcto')
        break
    
  return retorno

# lista_a = ["a","b","c"]
# a = agregar_iniciales_nombre(lista_a)
# print(a)

#-------------------#

def stark_imprimir_nombres_con_iniciales(lista: list):
  '''
  Funcion que recorre una lista de diccionarios con clave "nombre" e imprime en pantalla los nombres con sus iniciales.

  Recibe como parametro la lista a iterar.
  '''
  agregar_iniciales_nombre(lista)
  mensaje = ""
  for elemento in lista:
    mensaje += "* {} ({}) \n".format(elemento["nombre"], elemento["iniciales"])
  

  print(mensaje)

# stark_imprimir_nombres_con_iniciales(lista_personajes)

#-------------------#

def generar_codigo_heroe(id: int, genero: str)-> str:
  '''
  La funcion recibe como parametro un id (int) y un genero (str) 

  Retorna un string formateado (GENERO-000...000ID)
  '''

  retorno = 'N/A'

  if type(id) == int and type(genero) == str:
    genero = genero.upper()
    nuevo_id = str(id)
    if genero == "NB":
      nuevo_id = nuevo_id.zfill(7)
    else:
      nuevo_id = nuevo_id.zfill(8)
    retorno = genero + " " + nuevo_id
    lista_1 = retorno.split(" ")
    separador = "-"
    retorno = separador.join(lista_1)
    
  return (retorno)

# a = generar_codigo_heroe(1,"nb")
# print(a)

#-------------------#

def agregar_codigo_heroe(dic: dict, id: int)-> bool:
  '''
  La funcion agrega una nueva clave a un diccionario llamada "codigo_heroe" con un valor.

  Recibe como parametro el diccionario y el valor del codigo_heroe

  Retorna True si funciona, False si ocurre un error.
  '''
  retorno = False

  if len(dic) > 0:
    dic["codigo_heroe"] = generar_codigo_heroe(id, dic["genero"])
    if len(dic["codigo_heroe"]) == 10:
      retorno = True
  return retorno

# a= agregar_codigo_heroe(lista_personajes[0], 20)
# print(a)

#-------------------#

def stark_generar_codigos_heroes(lista: list):
  '''
  La función itera la lista de personajes y agrega el código a cada uno.

  El codigo del personaje surge de la posicion del mismo, comenzando en 1.

  Imprime en pantalla la cantidad de codigos asignados y una lista con cada uno.
  '''
  mensaje = "El orgien de los datos no contiene el formato correcto"

  if len(lista) > 0:
    contador_codigos = 0
    for elemento in lista:
      if type(elemento) == dict:
        agregar_codigo_heroe(elemento, lista.index(elemento) + 1)
        contador_codigos += 1
    
    mensaje = "Se asignaron {0} códigos. \n".format(contador_codigos)
    mensaje += "* El codigo del primer héroe es: {0}\n* El codigo del último héroe es: {1}".format(lista[0]["codigo_heroe"],lista[contador_codigos - 1]["codigo_heroe"])
  print(mensaje)
    
# stark_generar_codigos_heroes(lista_personajes)

#-------------------#

def sanitizar_entero(numero_str: str)-> int:
  '''
  Funcion que cambia el tipo de un string a entero en el caso que sea posible.

  Recibe el numero en string a convertir.

  Si contiene carácteres no numéricos retorna (-1), Si el número es negativo retorna (-2).
  Si ocurren otros errores que no permiten convertirlo a entero retorna (-3)

  En el caso de funcionar correctamente retorna el entero.
  '''
  retorno = -3
  if type(numero_str) == int:
    return retorno

  numero = numero_str
  if numero_str.isnumeric() == True:
    numero = numero_str.strip(" ")
    numero = int(numero)
    if numero >= 0:
      retorno = numero
    else:
      retorno = -2 
  elif numero_str.isalpha() == True:
    retorno = -1
    return retorno


  return retorno

# a = sanitizar_entero("-240")
# print(a)

#-------------------#

def sanitizar_flotante(numero_str: str)-> float:
  '''  
  Funcion que cambia el tipo de un string a flotante en el caso que sea posible.

  Recibe el numero en string a convertir.

  Si contiene carácteres no numéricos retorna (-1), Si el número es negativo retorna (-2).
  Si ocurren otros errores que no permiten convertirlo a entero retorna (-3)

  En el caso de funcionar correctamente retorna el flotante.
  '''
  retorno = -3
  if type(numero_str) == int or type(numero_str) == float:
    return retorno

  numero = numero_str
  if numero.isnumeric() == False:
    if numero.count(".") > 0:
      numero = numero_str.strip(" ")
      numero = float(numero)
      if numero >= 0:
        retorno = numero
      else:
        retorno = -2
    elif numero.isalpha() == True:
      retorno = -1
  else:
    retorno = -3
      

  return retorno

# a = sanitizar_flotante("asdsad")
# print(a)

#-------------------#

def sanitizar_string(valor_str: str, valor_por_defecto = "-")-> str:
  '''
  Funcion que analiza un string y determina si solo contiene texto.

  Recibe como parametro el string y un valor por defecto.

  En el caso de contener numeros retorna "N/A". Si el string contiene solo texto lo retorna en minusculas.

  Si el valor por defecto contiene el string y el valor se pasa vacío. Retorna el valor por defecto en minusculas.
  '''
  if type(valor_str) == str:
    if len(valor_str) > 0:
      string = valor_str
    else:
      string = valor_por_defecto

    if len(string) > 0:
    
      string = string.strip()

      if string.count("/") > 0:
        string = string.replace("/", " ")
      
      lista_str = string.split(" ")
      i = 0
      string = ""
      for e in lista_str:
        if lista_str[i].isalpha() == True:
          string += e + " "
          i += 1
        else:
          retorno = "N/A"
          return retorno
      
      retorno = string.lower()
  
  else:
    retorno = "N/A"
  
  return retorno
 
# sanitizar_string("", "hola/HOLA")

#-------------------#

def sanitizar_dato(heroe: dict, clave: str, tipo: str)->bool:
  '''
  Funcion que sanitiza un dato str a (int,float,str) obtenido de la clave de un diccionario.

  Recibe como parametro el diccionario, la clave y el tipo:
    Para sanitizar str (tipo = "String")
    Para sanitizar int (tipo = "Entero")
    Para sanitizar flotante (tipo = "Flotante")
  
  Retorna True si sanitizo correctamente, False si hubo errores.
  '''
  retorno = False
  tipo = tipo.lower()

  for elemento in heroe:
    if elemento.count(clave) > 0:
      existe_clave = 1
      break
    else:
      existe_clave = 0
  
  if existe_clave == 0:
    print("La clave especificada no existe en el heroe")
    return retorno

  if tipo == "string":
    sanitizar_string(heroe[clave])
    if sanitizar_string(heroe[clave]) == 'N/A':
      retorno = False
    else:
      retorno = True
  elif tipo == "entero":
    sanitizar_entero(heroe[clave])
    if sanitizar_entero(heroe[clave]) >= 0:
      retorno = True
    else:
      retorno = False
  elif tipo == "flotante":
    sanitizar_flotante(heroe[clave])
    if sanitizar_flotante(heroe[clave]) >= 0:
      retorno = True
    else:
      retorno = False
      
  else:
    print("Tipo de dato no reconocido")

  return retorno
    

# a = sanitizar_dato(lista_personajes[0], "nombre", "string")
# print(a)

#-------------------#

# def stark_normalizar_datos(lista_heroes: list):
#   '''
#   Funcion encargada de sanitizar los datos de una lista de diccionarios con las siguientes claves:

#   "altura", "peso", "color_ojos", "color_pelo", "fuerza" e "inteligencia".

#   Muestra "Datos normalizados" finalizado el proceso o "Lista de heroes vacías" si no hay elementos.
#   '''
  
    
  
    
    
    


#   print("Datos normalizados")

# stark_normalizar_datos(lista_personajes)

#-------------------#

def generar_indice_nombres(lista_heroes: list) -> list:

  retorno = 'El origen de los datos no contiene el formato correcto'

  if len(lista_heroes) > 0:
    nombre = ""
    for elemento in lista_heroes:
      if type(elemento) == dict and "nombre" in elemento:
        nombre += elemento["nombre"] + " "
  
    retorno = re.findall('[a-zA-Z]+', nombre)

  return retorno

# generar_indice_nombres(lista_personajes)

#-------------------#

def stark_imprimir_indice_nombre(lista_heroes: list):
  lista_nombres = generar_indice_nombres(lista_heroes)
  separador = "-"

  nombres_separados = separador.join(lista_nombres)
  print(nombres_separados)

# stark_imprimir_indice_nombre(lista_personajes)

#-------------------#

def convertir_cm_a_mtrs(valor_cm: float)-> float:
  '''
  Funcion que transforma a la unidad metro un flotante que representa una medida en centímetros.

  Recibe como parametro el numero de tipo flotante.

  Retorna el numero convertido si funciona o -1 si hubo algun error.
  '''
  valor_mtrs = -1

  if type(valor_cm) == float and valor_cm >= 0:
    valor_mtrs = "{0:.2f}".format(valor_cm / 100)
    valor_mtrs = float(valor_mtrs)
    


  return valor_mtrs

# print(convertir_cm_a_mtrs(178.28))

#-------------------#

def generar_separador(patron:str,largo:int,imprimir = True):
  '''
  '''
  retorno = 'N/A'

  if len(patron) > 0 and len(patron) < 3 and type(largo) == int and largo > 0 and largo < 236:
    patron = str(patron)
    retorno = ""
    for i in range(largo):
      retorno += patron

    if imprimir == True:
      print(retorno)
  
  return retorno

# generar_separador("/", 4, False)

#-------------------#

def generar_encabezado(titulo: str):


