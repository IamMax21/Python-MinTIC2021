"""
#Funciones 1. Imprimir los cuadrados del 1 al 5.

def print_squares():
    for i in range(1,6):
        print(i**2, end=", ")

print_squares()

#Funciones 2. Imprimir los cuadrados del 1 al x.

x=int(input("Digite un número: "))
def print_squaresX(limiteSup):
    for j in range(1,limiteSup+1):
        print(j**2)

print_squaresX(x)

#Funciones 3. Escribir una funcion que escriba el reverso de un String

def reverseString (phrase):
    #Metodo 1
    
    index=len(phrase)-1
    rPhrase=""
    while index >= 0:
        
        rPhrase=rPhrase+phrase[index]
        index-=1

    print(rPhrase)
    
    #Metodo 2
    
    print(phrase[::-1])
    
    #Metodo 3
    
    print(''.join(reversed(phrase)))

phrase=input("Dame la frase: ")

reverseString(phrase)


#Funciones 4. Maximo de 3 numeros
def maximos(a,b,c):
    return max(a,b,c)

a=int(input("Digite el primer numero: "))
b=int(input("Digite el segundo numero: "))
c=int(input("Digite el tercero numero: "))

print(maximos(a,b,c))

#Funciones 5. Lista con los numeros sin repetir.

def listaSinRepetir(mylist):
    u=set(mylist)
    lista=list(u)

    return lista

mylist=[1,2,3,4,5,5,7,6,3,8,9]
print(listaSinRepetir(mylist))
"""

#Funciones 6. Determina cuantas veces se repite un string corto dentro de uno largo

# def stringR(string1, string2):
#     contador=string1.count(string2)

#     return contador

# print(stringR("ABCDCDC", "CDC"))

#Funciones 7. Verificador de Paquetes

def procesar_dato(peso, volumen):
    is_valid=False
    if peso<2 and volumen<0.027:
        is_valid=True

    return is_valid
"""
Funciones

Son pedacitos de codigos que permiten realizar una tarea especifica que y que puede reutilizarse varias veces.
Las funciones en python se hace de la siguiente manera 

"def <name> (argumento1, arg2):
    <algorithm>
    (optional) return result.


Metodos
phrase[::-1]= Retorna la frase invertida

i in reversed (range(10)): El iterador empieza de 9 hacia abajo.

'x'.join(list): retorna un string con los elementos de una lista de string, separados por X (tambien es posible no dejar espacios).
este metodo tambien funciona con con una cadena de string.

set(x)= Crea un conjunto con los elementos de X.

list(x)= Crea una lista con los elementos de X.

"""