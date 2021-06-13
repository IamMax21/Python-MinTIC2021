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
#Ejercicio 1. Números primos, escribir los numeros primos en el rango (2,n)
"""
n=int(input("Digite el limite superior del rango: "))
contador=0
boolPrimo=False
listPrimos=[]
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            contador+=1
            if contador==2:
                print(f"{i} es Primo")
                boolPrimo=True
            else:
                print(f"{i} no es Primo")
                boolPrimo=False
        
    if boolPrimo==True:
        listPrimos.append(i)
    contador=0
    print("")
        
print(listPrimos)
"""
#Ejercicio 2. 



"""
For anidados
Si el for permite recorrer una determinada lista, uno anidado permite recorrer todos los elementos que existen en diferentes listas.
Ejemplo
for i in range(1,3):
    for j in range(1,10):
        print(f"I: {i} J: {j}")
Donde se puede ver que por cada iterador i, el iterador j recorre toda una lista.
Metodos
"""

