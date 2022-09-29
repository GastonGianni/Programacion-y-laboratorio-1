lista = [3, 4, 5, 6, 2, 6, 5, 10, 9, 8, 6, 4, 8]


def encontrar_minimo(lista: list):
    minimo = lista[0]
    indice = 0

    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            indice = i

    return indice


# encontrar_minimo(lista)


def nahu_sort(lista_desordenada: list) -> list:
    copia_lista = lista_desordenada[:]
    lista_ordenada = []
    while len(copia_lista) > 0:
        index_min = encontrar_minimo(copia_lista)
        min_pop = copia_lista.pop(index_min)
        lista_ordenada.append(min_pop)

    return lista_ordenada


# print(nahu_sort(lista))

# --------------------#

# def sort_list(lista_desordenada:list) -> list:
#     copia_lista = lista_desordenada[:]
#     i = 0
#     aum = 0
#     print(copia_lista)

#     for i in range(len(copia_lista)):
#         for elemento in copia_lista:
#             if elemento < copia_lista[i]:
#                 aum += 1
#                 copia_lista[i + aum] = elemento
#                 i = 1


#     print(copia_lista)
# sort_list(lista)
