lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }
}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el producto mostrar el mensaje 'el articulo no se encuentra en la lista'
# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)
def mostrar_producto(diccionario_recibido:dict):
    consultar_producto = input("Ingrese producto > ")
    producto_seleccionado = diccionario_recibido.get(consultar_producto)
    if producto_seleccionado != None:
        precio_producto = producto_seleccionado.get("precio")
        stock_producto = producto_seleccionado.get("stock")
        print("Producto : {0} | Precio : {1} | Stock : {2}".format(consultar_producto.capitalize(), precio_producto, stock_producto))
        cantidad = int(input("Ingrese cantidad > "))
        print("Precio final : {0}".format(precio_producto * cantidad))
    else:
        print("El producto no se encuentra en la lista")
# mostrar_producto(lista_precios)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios
def ingresar_nueva_fruta(diccionario_recibido:dict):
    nueva_fruta = input("Ingrese fruta > ")
    nuevo_precio = int(input("Ingrese precio > "))
    nueva_medida = input("Ingrese unidad de medida > ")
    nuevo_stock = int(input("Ingrese stock > "))
    diccionario_recibido.update({f"{nueva_fruta}":{"precio":f"{nuevo_precio}","unidad_medida":f"{nueva_medida}","stock":f"{nuevo_stock}"}})

    print(diccionario_recibido)
# ingresar_nueva_fruta(lista_precios)

# Punto 4: imprimir el listado de frutas (solo su nombre)
def listar_frutas(diccionario_recibido:dict):
    list(map(print,list(diccionario_recibido.keys())))
# listar_frutas(lista_precios)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

def eliminar_fruta(diccionario_recibido:dict):
    fruta_a_eliminar = input("Fruta a eliminar > ")
    print(diccionario_recibido.pop(fruta_a_eliminar,"El articulo no se encuentra en la lista"))
    listar_frutas(diccionario_recibido)

# eliminar_fruta(lista_precios)


