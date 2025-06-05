from claseMedios import Medios

class PrensaEscrita(Medios):
    __tipoPublicacion: str
    __periodicidad: str

    def __init__(self, nombre, audiencia, tipoPublicacion, periodicidad):
        super().__init__(nombre, audiencia)
        self.__tipoPublicacion = tipoPublicacion
        self.__periodicidad = periodicidad

    def getTipoPublicacion(self):
        return self.__tipoPublicacion

    def getPeriodicidad(self):
        return self.__periodicidad

    def __str__(self):
        return f"{super().__str__()}, Tipo de Publicación: {self.__tipoPublicacion}, Periodicidad: {self.__periodicidad}"
    