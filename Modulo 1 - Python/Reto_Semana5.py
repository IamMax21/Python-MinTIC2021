#Prueba Teorica Semana 5
def dicCuadrado(number):
    diccionario={}
    for i in range(0, number):
        
        diccionario[i] = i**2
    return diccionario

print(dicCuadrado(10))
