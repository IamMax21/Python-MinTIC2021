"""
GamePy

El usuario entra a una habitacion oscura y tiene que escoger entre la puerta 1 y la 2.

Puerta 1. Contiene un oso comiendo un pastel de queso, que haras?
    1. Coger el pastel = El oso de come tu cabeza, Good Job!
    2. Gritarle al oso = El oso se come tus puertas, Good Job!
    Otro. No hacer nada, vives. Good Job!

Puerta 2. Te encuentras en un abismo infernal, que tan loco estas?
    1. Uvas rojas 
    2. Chaquetas amarillas
    3. Entiendes el canto

    Si escoge 1 o 2, Tu cuerpo sobrevive, Good Job!
    Si escoges 3, Good Job!
    Otra, Estas jodidamente loco, Good Job!

Otra. Muerto, Good Job!

"""
print("Bienvenido al Juego \nEstas en una habitación oscura y frente a ti hay dos puertas.")
numberDoor=input("¿Cúal deseas abrir? \n1 o 2: ")

if numberDoor.isdigit()==True:
    numberDoor=int(numberDoor)

    if numberDoor==1:
        print("Contiene un oso comiendo un pastel de queso, que haras?")
        accionP1=input("1. Coger el pastel o 2. Gritarle al oso: ")

        if accionP1.isdigit()==True:
            accionP1=int(accionP1)

            if accionP1==1:
                print("El oso de come tu cabeza, Good Job!")
            elif accionP1==2:
                print("El oso se come tus puertas, Good Job!")
            else:
                print("No hacer nada, vives. Good Job!")
            
        else:
            print("No hacer nada, vives. Good Job!")

    elif numberDoor==2:
        print("Te encuentras en un abismo infernal, que tan loco estas?")
        accionP2=input("1. Uvas rojas \n2. Chaquetas amarillas \n3. Entiendes el canto \nEscoge: ")

        if accionP2.isdigit()==True:
            accionP2=int(accionP2)
            
            if accionP2==1 or accionP2==2:
                print("Tu cuerpo sobrevive, Good Job!")
            elif accionP2==3:
                print("Good Job!")
            else:
                print("Estas jodidamente loco, Good Job!")
            
        else:
            print("Estas jodidamente loco, Good Job!")

    else:
        print("Muerto, Good Job!")
else:
    print("Muerto, Good Job!")