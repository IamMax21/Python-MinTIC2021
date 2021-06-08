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

#Algoritmo 4. Detectar un email bien escrito.
email=input("Escribe tu email: ")
x=email.find("@")!=-1
y=email.find(".com")!=-1 or email.find(".co")!=-1

if  x==True and y==True:
    print("Valido")
else:
    print("Invalido")

#Algoritmo 5. Validar que el sexo y el email no esten vacios, de estar vacios imprimir "Invalido"
gender=input("Insert your gender (F/M): ").upper()
email=input("Escribe tu email: ")
x=email.find("@")!=-1
y=email.find(".com")!=-1 or email.find(".co")!=-1

if  gender=="" or email=="":
    print("Campos Vacios")
elif x==True and y==True and (gender=="F" or gender=="M"):
    print("Valido")
else:
    print("Invalido")
"""


#Algoritmo 6. Crear un algoritmo que siga las siguientes instrucciones
#   A: Solicite un numero y evalue que sea par o impar; si es impar imprimir algo.
#   B: Si es par y esta dentro de un rango de 2 a 5, imprimir otra cosa.
#   C: Si es par y esta dentro de un rango de 6 a 20, imprimir otra cosa.
#   D: Si es par y mayor a 20 imprimir otra cosa.

number=input("Digite un número: ")

if not number.isdigit():
    print("Usted no digito un número")
else: 
    number=float(number)
    if number%2==0:
        print("A")
    else:
        if number in range(2,6):
            print("B")
        elif number in range(6,21):
            print("C")
        elif number>20:
            print("D")


#Metodos
"""
Modulo: Para sacar el modulo de una division en python se hace mediante el caracter porcentual "%"
Con esto podemos saber cuando un numero es divisible com
pletamente por otro.

.upper(): Método que sirve para pasar todo un string a mayusculas
.lower(): Método que sirve para pasar todo un string a minusculas
.find("@"): Método que sirve para buscar un caracter particular dentro de un string. La salida de dicho metodo, es el numero indice
en el que se encuentra ubicado dicho caracter; de no encontrarse el caracter dentro del String, entonces el metodo retorna -1
in: sirve para evaluar una variable dentro de un rango especifico, ejemplo: 5 IN range (1, 5) (Cabe aclarar que el número 5 no 
queda como una opcion valida dentro del rango, por lo que realmente el rango seria de 1 a 4).


"""

