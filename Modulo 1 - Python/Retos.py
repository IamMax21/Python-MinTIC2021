#import math
#Example - Reto Semana 1. Escriba un programa que calcule el cuadrado de un número.
"""
number=float(input())
powNumber=pow(number, 2)
print(powNumber)
"""

#Original - Reto Semana 1. 
"""
¡Qué bueno! Acabas de recibir tu primer salario luego de una 
ardua jornada de trabajo. Piensas por unos instantes en lo 
que vas hacer con el dinero que has recibido. De manera casi 
inmediata, vienen a tu mente varias ideas; sin embargo, decides 
rápidamente la forma en la que distribuirás el dinero. Un 25 % 
para compra de alimentos, 10% para compra de pasajes, 5% para 
compra de boletos de cine, 20% para compra de libros y el dinero 
restante debe ser destinado para el pago del alquiler del lugar 
donde estás viviendo.

Entrada: Las variables necesarias para realizar los respectivos cálculos
Salida: El resultado corresponde a un número que refleja el saldo luego de realizar las compras.
"""
#Categorias
"""
Alimentos=25%
Pasajes=10%
Boletos de Cine=5%
Libros=20%
Alquiler= (100-25-10-5-20) = 40%
"""
#Resolución de los problemas
salario=int(input())
alquiler=salario*0.4

#Respuesta 1. Formateo de Numero a 2 decimales
print("%.1f"%alquiler)

#Respuesta 2. Redondeo de Numero a 2 decimales con funcion round.
alquiler1=round(alquiler,1)
print(alquiler1)

