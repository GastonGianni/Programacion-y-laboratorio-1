'''
Ejercicio Integrador 05

En la base de datos de la división de armamento de industrias Wayne se tiene una información la cual están con la necesidad de cambiar el formato la lista de habilidades con sus respectivos puntos de combate, actualmente cada una de ellas está presente como un diccionario pero para su nuevo sistema requieren que el tipo de dato sea una tupla la cual albergue solamente el nombre de la habilidad y su poder al estilo ("rayo laser", 99). A su vez, todas y cada una de las habilidades deben estar dentro de una lista de habilidades, la cual debe ser el valor de una key que conforme un diccionario, como key par albergarlas usaremos “habilidades_UTN”.
Formato de resultado esperado:

{
 "habilidades_UTN": [("habilidad_alfa", número), ("habilidad_beta", número)] etc.
}

Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores,  conjuntamente con la key que integra dicha estructura de datos.

EJEMPLO

habilidades_UTN:
Habilidad 1: habilidad_alfa | Poder: numero
Habilidad 2: habilidad_beta | Poder: numero
Etcétera.

'''
habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]


i = 0

habilidades_dict = {}
habilidades_dict["habilidades_UTN"] = []
lista_nombre_y_poder = []
mensaje = ""


for habilidad in habilidades:

    nombre_y_poder = habilidad["Nombre"] , habilidad["Poder"]

    lista_nombre_y_poder.append(nombre_y_poder)

    habilidades_dict["habilidades_UTN"].append((lista_nombre_y_poder[i]))

    i += 1
    
habilidades_dict["habilidades_UTN"].sort(key= lambda x:x[1])
    

for i in range(6):
    mensaje += 'Habilidad {0}: {1} | Poder: {2} \n'.format(i, habilidades_dict["habilidades_UTN"][i][0],habilidades_dict["habilidades_UTN"][i][1])

print(mensaje)


# print(habilidades_dict) = {'habilidades_UTN': [('Vuelo', 32), ('Vision-X', 64), ('Super Velocidad', 128), ('Inteligencia', 256), ('Magia', 512), ('Metamorfosis', 1024)]}