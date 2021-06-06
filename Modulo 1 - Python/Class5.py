#Condicionales

"""
Los condicionales son la estructura que le permite a un programa tomar 
decisiones con base a la evaluación con operadores lógicas y variables.

Para la toma de estas decisiones se utilizan operadores lógicos y operadores iterativos.

Operadores Lógicos
== Igual que?
!= Diferente que?
<  Menor que?
>  Mayor que?
<= Menor o igual que?
>= Mayor o igual que?
"""

#Ejemplos

print(3>=3)
print (3>3)
print(3!=3)
print("max"=="jimenez")
print("max"=="max")
print(3*8==6*4)
print("jjjj"=="j"*4)
print(True==1.0)
print(True!="max")
print(True=="True")
print("1"==1)

"""
Ahora utilizamos los AND, OR y NOT junto a los operadores lógicos
"""

#AND. True only if all the inputs are True
print("AND")
print(True and True and False)

print(True and "jjjj"!="j"*4 and True)

print((True and "jjjj"!="j"*4 and True) and (True and True and False))

#OR. False only if all the inputs are False
print("OR")
print(True or True or False)

print(True or "jjjj"!="j"*4 or True)

print((True or "jjjj"!="j"*4 or True) or (True or True or False))

#NOT. CHANGE THE RESULT
print("NOT")
print(not True)

#Ejercicio
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

#Métodos

number0=input("Digite un número")
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