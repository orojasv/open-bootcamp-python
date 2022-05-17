import time

hora_actual = time.strftime("%H:%M:%S")
hora_salida = time.strptime('19:00:00', "%H:%M:%S")


def tiempo_restante(hora_salida, hora_actual):
    horas_restantes = hora_salida.tm_hour - time.strptime(hora_actual, "%H:%M:%S").tm_hour
    segundos_restantes = 60 - time.strptime(hora_actual, "%H:%M:%S").tm_sec
    resta = 'Restan ' + str(horas_restantes) + ' horas, y ' + str(segundos_restantes) + ' segundos'
    return resta


if hora_actual > '19:00:00':
    print("Hora de ir a casa")
else:
    print(tiempo_restante(hora_salida, hora_actual))