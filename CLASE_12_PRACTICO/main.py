'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("./CLASE_12_PRACTICO\data.json")
    # print(lista_personajes)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            funciones.listar_personajes_ordenados_altura(lista_personajes)
        elif(respuesta=="2"):
            funciones.mostrar_personaje_mas_alto_genero(lista_personajes)
        elif(respuesta=="3"):
            lista_personajes = funciones.sort_list(lista_personajes, "mass")
        elif(respuesta=="4"):
            buscador = input("Buscar personaje > ")
            funciones.buscador_personaje(lista_personajes, buscador)
        elif(respuesta=="5"):
            funciones.exportar_csv(lista_personajes)
        elif(respuesta=="6"):
            break


starwars_app()

