#Conjuntos. Sirven para crear conjuntos y realizar operaciones propias de conjuntos
my_set={1,2,3,4}

#Tuplas. Sirven para crear listas inmutables.
my_tuple=(1,2,3)

#Listas. Sirven para crear listas que pueden ser utilizadas de diferentes formas
my_list=["Max", "Jimenez", "Jimenez", True]
    #Metodos
my_list.append("False") #Metodo para agregar un valor al final de la lista
print(my_list)
my_list.remove("Jimenez") #Metodo para remover la primera coincidencia con el valor usado "Jimenez" en este caso
print(my_list)
bool=my_list.pop() #Metodo para eliminar y retornar el valor de una posicion de la lista; sino se especifica el indice, se asumirá la ultima posición de la lista.
print(bool)

#Diccionarios. Estructuras orientadas al vinculo de llave valor.
my_dic={"key1":1, "key2":"String", "key3":True,}
print(my_dic["key3"])

my_dic={"Name":"Max", "Surname":"Jimenez", "Edad":27,}
print(my_dic["Edad"])

my_dic={1:"Max", 2:"Jimenez", 3:27,}
print(my_dic[1])

my_dic={"Name":"Max", "Surname":"Jimenez", "Notas":[5,3,1,2,0,4]}
print("La primera nota de Max es de ", my_dic["Notas"][0])

my_dic={"Name":"Max", "Surname":"Jimenez", "Notas":{1:5,2:3,3:1,4:2,5:0,6:4}}
print("La primera nota de Max es de ", my_dic["Notas"][2])