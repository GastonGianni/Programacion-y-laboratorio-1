from data_stark import lista_personajes


'''
[
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
]
'''
# A)
 
'''print(lista_personajes)'''

# -----------------B) IMPRIMIR EL NOMBRE DE CADA SUPERHEROE. ---------------- #
'''
for personaje in lista_personajes:
    print("Nombre: {0} ".format(personaje["nombre"])) 
'''

# ---------------- C) IMPRIMIR NOMBRE Y ALTURA ---------------- #
'''
for personaje in lista_personajes:
    personaje["altura"] = float(personaje["altura"])
    print("Nombre: {0} | Altura: {1}".format(personaje["nombre"], personaje["altura"]))

'''

# --------------- D) IMPRIMIR SUPERHEROE MAS ALTO ---------------- #
'''
personaje_mas_alto = lista_personajes[0]

for personaje in lista_personajes:
    personaje["altura"] = float(personaje["altura"])
    # print(personaje["altura"])
    if personaje["altura"] > personaje_mas_alto["altura"]:
        personaje_mas_alto = personaje

# print(personaje_mas_alto["altura"])

# -------------- G) IMPRIMIR NOMBRE DEL MAS ALTO Y EL MAS BAJO  ----------------- #

print("El superheroe mas alto es: {0}, y su altura es de: {1} ".format(personaje_mas_alto["nombre"], personaje_mas_alto["altura"]))

'''

# -------------- E) IMPRIMIR EL SUPERHEROE MAS BAJO ----------------- #

'''
personaje_mas_bajo = lista_personajes[0]

for personaje in lista_personajes:
    personaje["altura"] = float(personaje["altura"])
    # print(personaje["altura"])
    if personaje["altura"] < personaje_mas_bajo["altura"]:
        personaje_mas_bajo = personaje

# print(personaje_mas_bajo["altura"])

# -------------- G) IMPRIMIR NOMBRE DEL MAS ALTO Y EL MAS BAJO  ----------------- #

print("El superheroe mas bajo es: {0}, y su altura es de: {1} ".format(personaje_mas_bajo["nombre"], personaje_mas_bajo["altura"]))

'''
# -------------- F) IMPRIMIR LA ALTURA PROMEDIO DE LOS SH  ----------------- #

'''
acumulador_altura = 0

for personaje in lista_personajes:
    personaje["altura"] = float(personaje["altura"])

    acumulador_altura += personaje["altura"]

# print(acumulador_altura)
# print(len(lista_personajes))
print("La altura promedio de los superhéroes es: {0:.2f}".format(acumulador_altura/len(lista_personajes)))

'''

# -------------- H) IMPRIMIR SUPERHEROE MAS Y MENOS PESADO  ----------------- #
'''
personaje_mas_pesado = lista_personajes[0]
personaje_menos_pesado = lista_personajes[0]

for personaje in lista_personajes:
    personaje["peso"] = float(personaje["peso"])
    # print(personaje["peso"])
    if personaje["peso"] > personaje_mas_pesado["peso"]:
        personaje_mas_pesado = personaje

    if personaje["peso"] < personaje_menos_pesado["peso"]:
        personaje_menos_pesado = personaje
    

# print(personaje_mas_pesado["peso"])
print("\nEl superheroe mas pesado es: {0}, y su peso es: {1} \nEl superheroe menos pesado es {2}, y su peso es: {3} ".format(personaje_mas_pesado["nombre"], personaje_mas_pesado["peso"],personaje_menos_pesado["nombre"] ,personaje_menos_pesado["peso"]))

'''

#------------------I) IMPLEMENTAR FUNCIONES PARA CADA VALOR --------------------#

def mostrar_nombre():
    for personaje in lista_personajes:
        print("Nombre: {0} ".format(personaje["nombre"])) 

def mostrar_nombre_y_altura():
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        print("Nombre: {0} | Altura: {1:.2f}".format(personaje["nombre"], personaje["altura"]))

def calcular_mas_alto():
    personaje_mas_alto = lista_personajes[0]

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
    # print(personaje["altura"])
        if personaje["altura"] > personaje_mas_alto["altura"]:
            personaje_mas_alto = personaje

    print("El superheroe mas alto es: {0}, y su altura es de: {1} ".format(personaje_mas_alto["nombre"], personaje_mas_alto["altura"]))

def calcular_mas_bajo():
    personaje_mas_bajo = lista_personajes[0]

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        # print(personaje["altura"])
        if personaje["altura"] < personaje_mas_bajo["altura"]:
            personaje_mas_bajo = personaje

    print("El superheroe mas bajo es: {0}, y su altura es de: {1} ".format(personaje_mas_bajo["nombre"], personaje_mas_bajo["altura"]))

def calcular_promedio_altura():
    acumulador_altura = 0

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])

        acumulador_altura += personaje["altura"]

    print("La altura promedio de los superhéroes es: {0:.2f}".format(acumulador_altura/len(lista_personajes)))

def calcular_mas_menos_pesado():
    personaje_mas_pesado = lista_personajes[0]
    personaje_menos_pesado = lista_personajes[0]

    for personaje in lista_personajes:
        personaje["peso"] = float(personaje["peso"])
        # print(personaje["peso"])
        if personaje["peso"] > personaje_mas_pesado["peso"]:
            personaje_mas_pesado = personaje

        if personaje["peso"] < personaje_menos_pesado["peso"]:
            personaje_menos_pesado = personaje
    
    print("\nEl superheroe mas pesado es: {0}, y su peso es: {1} \nEl superheroe menos pesado es {2}, y su peso es: {3} ".format(personaje_mas_pesado["nombre"], personaje_mas_pesado["peso"],personaje_menos_pesado["nombre"] ,personaje_menos_pesado["peso"]))

while True:
    respuesta = input("\n 1) Nombre de cada superheroe \n 2) Nombre y Altura \n 3) Superheroe mas alto \n 4) Superheroe mas bajo \n 5) Altura promedio de los superheroes \n 6) Superheroe mas pesado y menos pesado  \n 7) Salir \n >")
    if(respuesta == '1'):
        mostrar_nombre()
    elif(respuesta == '2'):
        mostrar_nombre_y_altura()
    elif(respuesta == '3'):
        calcular_mas_alto()
    elif(respuesta == '4'):
        calcular_mas_bajo()
    elif(respuesta == '5'):
        calcular_promedio_altura()
    elif(respuesta == '6'):
        calcular_mas_menos_pesado()
    elif(respuesta == '7'):break







    





    




    


