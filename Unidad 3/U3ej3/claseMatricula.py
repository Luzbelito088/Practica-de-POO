from claseEmpleado import empleado
from clasePrograma import programa

class Matricula:
    __fecha: str
    __empleado: object
    __programa: object

    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa

    def getFecha(self):
        return self.__fecha
    def getEmpleado(self):
        return self.__empleado
    def getProgramas(self):
        return self.__programa
    
    def __str__(self):
        return f"Fecha: {self.getFecha()} Empleado: {self.getEmpleado()} Programa: {self.getProgramas()}"   