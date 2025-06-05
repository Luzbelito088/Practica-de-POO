from claseMedios import Medios

class Television(Medios):
    __canal: int
    __cantidadProgramas: int
    __programas: list

    def __init__(self, nombre,  canal, audiencia, cantidadProgramas):
        super().__init__(nombre, audiencia)
        self.__canal = canal
        self.__cantidadProgramas = cantidadProgramas
        self.__programas = []

    def getCantidadProgramas(self):
        return self.__cantidadProgramas
    def getProgramas(self):
        return self.__programas
    def getCanales(self):
        return self.__canales
    
    def __str__(self):
        return f"{super().__str__()}, Cantidad de Programas: {self.__cantidadProgramas}, Programas: {self.__programas}, Canal: {self.__canal}"
    
    def mostrarProgramas(self):
        pass