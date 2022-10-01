from funciones import *

'''
[
    {
        'nombre': 'Howard the Duck', 
        'identidad': 'Howard (Last name unrevealed)', 
        'altura': 79.35, 
        'peso': 18.45, 
        'fuerza': 2, 
        'inteligencia': ''
    }, 
    {
        'nombre': 'Rocket Raccoon', 
        'identidad': 'Rocket Raccoon', 
        'altura': 122.77, 
        'peso': 25.73, 
        'fuerza': 5, 
        'inteligencia': 'average'
    },
'''

#URL data_stark.json
url_archivo = r".\CLASE_10\data_stark.json"

lista_heroes = importar_json(url_archivo)

#----- MENU -----#

def imprimir_menu():
    print("1)Listar héroes.\n2)Ordenar y listar heroes por su altura.\n3)Ordenar y listar héroes por su fuerza.\n4)Calcular promedio de una clave y filtrar heroe.\n5)Buscar héroes por tipo de inteligencia.\n6)Crear archivo .CSV con la ultima lista seleccionada.\n7)Salir")
 
def app(lista_recibida:list):
    #lista_seleccionada = []
    while True:
        imprimir_menu()
        respuesta = input("\nIngrese respuesta > ")
        respuesta = validar_entero(respuesta)
        if respuesta == False:
            continue
        else:
            respuesta = int(respuesta)
            if respuesta == 1:
                valor_maximo = input("Escriba valor maximo > ")
                lista_seleccionada = listar_heroes(lista_recibida, valor_maximo)
            elif respuesta == 2:
                metodo = input("Escriba metodo ('Asc' o 'Desc') > ")
                lista_seleccionada = ordenar_heroes_por_altura(lista_recibida, metodo)
            elif respuesta == 3:
                metodo = input("Escriba metodo ('Asc' o 'Desc') > ")
                lista_seleccionada = ordenar_heroes_por_fuerza(lista_recibida, metodo)
            elif respuesta == 4:
                clave = input("Escriba clave ('Fuerza', 'Altura', 'Peso') > ")
                condicion = input("Escriba condicion ('Mayor' o 'Menor')")
                lista_seleccionada = calcular_promedio_y_filtrar(lista_recibida, clave, condicion)
            elif respuesta == 5:
                tipo_inteligencia = input("Escriba tipo de inteligencia (Good, Average, High) > ")
                lista_seleccionada = buscar_heroes_por_inteligencia(lista_recibida, tipo_inteligencia)
            elif respuesta == 6:
                exportar_csv(lista_seleccionada)
            elif respuesta == 7:
                break
            else:
                print("\nOpción fuera de rango (1-7)\n")
            
app(lista_heroes)

            