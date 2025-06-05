class Programa:
    __nombre: str
    __horaInicio: str
    __horaFin: str

    def __init__(self, nombre, horaInicio, horaFin):
        self.__nombre = nombre
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin

    def getNombre(self):
        return self.__nombre
    def getHoraInicio(self):
        return self.__horaInicio
    def getHoraFin(self):
        return self.__horaFin
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Hora Inicio: {self.__horaInicio}, Hora Fin: {self.__horaFin}"
    