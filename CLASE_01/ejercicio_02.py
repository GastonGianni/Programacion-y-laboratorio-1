'''
EJERCICIO 02

La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
1) PESO: (entre 10 y 100 kilos)
2) PRECIO POR KILO: (mayor a 0 [cero]).
3) TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).

Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.

A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
'''
peso_total = 0
descuento = 0
total_precio_por_kilo = 0
cantidad_de_ingresos = 0
precio_bruto = 0
flag_alimento_mas_caro = True

while True:
    peso_ingresado = input('Ingrese peso (Entre 10 y 100 kilos): ')
    peso_ingresado = int(peso_ingresado)
    while peso_ingresado < 10 or peso_ingresado > 100:
        peso_ingresado = input('Error. Ingrese peso (Entre 10 y 100 kilos): ')
        peso_ingresado = int(peso_ingresado)
    
    precio_por_kilo = input('Ingrese precio por kilo (Mayor a 0): ')
    precio_por_kilo = int(precio_por_kilo)
    while precio_por_kilo < 0:
        precio_por_kilo = input('Error. Ingrese precio por kilo (Mayor a 0): ')
        precio_por_kilo = int(precio_por_kilo)

    tipo_ingresado = input('Ingrese tipo ("v", "a", "m");(vegetal, animal, mezcla): ')
    while tipo_ingresado != 'v' and tipo_ingresado != 'a' and tipo_ingresado != 'm':
        tipo_ingresado = input('Error. Ingrese tipo ("v", "a", "m");(vegetal, animal, mezcla): ')

    if flag_alimento_mas_caro == True:
        precio_mas_caro = precio_por_kilo
        tipo_alimento_mas_caro = tipo_ingresado
        flag_alimento_mas_caro = False
    elif precio_por_kilo > precio_mas_caro:
        precio_mas_caro = precio_por_kilo
        tipo_alimento_mas_caro = tipo_ingresado

    peso_total += peso_ingresado

    total_precio_por_kilo += precio_por_kilo

    precio_bruto += precio_por_kilo * peso_ingresado

    cantidad_de_ingresos += 1

    continuar = input('Continuar? s/n: ')

    if continuar == 's': continue
    else: break

promedio_precio_por_kilo = total_precio_por_kilo / cantidad_de_ingresos

if tipo_alimento_mas_caro == 'v':
    tipo_alimento_mas_caro = 'Vegetal'
elif tipo_alimento_mas_caro == 'a':
    tipo_alimento_mas_caro = 'Animal'
else:
    tipo_alimento_mas_caro = 'Mezcla'

print ('Precio bruto sin descuento: $',precio_bruto,"\n"
        'Tipo de alimento mas caro:', tipo_alimento_mas_caro,"\n"
        'Promedio de peso por kilo: $',promedio_precio_por_kilo)

# print('precio bruto:', precio_bruto)

if peso_total >= 100 and peso_total < 300:
    descuento = 15
elif peso_total >= 300:
    descuento = 25

# print ('descuento', descuento)

if descuento != 0:
    calculo_descuento = (descuento / 100) * precio_bruto

#   print (calculo_descuento)

    precio_final = precio_bruto - calculo_descuento
    print('El precio final con descuento es: $', precio_final)