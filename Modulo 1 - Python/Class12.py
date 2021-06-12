#Reto Semana 3
"""
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
"""


