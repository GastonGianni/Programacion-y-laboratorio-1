from data_pokemon import pokemones
'''
{
    "id": 1,
    "nombre": "bulbasaur",
    "tipo": ["planta"],
    "evoluciones": ["ivysaur", "venusaur"],
    "poder": 4,
    "fortaleza":["agua"],
    "debilidad":["fuego"]
},
'''

#----------------#

def obtener_nombre_pokemon(dic: dict):
    retorno = dic["nombre"]
    return retorno

#----------------#

def pokedex_imprimir_pokemon(lista:list):
    for elemento in lista:
        retorno = obtener_nombre_pokemon(elemento)
        print(retorno)

#----------------#

def tiene_id_par(dic: dict):
    if dic["id"] % 2 == 0:
        retorno = True
    else:
        retorno = False

    return retorno

#----------------#

def obtener_id_pokemon(dic: dict):
    retorno = dic["id"]
    retorno = str(retorno)
    return retorno

#----------------#

def pokedex_imprimir_pokemones_id_par(lista: list):
    pokemons_id_par = {}
    mensaje = "\nPokemons con id par: \n \n"

    for elemento in lista:
        tiene_par = tiene_id_par(elemento)
        if tiene_par == True:
            pokemons_id_par[obtener_nombre_pokemon(elemento)] = obtener_id_pokemon(elemento)
            mensaje += "Nombre: {0} || Id: {1} \n".format(obtener_nombre_pokemon(elemento).capitalize(),obtener_id_pokemon(elemento))
    print(mensaje)
        
#----------------#

def id_multiplo_25(dic: dict):
    if dic["id"] % 25 == 0:
        retorno = True
    else:
        retorno = False

    return retorno

#----------------#

def pokedex_imprimir_pokemon_id_mul_25(lista: list):
    pokemons_id_multiplo_25 = {}
    mensaje = "\nPokemons con id multiplo de 25: \n \n"

    for elemento in lista:
        mult_25 = id_multiplo_25(elemento)
        if mult_25 == True:
            pokemons_id_multiplo_25[obtener_nombre_pokemon(elemento)] = obtener_id_pokemon(elemento)
            mensaje += "Nombre: {0} || Id: {1} \n".format(obtener_nombre_pokemon(elemento).capitalize(),obtener_id_pokemon(elemento))
    print(mensaje)

#----------------#

def nombre_format_pokemon(dic: dict):
    id_pokemon = obtener_id_pokemon(dic)
    nombre_pokemon = obtener_nombre_pokemon(dic)
    retorno = "#{0} - {1}".format(id_pokemon, nombre_pokemon)
    return retorno

#----------------#

def pokedex_imprimir_nombres_poke_fmt(lista: list):

    for elemento in lista:
        retorno = nombre_format_pokemon(elemento)
        print(retorno)

#----------------#

def calcular_max_dato(lista: list, operacion:str, key: str):
    if operacion == "Maximo":
        elemento_maximo = lista[0][key]
        for elemento in lista:
            if elemento[key] > elemento_maximo:
                elemento_maximo = elemento[key]
    
    return elemento_maximo

#----------------#

def obtener_lista_pokemones(lista: list, key: str, valor: int):
    lista_pok = []
    for elemento in lista:
        if elemento[key] == valor:
            lista_pok.append(elemento["nombre"].capitalize())
    
    if len(lista_pok) == 0:
        lista_pok = "No se encontraron pokemons con ese valor"
                    
    return lista_pok

#----------------#

def string_max_dato(lista: list, operacion: str, key: str):
    if operacion == "Maximo":
        valor_max = calcular_max_dato(lista, operacion, key)
        lista_pokemons = obtener_lista_pokemones(lista, key, valor_max)
        pokemons = ""
        for pokemon in lista_pokemons:
            pokemons += pokemon + " - "
        retorno = "{0} maximo: {1} | Pokemons: {2}".format(key.capitalize(), valor_max, pokemons)
        return retorno

#----------------#

def imprimir_pokemones_fuertes(string: str):
    print(string)

#----------------#

def pokedex_imprimir_pokemones_fuertes(lista):
    lista_mas_fuertes = string_max_dato(lista, "Maximo", "poder")
    imprimir_pokemones_fuertes(lista_mas_fuertes)

#----------------#

def calcular_min_dato(lista: list, operacion: str, key: str):
    if operacion == "Minimo":
        elemento_minimo = lista[0][key]
    for elemento in lista:
        if elemento[key] < elemento_minimo:
            elemento_minimo = elemento[key]
    
    return elemento_minimo

#----------------#

def string_min_dato(lista: list, operacion: str, key: str):
    if operacion == "Minimo":
        valor_min = calcular_min_dato(lista, operacion, key)
        lista_pokemons = obtener_lista_pokemones(lista, key, valor_min)
        pokemons = ""
        for pokemon in lista_pokemons:
            pokemons += pokemon + " - "
        retorno = "{0} minimo: {1} | Pokemons: {2}".format(key.capitalize(), valor_min, pokemons)
        return retorno
