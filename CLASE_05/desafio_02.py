from data_stark import lista_personajes
from stark_biblioteca import stark_normalizar_datos
from stark_biblioteca import obtener_nombre
from stark_biblioteca import imprimir_dato
from stark_biblioteca import stark_imprimir_nombre_heroes
from stark_biblioteca import obtener_nombre_y_dato
from stark_biblioteca import stark_imprimir_nombres_alturas
from stark_biblioteca import calcular_max
from stark_biblioteca import calcular_min
from stark_biblioteca import calcular_max_min_dato
from stark_biblioteca import stark_calcular_imprimir_heroe
from stark_biblioteca import sumar_dato_heroe
from stark_biblioteca import dividir
from stark_biblioteca import calcular_promedio
from stark_biblioteca import stark_calcular_imprimir_promedio_altura
from stark_biblioteca import imprimir_menu
from stark_biblioteca import validar_entero
from stark_biblioteca import stark_menu_principal

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
    "inteligencia": ""
  },
'''

#---- 7) Crear la funcion stark_marvel_app

def stark_marvel_app(lista: list):

  while True:
    respuesta = stark_menu_principal()
    if respuesta == 1:
      stark_imprimir_nombre_heroes(lista)
    elif respuesta == 2:
      stark_imprimir_nombres_alturas(lista)
    elif respuesta == 3:
      stark_calcular_imprimir_heroe(lista, "altura", "Maximo")
    elif respuesta == 4:
      stark_calcular_imprimir_heroe(lista, "altura", "Minimo")
    elif respuesta == 5:
      stark_calcular_imprimir_promedio_altura(lista)
    elif respuesta == 6:
      stark_calcular_imprimir_heroe(lista, "altura", "Maximo")
      stark_calcular_imprimir_heroe(lista, "altura", "Minimo")
    elif respuesta == 7:
      stark_calcular_imprimir_heroe(lista, "peso", "Minimo")
      stark_calcular_imprimir_heroe(lista, "peso", "Maximo")
    elif respuesta == 8:
      break
    elif respuesta > 8 or respuesta < 1:
      imprimir_dato("Error. Opcion incorrecta\n")

stark_marvel_app(lista_personajes)