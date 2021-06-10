
"""
#Algoritmo 1. Imprima el valor minimo y maximo.
string1=input("Mande el String: ")

mylist=string1.split(",")

numberMAX=max(mylist)
numberMIN=min(mylist)

print(f"El número máximo es: {numberMAX} y el minimo es: {numberMIN}" )
"""
#Algoritmo 2. 
# Crea un algoritmo que permita encontrar una palabra X en una frase determinada.
# En el input 1 se entregan las palabras a buscar separadas por espacio
# En el input 2 se entrega la frase donde se van a buscar las palabras.
# Imprimir por YES o NO por cada palabra de encontrarse o no en la frase.

words=input("Palabras: ")
frase=input("Frase: ")
contador=0
contador2=0
myWords=words.split(" ")
myFrase=frase.split(" ")
#Primera Palabra
if myWords[0]==myFrase[0]:
    contador=contador+1
else:
    contador+0
if myWords[0]==myFrase[1]:
    contador=contador+1
else:
    contador+0
if myWords[0]==myFrase[2]:
    contador=contador+1
else:
    contador+0
#Segunda Palabra 
if myWords[1]==myFrase[0]:
    contador2=contador2+1
else:
    contador2+0
if myWords[1]==myFrase[1]:
    contador2=contador2+1
else:
    contador2+0
if myWords[1]==myFrase[2]:
    contador2=contador2+1
else:
    contador2+0

print(f"{myWords[0]}: {contador} \n{myWords[1]}: {contador2} ")


"""
Metodos.

.split()= Sirve para convertir un String en una lista siempre que haya un mismo signo consecutivamente a lo largo de todo el string. 
El metodo retorna una lista con dichos elementos separados en base al signo introducido como parametro.
Ejemplo
String="A,9,1"
String.split(",") ----> Retorna ----> ['A', '9', '1']

Condicionales 2.0

Primera Forma:

    myCondicion=True

    if myCondicion:
        print("Verdadero")
    else:
        print("Falso")

Segunda Forma:

    myCondicion=True

    print("Verdadero") if myCondicion else print("Falso")

.len(mylist): Este metodo retorna la cantidad de elementos que se encuentran en una lista.

"""