"""
#Algoritmo 1. Escriba un algoritmo que permita establecer si el dato ingresado es un número positivo, negativo o 0
number1=input("Digite un número")

if number1.lstrip("-").isdigit()==False:
    print("No digitaste ún número")
else:
    number1=float(number1)
    if number1==0:
        print("Es 0")
    elif number1<0:
        print("Es negativo")
    else:
        print("Es positivo")
"""
#Algoritmo 2. Crea un algoritmo que genere un número aleatorio y que le permita al usuario adivinarlo.
import random
numberAl=random.randint(1, 5)
print(numberAl)
number1=input("Digite un número: ")

if number1.lstrip("-").isdigit()==False:
    print("No digitaste ún número")
else:
    number1=float(number1)
    if number1==numberAl:
        print("You Win!")
    else:
        print(f"You Lose. The winner number is {numberAl}")

    



#Métodos
number0=input("Digite un número: ")
print(number0.startswith("-"))
"""
El metodo .startswith sirve para identificar el caracter con el que empieza un valor de una variable.
En este caso utilizamos este metod para poder identificar si el input trae un número negativo mediante la identificacion del signo de resta (-)
Para cuando existe una coincidencia, el metodo retorna TRUE
Para cuando no existe una coincidencia, el metodo retorna FALSE
"""
print(number0.lstrip("-"))
"""
El metodo .lstrip sirve evaluar y eliminar el primer caracter del del valor de una variable.
Para cuando existe una coincidencia, el metodo elimina dicho caracter.
Para cuando no existe una coincidencia, el metodo retorna el mismo valor.
"""

#Librerias
"""
random: Librería que permite generar números aleatorios.
random.randint(inicioRango, finalRango): Permite establecer la generación aleatoria a un número entero dentro de un rango de valores establecidos.
"""