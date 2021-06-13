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
#Ejercicio 2. Dibujar las figuras utilizando while y for
"""
******
*****
****
***
**
*
**
***
****
*****
******


n=6
m=6

while not m==0:
    print("*"*m)
    m-=1

while n>0:
    print("*"*n)
    if n==1:
        for i in range(2, 7):
            print("*"*i)
    n-=1    
"""
#Ejercicio 3. Dados los datos de dos listas, imprime los nombres junto a las edades de las personas.
#Ejemplo:
#   Jose 29
#   Diana 28
people=["Jonas","Julio","Mike","Mez"]
ages=[25,30,31,39]

for i in range(0, len(people)-1):
    print(f"{people[i]} {ages[i]}")

#Ejercicio 4. Dada una cadena de caracteres, determine cual es el caracter que mas se repite
#y cuantas veces (case insensitive): +
# Ejemplo: 
# input="hola soy la letra mas repetida." 
# Output= a 5
"""
phrase="hola soy la letra más repetida".replace(" ", "").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
phrase.lower
print(phrase)
contador1=0
contador2=0
for i in range (0, len(phrase)):
    char1=phrase[i]
    contador1=phrase.count(char1)
    if contador1>contador2:
        contador2=contador1
        char2=char1
print(f"{char2} {contador2}")
"""

#Ejercicio 5. Detectar un programa que evalue si los parentesis dentro de un String estan completos (abierto y cerrado)

phrase="hola (soy) la letra (más) repetida".replace(" ","")
index=0
contador1=0
contador2=0
while index!=len(phrase)-1:
    if phrase[index]=="(":
        contador1+=1
    elif phrase[index]==")":
        contador2+=1        
    index+=1
if contador1==contador2:
    print("Good")
else:
    print("Bad")




"""
charR=list[i]
    for j in range (0, len(list)-1):
        if charR==list[j]:
            contador+=1
For anidados
Si el for permite recorrer una determinada lista, uno anidado permite recorrer todos los elementos que existen en diferentes listas.
Ejemplo
for i in range(1,3):
    for j in range(1,10):
        print(f"I: {i} J: {j}")
Donde se puede ver que por cada iterador i, el iterador j recorre toda una lista.

Metodos
.count(x): Permite contar el numero de veces que se repite un caracter dentro de una variable.

in count(x,y): Permite crear un rango donde X determina el numero inicial y Y determina la cantidad los saltos que va dar el iterador (si de dos en dos, tres en tres, etc)

itertools: Libreria muy util para hacer ciertas tareas que tengan iteradores.
    permutations(xyz): Devuelve todas las posibles combinaciones que se pueden dar entre x, y, z. Debes guardar la informacion en una lista.
    list(permutations('ABC'))

    list(compress(data, selector)): Crea una lista en donde "selector" es un True o False, y este valida la lista de "data"
    por tanto, en la nueva lista solo se guardaran los elementos de data que tengan un True en la lista selector.
"""

