# ---- BLOQUE DE FUNCIONES ESPECIFICAS ---- #                
def mostrar_genero_masculino(lista):
    lista_masculinos = recorrer_y_mostrar(lista, "genero", "M", "nombre")
    mensaje = "Personajes Masculinos: \n"
    for masculino in lista_masculinos:
        mensaje += "{0}: {1} \n".format(masculino + 1, lista_masculinos[masculino])
    print(mensaje)

def mostrar_genero_femenino(lista):

    lista_femeninos = recorrer_y_mostrar(lista, "genero", "F", "nombre")
    mensaje = "Personajes Femeninos: \n"
    for femenino in lista_femeninos:
        mensaje += "{0}: {1} \n".format(femenino + 1, lista_femeninos[femenino])
    print(mensaje)

def mostrar_personaje_masculino_mas_alto(lista):
    masculino_mas_alto = maximos_minimos(lista,"altura","genero","M","Maximo")
    mensaje = "El personaje Masculino mas alto es: {0} | Siendo su altura: {1} cm".format(masculino_mas_alto["nombre"], masculino_mas_alto["altura"])
    print(mensaje)

def mostrar_personaje_femenino_mas_alto(lista):
    femenino_mas_alto = maximos_minimos(lista,"altura","genero","F","Maximo")
    mensaje = "El personaje Femenino mas alto es: {0} | Siendo su altura: {1} cm".format(femenino_mas_alto["nombre"],femenino_mas_alto["altura"])
    print(mensaje)

def mostrar_personaje_masculino_mas_bajo(lista):
    masculino_mas_bajo = maximos_minimos(lista,"altura","genero","M","Minimo")
    mensaje = "El personaje Masculino mas bajo es: {0} | Siendo su altura: {1} cm".format(masculino_mas_bajo["nombre"], masculino_mas_bajo["altura"])
    print(mensaje)

def mostrar_personaje_femenino_mas_bajo(lista):
    femenino_mas_bajo = maximos_minimos(lista,"altura","genero","F","Minimo")
    mensaje = "El personaje Femenino mas bajo es: {0} | Siendo su altura: {1} cm".format(femenino_mas_bajo["nombre"],femenino_mas_bajo["altura"])
    print(mensaje)

def mostrar_promedio_altura_masculino(lista):

    promedio_altura_masculino = calcular_promedios(lista, "altura", "genero", "M")
    mensaje = "El promedio de altura de los personajes Masculinos es: {0:.2f} Cm".format(promedio_altura_masculino)
    print(mensaje)

def mostrar_promedio_altura_femenino(lista):
    promedio_altura_femenino = calcular_promedios(lista, "altura", "genero", "F")
    mensaje = "El promedio de altura de los personajes Femeninos es: {0:.2f} Cm".format(promedio_altura_femenino)
    print(mensaje)

def mostrar_cantidad_por_color_ojos(lista):
    cantidad_color_ojos = calcular_cantidad_por_tipo(lista, "color_ojos")
    mensaje = "La cantidad de personajes por tipo de color de ojos es: \n"
    for e in cantidad_color_ojos:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e, cantidad_color_ojos[e])

    print(mensaje)

def mostrar_cantidad_por_color_pelo(lista):
    cantidad_color_pelo = calcular_cantidad_por_tipo(lista, "color_pelo")

    mensaje = "La cantidad de personajes por tipo de color de pelo es: \n"
    for e in cantidad_color_pelo:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e, cantidad_color_pelo[e])

    print(mensaje)

def mostrar_cantidad_por_inteligencia(lista):
    cantidad_inteligencia = calcular_cantidad_por_tipo(lista, "inteligencia")

    mensaje = "La cantidad de personajes por tipo de inteligencia es: \n"
    for e in cantidad_inteligencia:
        if e == '':
            mensaje += "No tiene"

        mensaje += "{0}: {1} \n".format(e, cantidad_inteligencia[e])

    print(mensaje)

def mostrar_lista_por_color_ojos(lista):
    lista_personajes_por_color_ojos = listar_por_tipo(lista, "color_ojos", "nombre")
    mensaje = "Personajes por color de ojos: \n"
    for e in lista_personajes_por_color_ojos:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e,lista_personajes_por_color_ojos[e])

    print(mensaje)

def mostrar_lista_por_color_pelo(lista):
    lista_personajes_por_color_pelo = listar_por_tipo(lista, "color_pelo", "nombre")
    mensaje = "Personajes por color de pelo: \n"
    for e in lista_personajes_por_color_pelo:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e,lista_personajes_por_color_pelo[e])

    print(mensaje)

def mostrar_lista_por_inteligencia(lista):
    lista_personajes_por_inteligencia = listar_por_tipo(lista, "inteligencia", "nombre")
    mensaje = "Personajes por inteligencia: \n"
    for e in lista_personajes_por_inteligencia:
        if e == '':
            mensaje += "No tiene"
        mensaje += "{0}: {1} \n".format(e,lista_personajes_por_inteligencia[e])

    print(mensaje)
