'''
    TEMAS SEGUNDA PARTE.

        -Listas avanzado
        -Diccionarios avanzado
        -Comprensión listas
        -Manejo de excepciones / Validaciones
        -Bases de datos (SQLite)
        -Test unitarios
        -Decordaroes / Generadores
        -Intro a OOP
        -Web Server (Flask)
        -Web scraping
        -Argumentos en consola
        -Preparación para entrevistas
        -Pygame
        -HTML5 / Bootstrap
'''

'''
    LISTAS AVANZADO 6/10
        
        FUNCION LAMBDA.
            Anonimas, muy cortas (1 linea de codigo), procesa parametros y los retorna. 
            def sumar(a,b):     |   lambda a, b : a + b
                return a + b    |
            
            Puede asignarse a una variable
            sumar = lambda a, b : a + b ---> print(sumar(4,5)) # 9

        LISTAS.
            Almacena conjunto arbitrario de datos.
            <class 'list'>
            
            Pueden copiarse -> shallow o deep.

            Shallow -> lista_2 = lista.copy()

            Deep -> lista_2 = deepcopy(lista_1) --> import copy / from copy import deepcopy

            Metodo insert() --> lista.insert(1,"Jennifer") Inserta elemento en indice [1]

            Metodo extend() --> lista.extend(["a","b"]). Añade una lista a la lista inicial.

            Metodo pop() --> elemento_eliminado = lista.pop(1) Retorna el elemento eleminado

            Metodo remove() --> lista.remove("a") Elimina y no retorna.

            Metodo index() --> lista.index("a") Retorna la posicion del elemento.

            Metodo enumerate() --> for indice, elemento in enumerate(lista): -> # Indice y elemento          
            
            Metodo zip() --> for e1, e2, e3 in zip(lista1,lista2,lista3): -> Recorre listas en paralelo. 

            Metodo map() --> lista_resultado = list(map(str.upper,lista)) -> Se pasa por parametro una func, a cada elemento de una lista y retorna una nueva. Retorna un objeto map, por lo tanto debe castearse.

            Metodo filter() --> lista_resultado = list(filter(lambda elem : elem >= 18, lista)) -> Devuelve el elemento que retorne True la condicion pasada por parametro.

            Metodo reduce() --> suma = reduce(lambda x, y : x + y, lista) -> Se utiliza principalmente para calculos acumulativos, recibe dos parametros. Necesita el modulo functools. //from functools import reduce//.

            Metodo shuffle() --> shuffle(lista) -> Mezcla una lista. Necesita modulo

            Metodo sort() --> lista.sort() -> Sin parametros ascendente, para desc sort(reverse=True). Puede pasarse la clave sort(key=len). 
'''         

