#Reto tema 3
#               Planteamiento de la situación

#Una linea de supermercados de renombre en tu país te ha contratado y encomendado la tarea de automatizar 
# el cálculo de la suma a pagar por parte de sus clientes durante una campaña agresiva para mover inventario. 
# La campaña consiste en dar descuentos para algunos productos de hasta el 30%. 
# Adicionalmente, si la fecha de vencimiento del producto es el día de hoy, se aplicará un 20% adicional de descuento.

#La cadena de supermercados ya tiene un software que se encarga de registrar y ordenar los datos de los productos del 
# cliente, utilizando listas y diccionarios, siguiendo la siguiente estructura:

"""
productos = [
    {'sku': 1, 'fecha_expiracion': '', 'precio': 423.646, 'descuento': 0},
    {'sku': 2, 'fecha_expiracion': '', 'precio': 45.117, 'descuento': 24},
    {'sku': 3, 'fecha_expiracion': 'hoy', 'precio': 485.603, 'descuento': 0}
]
"""

#dónde:

# 1. sku corresponde a la llave de identificador único del producto
# 2. fecha_expiracion corresponde a la llave de la fecha de expiración, si el producto vence el día de hoy, tendrá 
#    el valor "hoy", en caso contrario, irá vacía.
# 3. precio corresponde a la llave con el precio del producto
# 4. descuento corresponde a la llave con el descuento de la campaña para rotar inventario. 
#    Este descuento es un número entero, representando el porcentaje a aplicar, es decir, si la llave trae el valor 30 deberás aplicar un 30% de 
#    descuento al precio del producto

#Planteamiento del reto

# Con respecto a la situación planteada, ¿De qué manera crees que puedes automatizar el proceso de cálculo y entrega de la nota?,  
# considerando que la cantidad de productos es numerosa, demandando mucho tiempo para realizar los cálculos de forma manual, y 
# la alta probabilidad de equivocarse;  entonces, se te solicita diseñar un algoritmo desde un lenguaje de programación, que 
# simplifique el tiempo empleado y minimice la probabilidad de error humano al realizar las operaciones necesarias para dar la calificación final.

import json
productos= [{"sku": 1, "fecha_expiracion": "", "precio": 376.443, "descuento": 0}, 
            {"sku": 2, "fecha_expiracion": "hoy", "precio": 84.945, "descuento": 31}, 
            {"sku": 3, "fecha_expiracion": "", "precio": 941.135, "descuento": 15}, 
            {"sku": 4, "fecha_expiracion": "hoy", "precio": 40.244, "descuento": 20}, 
            {"sku": 5, "fecha_expiracion": "hoy", "precio": 796.153, "descuento": 21}, 
            {"sku": 6, "fecha_expiracion": "hoy", "precio": 308.358, "descuento": 0}, 
            {"sku": 7, "fecha_expiracion": "hoy", "precio": 457.561, "descuento": 20}, 
            {"sku": 8, "fecha_expiracion": "", "precio": 322.529, "descuento": 7}, 
            {"sku": 9, "fecha_expiracion": "hoy", "precio": 837.608, "descuento": 0}]
numberObjects=len(productos)
indiceDiccionario=0
subtotal=0
precio=0
descuento=0.0
vencimiento=False
print(f"La lista tiene {numberObjects} objetos")

while indiceDiccionario<numberObjects:

    precio=productos[indiceDiccionario]["precio"]
    if productos[indiceDiccionario]["fecha_expiracion"]=="hoy":
        vencimiento=True
        sku=productos[indiceDiccionario]["sku"]
        print(f"Sku: {sku}")
        print(f"Precio Real: {precio}")
        descuento=(1-(productos[indiceDiccionario]["descuento"])/100)
        print(f"Descuento: {descuento}")
        precio= (precio*descuento)
        print(f"Nuevo Precio: {precio}")
        print(f"Subtotal: {subtotal}")
        print(f"Descuento por Vencimiento: {vencimiento}")
        subtotal+=precio*0.8
        print(f"Nuevo Subtotal: {subtotal}")
        print("")
    else:
        vencimiento=False
        sku=productos[indiceDiccionario]["sku"]
        print(f"Sku: {sku}")
        print(f"Precio Real: {precio}")
        descuento=(1-(productos[indiceDiccionario]["descuento"])/100)
        print(f"Descuento: {descuento}")
        precio= (precio*descuento)
        print(f"Nuevo Precio: {precio}")
        print(f"Subtotal: {subtotal}")
        print(f"Descuento por Vencimiento: {vencimiento}")
        subtotal+=precio
        print(f"Nuevo Subtotal: {subtotal}")
        print("")

    indiceDiccionario+=1
resultado=round(subtotal, 2)

print(resultado)



