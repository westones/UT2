def checkpar(numero):
    if numero % 2 == 0:
        print("El número es Par!")
    else:
        print("El número es Impar!")


p2 = "y"
while p2.lower() != "n":
    try:
        p1 = int(input("Introduce un número: "))
        checkpar(p1)
    except ValueError:
        print("No has introducido un número")

    p2 = input("Quieres salir? y/n \n")
    if p2.lower() == "y":
        break
    elif p2.lower() == "n":
        continue
    else:
        while True:
            p2 =input("Indica 'y' o 'n' ")
            if p2.lower() == "y" or p2.lower() == "n":
                break
            else:
                continue
