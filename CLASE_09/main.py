''''
ALGORITMOS DE ORDENAMIENTO
'''

lista = [9,8,10,7,6,4,5,3,2,1]

'''
QUICK SORT.
    - Se selecciona un "Pivote" Al azar de la lista.
    - Se generan dos listas vacias (izquierda y derecha)
    - Se appendean los elementos menores al pivote en la lista izquierda y los mayores en la derecha (ordenamiento ascendente)
    - De cada sublista creada se genera un nuevo Pivote y se realiza el mismo procedimiento. (RECURSIVIDAD)
    - Cuando cada sublista tenga su tamaño en 1 elemento
'''

def qsort(lista_a_ordenar:list)-> list:
    copia_lista = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        pivot = copia_lista[0]
        for elemento in copia_lista[1:]:
            if(elemento > pivot):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

    lista_izq = qsort(lista_izq)
    lista_der = qsort(lista_der)
    lista_izq.append(pivot)

    return lista_izq + lista_der
lista_ordenada = qsort(lista)
print(lista_ordenada)