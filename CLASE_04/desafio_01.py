from data_stark import lista_personajes

"""
  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
"""

# print(lista_personajes)


# ---------- A) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M ---------#

def Mostrar_Genero_M():


    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            mensaje = ("Nombre: {0} | Genero: {1}".format(personaje["nombre"], personaje["genero"]))
            print(mensaje)


# Mostrar_Genero_M()


# ---------- B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F --------- #

def Mostrar_Genero_F():
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            mensaje = ("Nombre: {0} | Genero: {1}".format(personaje["nombre"], personaje["genero"]))
            print(mensaje)


# Mostrar_Genero_F()


# ---------- C) Recorrer la lista y determinar cuál es el superhéroe más alto de género M  ---------#

def Calcular_Masculino_Mas_Alto():

    flag = True

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])

        if flag == True and personaje["genero"] == "M":
            masculino_mas_alto = personaje
            flag = False

        if personaje["altura"] > masculino_mas_alto["altura"] and personaje["genero"] == "M":
            masculino_mas_alto = personaje

    mensaje = ("El personaje de genero Masculino mas alto es: {0} | Y su altura es de {1}".format(masculino_mas_alto["nombre"], masculino_mas_alto["altura"]))

    return print(mensaje)

# Calcular_Masculino_Mas_Alto()


# ---------- D) Recorrer la lista y determinar cuál es el superhéroe más alto de género F  ---------#

def Calcular_Femenino_Mas_Alto():

    flag = True

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])

        if flag == True and personaje["genero"] == "F":
            femenino_mas_alto = personaje
            flag = False

        if (flag == False and personaje["altura"] > femenino_mas_alto["altura"] and personaje["genero"] == "F"):
            femenino_mas_alto = personaje

    
    mensaje = ("El personaje de genero Femenino mas alto es: {0} | Y su altura es de {1}".format(femenino_mas_alto["nombre"], femenino_mas_alto["altura"]))

    return print(mensaje)

# Calcular_Femenino_Mas_Alto()


# ---------- E) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M  ---------#

def Calcular_Masculino_Mas_Bajo():

    flag = True

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])

        if flag == True and personaje["genero"] == "M":
            masculino_mas_bajo = personaje
            flag = False

        if flag == False and personaje["altura"] < masculino_mas_bajo["altura"] and personaje["genero"] == "M":
            masculino_mas_bajo = personaje

    mensaje = ("El personaje de genero Masculino mas bajo es: {0} | Y su altura es de {1}".format(masculino_mas_bajo["nombre"], masculino_mas_bajo["altura"]))

    return print(mensaje)

# Calcular_Masculino_Mas_Bajo()


# ---------- F) Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F  ---------#

def Calcular_Femenino_Mas_Bajo():

    flag = True

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])

        if flag == True and personaje["genero"] == "F":
            femenino_mas_bajo = personaje
            flag = False

        if flag == False and personaje["altura"] < femenino_mas_bajo["altura"] and personaje["genero"] == "F":
            femenino_mas_bajo = personaje

    mensaje = ("El personaje de genero Femenino mas bajo es: {0} | Y su altura es de {1}".format(femenino_mas_bajo["nombre"], femenino_mas_bajo["altura"]))

    return print(mensaje)

# Calcular_Femenino_Mas_Bajo()


# ---------- G) Recorrer la lista y determinar la altura promedio de los  superhéroes de género M  ---------#

def Calcular_Altura_Promedio_De_Masculinos():

    acumuladorAlturaMasculinos = 0
    contadorMasculinos = 0

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["genero"] == 'M':
            acumuladorAlturaMasculinos += personaje["altura"]
            contadorMasculinos += 1

    promedioAlturaMasculinos = acumuladorAlturaMasculinos / contadorMasculinos

    mensaje = ("La altura promedio de los personajes de genero Masculino es: {0:.2f}".format(promedioAlturaMasculinos))

    return print(mensaje)
    
# Calcular_Altura_Promedio_De_Masculinos()


# ---------- H) Recorrer la lista y determinar la altura promedio de los  superhéroes de género F ---------#

def Calcular_Altura_Promedio_De_Femeninos():



    acumuladorAlturaFemeninos = 0
    contadorFemeninos = 0

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if personaje["genero"] == 'F':
            acumuladorAlturaFemeninos += personaje["altura"]
            contadorFemeninos += 1

    promedioAlturaFemeninos = acumuladorAlturaFemeninos / contadorFemeninos

    mensaje = ("La altura promedio de los personajes de genero Femenino es: {0:.2f}".format(promedioAlturaFemeninos))

    return print(mensaje)

# Calcular_Altura_Promedio_De_Femeninos()


# ---------- I) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F) ---------#

def Informar_Heroes():
    Calcular_Masculino_Mas_Alto()
    Calcular_Femenino_Mas_Alto()
    Calcular_Masculino_Mas_Bajo()
    Calcular_Femenino_Mas_Bajo()

# Informar_Heroes()


#----------- J) Determinar cuántos superhéroes tienen cada tipo de color de ojos. -------------#

def Cantidad_De_Personajes_Por_Color_De_Ojos():

    tipos_color_de_ojos = {}

    for personaje in lista_personajes:
        personaje["color_ojos"] = personaje["color_ojos"].capitalize()
        if tipos_color_de_ojos.get(personaje["color_ojos"]) != None:
            tipos_color_de_ojos[personaje["color_ojos"]] += 1
        else:
            tipos_color_de_ojos[personaje["color_ojos"]] = 1

    for tipo in tipos_color_de_ojos:
        mensaje = "Existen {0} personajes con ojos color: {1}".format(tipos_color_de_ojos[tipo], tipo)
        print(mensaje)

# Cantidad_De_Personajes_Por_Color_De_Ojos()


#----------- K) Determinar cuántos superhéroes tienen cada tipo de color de pelo. -------------#

def Cantidad_De_Personajes_Por_Color_De_Pelo():

    tipos_color_de_pelo = {}

    for personaje in lista_personajes:
        personaje["color_pelo"] = personaje["color_pelo"].capitalize()
        if tipos_color_de_pelo.get(personaje["color_pelo"]) != None:
            tipos_color_de_pelo[personaje["color_pelo"]] += 1
        else:
            tipos_color_de_pelo[personaje["color_pelo"]] = 1 

    for tipo in tipos_color_de_pelo:
        mensaje = "Existen {0} personajes con color de pelo: {1}".format(tipos_color_de_pelo[tipo], tipo)
        if tipo == '':
            mensaje = "Existen {0} personajes con ningun color de pelo".format(tipos_color_de_pelo[tipo])
            
        print(mensaje)
    
# Cantidad_De_Personajes_Por_Color_De_Pelo()
    

#----------- L) Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).  -------------#

def Cantidad_De_Personajes_Por_Inteligencia():

    tipos_de_inteligencia = {}
    
    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"].capitalize()
        
        if tipos_de_inteligencia.get(inteligencia) != None:
            tipos_de_inteligencia[inteligencia] += 1
        else:
            tipos_de_inteligencia[inteligencia] = 1
        
    for tipo in tipos_de_inteligencia:
        mensaje = "Existen {0} personajes con inteligencia: {1}".format(tipos_de_inteligencia[tipo], tipo)
        if tipo == '':
            mensaje = "Existen {0} personajes con ningun tipo de inteligencia".format(tipos_de_inteligencia[tipo])
        print(mensaje)

# Cantidad_De_Personajes_Por_Inteligencia()
    
        
#----------- M) Listar todos los superhéroes agrupados por color de ojos. -------------#

def Agrupar_Personajes_Por_Color_De_Ojos():

    lista_personajes_por_color_de_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"].capitalize()
        if lista_personajes_por_color_de_ojos.get(color_ojos) != None:
            lista_personajes_por_color_de_ojos[color_ojos] += personaje["nombre"] + ' | '
        else:
            lista_personajes_por_color_de_ojos[color_ojos] = personaje["nombre"] + ' | '

    for color in lista_personajes_por_color_de_ojos:
        mensaje = "Los personajes con color de ojos '{0}' son : {1}".format(color, lista_personajes_por_color_de_ojos[color])
        print(mensaje)
            
# Agrupar_Personajes_Por_Color_De_Ojos()


#----------- N) Listar todos los superhéroes agrupados por color de pelo. -------------#
        
def Agrupar_Personajes_Por_Color_De_Pelo():

    lista_personajes_por_color_de_pelo = {}

    for personaje in lista_personajes:
        color_pelo = personaje["color_pelo"].capitalize()
        if lista_personajes_por_color_de_pelo.get(color_pelo) != None:
            lista_personajes_por_color_de_pelo[color_pelo] += personaje["nombre"] + ' | '
        else:
            lista_personajes_por_color_de_pelo[color_pelo] = personaje["nombre"] + ' | '

    for color in lista_personajes_por_color_de_pelo:
        mensaje = "Los personajes con color de pelo '{0}' son : {1}".format(color, lista_personajes_por_color_de_pelo[color])
        if color == '':
            mensaje = "Los personajes con ningun color de pelo son: {0}".format(lista_personajes_por_color_de_pelo[color])
        print(mensaje)

# Agrupar_Personajes_Por_Color_De_Pelo()


#----------- O) Listar todos los superhéroes agrupados por tipo de inteligencia -------------#

def Agrupar_Personajes_Por_Inteligencia():

    lista_personajes_por_inteligencia = {}

    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"].capitalize()
        if lista_personajes_por_inteligencia.get(inteligencia) != None:
            lista_personajes_por_inteligencia[inteligencia] += personaje["nombre"] + ' | '
        else:
            lista_personajes_por_inteligencia[inteligencia] = personaje["nombre"] + ' | '

    for tipo in lista_personajes_por_inteligencia:
        mensaje = "Los personajes con tipo de inteligencia '{0}' son : {1}".format(tipo, lista_personajes_por_inteligencia[tipo])
        if tipo == '':
            mensaje = "Los personajes con ningun tipo de inteligencia son: {0}".format(lista_personajes_por_inteligencia[tipo])
        print(mensaje)

# Agrupar_Personajes_Por_Inteligencia()


# --------- MENU ---------- #

while True:
    respuesta = input(
        "\n 1) Nombre de cada Superhéroe Masculino \n 2) Nombre de cada Superhéroe Femenino \n 3) Superheroe masculino mas alto \n 4) Superheroe femenino mas alto \n 5)  Superheroe masculino mas bajo \n 6)  Superheroe femenino mas bajo  \n 7) Promedio de altura de superheroes masculinos \n 8) Promedio de altura de superheroes femeninos \n 9) Nombre de cada indicador anterior \n 10) Cuantos superheroes por tipo de color de ojos \n 11) Cuantos superheroes por tipo de color de pelo \n 12) Cuantos superheroes por tipo de inteligencia \n 13) Lista de superheroes por color de ojos  \n 14) Lista de superheroes por color de pelo  \n 15) Lista de superheroes por tipo de inteligencia \n 16) Salir \n Respuesta > "
    )
    if respuesta == "1":
        Mostrar_Genero_M()
    elif respuesta == "2":
        Mostrar_Genero_F()
    elif respuesta == "3":
        Calcular_Masculino_Mas_Alto()
    elif respuesta == "4":
        Calcular_Femenino_Mas_Alto()
    elif respuesta == "5":
        Calcular_Masculino_Mas_Bajo()
    elif respuesta == "6":
        Calcular_Femenino_Mas_Bajo()
    elif respuesta == "7":
        Calcular_Altura_Promedio_De_Masculinos()
    elif respuesta == "8":
        Calcular_Altura_Promedio_De_Femeninos()
    elif respuesta == "9":
        Informar_Heroes()
    elif respuesta == "10":
        Cantidad_De_Personajes_Por_Color_De_Ojos()
    elif respuesta == "11":
        Cantidad_De_Personajes_Por_Color_De_Pelo()
    elif respuesta == "12":
        Cantidad_De_Personajes_Por_Inteligencia()
    elif respuesta == "13":
        Agrupar_Personajes_Por_Color_De_Ojos()
    elif respuesta == "14":
        Agrupar_Personajes_Por_Color_De_Pelo()
    elif respuesta == "15":
        Agrupar_Personajes_Por_Inteligencia()
    elif respuesta == '16':
        break