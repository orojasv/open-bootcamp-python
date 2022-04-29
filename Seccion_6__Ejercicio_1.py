class Vehiculo:
    color = "Blanco"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad: 80
    cilindrada: 1500

coche = Coche()
coche.color = "Rojo"
coche.velocidad = 90
coche.cilindrada = 1000

print("Color:", coche.color)
print("Ruedas:", coche.ruedas)
print("Puertas:", coche.puertas)
print("Velocidad:", coche.velocidad)
print("cilindrada:", coche.cilindrada)
