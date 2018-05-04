
salida = False
agenda = dict()

while not salida:
    accion = input("Que quieres hacer [A = Añadir amigo con su edadd],[C = consultar edad],[S = salir del programa]: ")

    if accion == "A":
        print("Vamos a añadir un amigo con su edad: ")
        print("-------------------------------------")
        nombre = input("Nombre: ")
        edad = input ("Edad: ")
        agenda[nombre] = edad

    elif accion == "C":
        print("Consultar edad: ")
        print("--------------------------------")
        nombre = input("De quien quieres ssaber la edad: ")
        print(agenda[nombre])


    elif accion == "S":
        salida = True