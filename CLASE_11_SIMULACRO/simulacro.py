import funciones
path_file = './CLASE_11_SIMULACRO\pokedex.json'

#---APP---#

def app_pokedex():
    lista_pokemones = funciones.importar_json(path_file)["pokemones"]
    # print(type(lista_pokemones))
    # print(lista_pokemones)
    funciones.ingresar_respuesta(lista_pokemones)

app_pokedex()

