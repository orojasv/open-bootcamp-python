def esPrimo(entero):
    i = 1
    contador = 0
    while i <= 9 and i <= entero:
        if entero % 2 == 0:
            contador += 1
        i += 1
    if contador > 2:
        return False

    return True

str_entero = input("Digite un número entero mayor que 1: ")
entero = int(str_entero)
if(esPrimo(entero)):
    print("El número", str_entero, "es primo")
else:
    print("El número", str_entero, "no es primo")


