#Algoritmo 1. Detectar que el numero es 5
"""
number=float(input("Digite el numero 5: "))

if number==5:
    print("El número es 5")
else:
    print("El número no es 5")

#Algoritmo 2. Detectar que el numero es divisible entre 5

number=float(input("Digite un número divisible entre 5: "))

if number%5==0:
    print("El número es divisible entre 5")
else:
    print("El número no es divisible entre 5")

#Algoritmo 3. Validar Generos M, F

gender=input("Insert your gender (F/M): ").upper()

if gender=="F":
    print(f"{gender}emenino")
elif gender=="M":
    print(f"{gender}asculino")
else:
    print("Dato Ingresado Invalido")
"""
#Algoritmo 4. Detectar un email bien escrito.
email=input("Escribe tu email: ")
x=email.find("@")!=-1
y=(email.find(".com")!=-1 or email.find(".co")!=-1)
if  x==True and y==True:
    print("Valido")
else:
    print("Invalido")


#Metodos
"""
Modulo: Para sacar el modulo de una division en python se hace mediante el caracter porcentual "%"
Con esto podemos saber cuando un numero es divisible com
pletamente por otro.

.upper(): Método que sirve para pasar todo un string a mayusculas
.lower(): Método que sirve para pasar todo un string a minusculas
.find("@"): Método que sirve para buscar un caracter particular dentro de un string. La salida de dicho metodo, es el numero indice
en el que se encuentra ubicado dicho caracter; de no encontrarse el caracter dentro del String, entonces el metodo retorna -1

"""

