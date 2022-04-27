def es_bisiesto(anio):
    if(anio % 4 != 0):
        return False
    elif(anio % 100 != 0):
        return True
    elif(anio % 400 == 0):
        return True
    return False

str_anio = input("Digite el año: ")
anio = int(str_anio)

if(es_bisiesto(anio)):
    print("El año", str_anio, "es bisiesto")
else:
    print("El año", str_anio, "no es bisiesto")

