"""
La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:

1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
4. La marca y el Fabricante.

 Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.


"""

barbijo_mas_caro_flag = True

mayor_unidades_flag = True

cantidad_jabones = 0


for i in range(2):
    while (True):
        tipo_producto = input('Ingrese tipo de producto ("Barbijo","Jabon","Alcohol"): ')

        if(tipo_producto != "Barbijo" and tipo_producto != "Jabon" and tipo_producto != "Alcohol"): continue
        else:
            break

    while(True):
        precio_producto = input('Ingrese precio (Entre 100 y 300): ')
        precio_producto = int(precio_producto)

        if(precio_producto < 100 or precio_producto > 300): continue
        else:
            break
    
    while(True):
        cantidad_productos = input('Ingrese cantidad de productos (Entre 1 y 1000): ')
        cantidad_productos = int(cantidad_productos)

        if(cantidad_productos < 1 or cantidad_productos > 1000): continue
        else:
            break

    marca_producto = input('Ingrese marca: ')

    fabricante_producto = input('Ingrese fabricante: ')

    if(barbijo_mas_caro_flag == True and tipo_producto == 'Barbijo'):
        precio_barbijo_mas_caro = precio_producto
        unidades_barbijo_mas_caro = cantidad_productos
        fabricante_barbijo_mas_caro = fabricante_producto
        barbijo_mas_caro_flag = False

    if(tipo_producto == 'Barbijo' and precio_producto > precio_barbijo_mas_caro):
        precio_barbijo_mas_caro = precio_producto
        unidades_barbijo_mas_caro = cantidad_productos
        fabricante_barbijo_mas_caro = fabricante_producto

    if(mayor_unidades_flag == True):
        item_mayor_unidades = cantidad_productos
        fabricante_mayor_unidades = fabricante_producto
        mayor_unidades_flag = False
    elif(cantidad_productos > item_mayor_unidades):
        item_mayor_unidades = cantidad_productos
        fabricante_mayor_unidades = fabricante_producto

    if(tipo_producto == 'Jabon'):
        cantidad_jabones += cantidad_productos


    

print('Unidades del barbijo mas caro :', unidades_barbijo_mas_caro)
print('Fabricante del barbijo mas caro :', fabricante_barbijo_mas_caro)

print('Fabricante con mayor unidades: ', fabricante_mayor_unidades)

print('Cantidad de unidades de Jabon: ', cantidad_jabones)



    
       
