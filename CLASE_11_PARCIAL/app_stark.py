'''
SIMULACRO PARCIAL.

    1- Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
    2- Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente ("asc") o descendente ("desc")
    3- Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente ("asc") o descendente ("desc")
    4- Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: "menor" o "mayor") se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.
    5- Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)
    6- Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

'''
import funciones
path_data_stark = ".\CLASE_11_PARCIAL\data_stark.json"

#---APP STARK---#

def app_stark():
    lista_heroes = funciones.importar_json(path_data_stark)
    funciones.ingresar_respuesta(lista_heroes)

app_stark()


