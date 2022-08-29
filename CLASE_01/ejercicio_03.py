'''
La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
1. Nombre de Heroína/Héroe
2. EDAD (mayores a 18 años)
3. Sexo ("m", "f" o "nb")
4. Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
A. Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
B. El sexo y nombre de Heroe | Heroína de mayor edad.
C. La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
D. El promedio de edad entre Heroinas.
E. El promedio de edad entre Heroes de fuerza.
'''

flag_h_mas_joven = True
flag_h_mayor_edad = True
contador_heroinas_fuerza_magia = 0
suma_edad_heroinas = 0
suma_edad_heroes_fuerza = 0
contador_heroinas = 0
contador_heroes_fuerza = 0
promedio_edad_heroinas = 0
promedio_edad_heroes_fuerza = 0


while True:
    nombre = input('Ingrese nombre de Héroe/Heroína: ')

    while True:
        edad = input('Ingrese edad (Mayor de 18 años): ')
        edad = int(edad)
        if edad < 18: continue
        else:break

    while True:
        sexo = input('Ingrese sexo ("m", "f" o "nb"): ')
        if sexo != 'm' and sexo != 'f' and sexo != 'nb': continue
        else: break

    while True:
        habilidad = input('Ingrese habilidad ("fuerza", "magia", "inteligencia"): ')
        if habilidad != 'fuerza' and habilidad != 'magia' and habilidad != 'inteligencia': continue
        else: break

    if flag_h_mas_joven == True and habilidad == 'fuerza':
        edad_mas_joven = edad
        nombre_h_mas_joven = nombre
        flag_h_mas_joven = False
    elif habilidad == 'fuerza' and edad < edad_mas_joven:
        edad_mas_joven = edad
        nombre_h_mas_joven = nombre

    if flag_h_mayor_edad == True:
        mayor_edad = edad
        nombre_h_mayor_edad = nombre
        sexo_h_mayor_edad = sexo
        flag_h_mayor_edad = False
    elif edad > mayor_edad:
        mayor_edad = edad
        nombre_h_mayor_edad = nombre
        sexo_h_mayor_edad = sexo

    if sexo == 'f':
        suma_edad_heroinas += edad
        contador_heroinas += 1

    if habilidad == 'magia' or habilidad == 'fuerza':
        contador_heroinas_fuerza_magia += 1
    elif sexo == 'm' and habilidad == 'fuerza':
        suma_edad_heroes_fuerza += edad
        contador_heroes_fuerza += 1
        


    continuar = input('Desea continuar? s/n: ')
    if continuar == 's': continue
    else: break

if  contador_heroinas != 0:
    promedio_edad_heroinas = suma_edad_heroinas / contador_heroinas
if  contador_heroes_fuerza != 0:
    promedio_edad_heroes_fuerza = suma_edad_heroes_fuerza / contador_heroes_fuerza

if  sexo_h_mayor_edad == 'f':
    sexo_h_mayor_edad = 'Femenino'
elif sexo_h_mayor_edad == 'm':
    sexo_h_mayor_edad = 'Masculino'
else:
    sexo_h_mayor_edad = 'No Binario'

print(  
    'El nombre del Heroe / Heroína de "fuerza" mas joven es:', nombre_h_mas_joven, 'con',edad_mas_joven, 'años', '\n'
    'El sexo y nombre del Heroe / Heroína de mayor edad es:', nombre_h_mayor_edad, "de sexo", sexo_h_mayor_edad,'con',mayor_edad, 'años', '\n'
    'La cantidad de Heroinas que tienen habilidades de Fuerza o Magia es:', contador_heroinas_fuerza_magia, '\n'
    'El promedio de edad entre Heroinas es:', promedio_edad_heroinas, 'años', '\n'
    'El promedio de edad entre Heroes de fuerza es:', promedio_edad_heroes_fuerza, 'años'
    )  
