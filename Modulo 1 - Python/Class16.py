"""
Diferentes formas de realizar una función.

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