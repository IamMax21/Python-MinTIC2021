import math

#Usando la libreria math para realizar diferentes calculos
"""
#Ejercicio 1. Calcula el coseno de un número
number1=10
coseno1=math.cos(number1)

#Ejercicio 2. Calcula la raíz cuadrada de un número insertado por el usuario
number2=int(input("Digite un número "))
raiz=math.sqrt(number2)
print(raiz)
"""

#Ejercicio 3. Write a program that receives from the user the radious of a circule. Your program should calculate the are of the circle.
radiuos=float(input("Escriba el radio de su circulo: "))
pi=math.pi
areCircule=(pi*(radiuos**2))
print("El área del circulo es: {}".format(areCircule))

#Ejercicio 4. Write a program that calculates the result of this math expression y=x^2-3thanh(x)
x=float(input("Digite el valor de X: "))
y=(x**2)-(3*math.tanh(x))
print("El resultado es: ", y)