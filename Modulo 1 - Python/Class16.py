"""
Diferentes formas de realizar una función.

"""
"""
import math
#Función. Manera 1
def apply_operation(number, default_operation="sqrt"):
    if default_operation=="sqrt":
        return math.sqrt(number)

#Función. Manera 2
def apply_operation(number, default_operation="sqrt"):
    if default_operation=="sqrt":
        return math.sqrt(number)
    if default_operation=="tan":
        return math.tan(number)
    if default_operation=="cos":
        return math.cos(number)

#Función. Manera 3                                             # De esta ultima manera puedes darle la flexibilidad 
def apply_operation(number, default_operation=math.sqrt):      # al usuario de escoger la operacion que quiera del 
    return default_operation(number)                           # modulo math sin tener que hacer 60 ifs correspondientes 
                                                               # al total de modulos totales que podria escribir el usuario.

#Ejemplo

var=4

print(apply_operation(var, default_operation=math.tan))
"""
# También podemos hacer una miscelanea de funciones a traves de un diccionario en donde creamos varias funciones y las listamos como objetos en dicho diccionario
# para despues escoger dicha operacion.


"""
argumento (*n): Esto hace que en dicha variable puedas meter diferentes argumentos que esten separados por comas y que estos van a ser guardados en una tupla.

"""
# Tenemos un caso muy particular con el uso de los diccionarios en las funciones. La primera cosa que tenemos que 
# tener en cuenta es que vamos a necesitar que la funcione requiera argumentos con la misma notacion que las llaves
# que tiene el diccionario.

data={"name":"max","surname":"jimenez","age":27,"email":"maxjip@gmail.com"}

#Metodo tradicional para imprimir el nombre

# def foo(data):
#     print(data["name"])
# foo(data["name"])

#Metodo Semimoderno para requerir el nombre
# def foo(name, data):
#     print(name)

# foo(data["name"],data)

#Metodo SuperPython
def foo(name, surname, **data):
    print(name)
    print(surname)

foo(**data)

#De esta manera puedes solicitar todos los argumentos que quieras del diccionario y la variable **data 
# guardara esas llaves para imprimir posteriormente esos unicos parametros de los objetos del diccionario.

# Si no colocas el **data dentro como argumento en la funcion, al pasarle el **data como variable en la funcion foo
# python intentara meter a la fuerza todos las llaves que tiene el diccionario dentro de la funcion, por lo cual si
# el diccionario tiene mas llaves de las que la funcion solicita, este producira un error.
 