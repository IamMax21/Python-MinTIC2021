#Funciones

#Creamos la función
def suma(number1, number2):
    result=number1+number2
    print(f"La suma de los números es: {result}")
#Llamamos la función
suma(1,2)

#Crear una función que calcule la tangente de un angulo

from math import tan

def tangenteAngulo(angulo):
    result1=tan(angulo)
    print(f"La tangente del ángulo es: {result1}")

tangenteAngulo(5)


#Operadores Logicos

#AND. Solo es verdadero cuando todo es verdadero, en los demás casos es falso
input1=True
input2=True
input3=False
input4=False

print(input1 and input2 and input3 and input4)

#OR. Solo es falso cuanto todo es falso, en los demás casos es verdadero
input1=True
input2=True
input3=False
input4=False

print(input1 or input2 or input3 or input4)

#NOT. Cambia el estado de la operación lógica realizada
input1=True
input2=True
input3=False
input4=False

print(not(input1 or input2 or input3 or input4))