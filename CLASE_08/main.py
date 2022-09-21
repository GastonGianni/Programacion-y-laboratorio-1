'''
ARCHIVOS

CSV = Valores separados coma(separador) en columnas de texto plano.
JSON = JavaScript Object Notation (Diccionario Python)

Archivos de texto = Caracteres legibles..(Json,Html,Cvs)
Archivos binarios = No se interpreta en forma de texto. Imagen, sonido, archivo comprimido.. (Jpg,GIF,MP4)

Modos de apertura:
-   r = archivo de texto solo para lectura
    rb = archivo binario solo para lectura
    r+ = archivo de texto para escritura y lectura
-   w = archivo de texto solo para escritura (Si existe lo sobreescribe)        
    wb = archivo solo para escritura (si existe lo sobreescribe)
    w+ = archivo de texto para escritura y lectura (Sobreescribe)
-   a = Abre archivo para anexar informacion 

Para abrir un archivo:
    archivo = open(nombre_archivo, modo)

    archivo: objeto file retornado por open()
    nombre_archivo: ruta completa del archivo
    modo: corresponde al modo de apertura (r,w,a...) se pasa tipo string ""

La funcion open() nos retorna un objeto file (elemento iterable) que contiene diferentes metodos.

Para cerrar un archivo:
    archivo.close()

Leer un archivo:
    ABRIMOS EL ARCHIVO archivo.open('txt', r)

    texto = archivo.read()
    print("El contenido del archivo es: " + texto)

    CERRAMOS EL ARCHIVO archivo.close()

    archivo.readlines() -> Nos retorna una lista separada por salto de linea. (Ideal para .csv)
    readlines() podría optimizarse:
        for linea in archivo:
            print(linea, end="")

Escribir un archivo:
    ABRIMOS EL ARCHIVO archivo.open('txt', w)

    archivo.write('primer linea \n')
    archivo.write('segunda linea \n')
    archivo.write('tercera linea \n')

    CERRAMOS EL ARCHIVO archivo.close()
    ---

    lineas_texto = ['Primer linea\n segunda linea\n tercera linea\n]
    
    archivo.writelines(lineas_texto)

Administrador de contexto:
    Se utiliza (with) para abrir archivos y dejar que el interprete se encargue de cerrar el mismo.

    with open('archivo', 'r+') as archivo:
        for linea in archivo:
            print(linea, end = "")
    
'''


'''
#------PRACTICA------#

def parse_csv(nombre_archivo:str) -> list:
    lista_rta = []
    
    
    archivo = open(nombre_archivo,"r")

    for linea in archivo:
        lista = linea.split(",")
        video["title"] = lista[0]
        video["views"] = lista[1]
        video["length"] = lista[2]
        video["img_url"] = lista[3]
        video["url"] = lista[4]
        video["date"] = lista[5]


    archivo.close()
    return lista_rta


lista_bzrp = parse_csv("ruta de acceso")
print(lista_bzrp)
'''