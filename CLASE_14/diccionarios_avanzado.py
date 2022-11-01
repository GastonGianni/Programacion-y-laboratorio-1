'''
    DICCIONARIOS AVANZADO.

        - Diccionario anidado = Cuando una de las claves contiene un diccionario como valor.
        - Copia de diccionarios = shallow/deep.
        - Metodo get() -->
            * Permite consultar el valor de una clave, si no se encuentra se pasa el valor por segundo parametro.
            * diccionario.get('name', 'NO NAME') -> retorna 'NO NAME' si no existe. (Parametro opcional)
        - Metodo keys() -->
            * Devuelve una lista con todas las claves de un diccionario.
            * list(diccionario.keys())
        - Metodo values() -->
            * Devuelve una lista con todos los valores de las claves.
            * list(diccionario.values())
        - Metodo items() -->
            * Devuelve una lista de tuplas con claves y valores.
            * list(diccionario.items())
        - Metodo pop() -->
            * Busca y elimina la key que se pasa como parametro, devuelve su valor asociado.
            * diccionario.pop('edad','none') -> retorna 'none' si no existe. (Parametro opcional)
        - Metodo update() -->
            * Se llama sobre un diccionario y tiene como entrada otro diccionario. Los values son actualizados si no existe la key.
            * Prevalece la clave del update si ya existía en el dic original.
            * diccionario.update({'year':'1973'})
'''