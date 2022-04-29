class Alumno:
    _nombre = ""
    _nota = 0

    def setNombre(self, nombre):
        self._nombre = nombre

    def setNota(self, nota):
        self._nota = nota

    def getNombre(self):
        return self._nombre

    def getNota(self):
        return self._nota

    def isAprobado(self):
        nota = self.getNota()
        self._aprobado = True if nota >= 6 else False
        return self._aprobado

a = Alumno()
a.setNombre("Oscar")
a.setNota(5.8)
print("Nota:", a.getNota(), "APROBADO" if a.isAprobado() else "NO APROBADO")
