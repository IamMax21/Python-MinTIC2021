"""
#Algoritmo 1. Escribe un programa donde preguntes al usuario el numero del mes y el programa debe devolverle el nombre de dicho mes.
year={0: "Invalido", 1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"} 
month=int(input("Digite el número del mes que desea buscar: "))
if month>12:
    print("Invalido")
else:
    print(f"El mes es: {year[month]}")
"""
#Algoritmo 2. Crea un algoritmo que pida al usuario digitar un año. El programa debe determinar si es biciesto o no.

year=input("Digite un año: ")

if not year.isdigit():
    print("Usted no digito un año")
else:
    year=int(year)
    if year%1!=0:
        print("Digite un número valido")
    else:
        if year%4!=0:
            print("No es biciesto")
        else:
            if year%100!=0:
                print("Es biciesto")
            else:
                if year%400==0:
                    print("Es biciesto")
                else:
                    print("No es biciesto")



