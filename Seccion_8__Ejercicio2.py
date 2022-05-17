import pickle

class Vehiculo:
    placa = ""
    marca = ""
    modelo = ""
    motor = 0

    def __init__(self, placa, marca, modelo, motor):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def getMarca(self):
        return self.marca


c1 = Vehiculo("MDM656", "Chevrolet", "Sprint", 1000)

f = open('datos.bin', 'wb')
pickle.dump(c1, f)
f.close()

f = open('datos.bin', 'rb')
vehiculo = pickle.load(f)
f.close()
print(vehiculo.getMarca())