import math

def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

area_triangulo = area_triangulo(base=5,altura=7)
print("Área de triangulo de base 5 y altura 7:", str (area_triangulo))

area_circulo = area_circulo(radio=3)
print("Área de circulo de radio 3", str (round(area_circulo,2)))