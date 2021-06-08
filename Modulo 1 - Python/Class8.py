#Algoritmo 1. Escribe un programa donde preguntes al usuario el numero del mes y el programa debe devolverle el nombre de dicho mes.

year={0: "Invalido", 1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"} 
month=int(input("Digite el número del mes que desea buscar: "))
if month>12:
    print("Invalido")
else:
    print(f"El mes es: {year[month]}")
