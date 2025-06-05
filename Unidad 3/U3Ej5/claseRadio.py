from claseMedios import Medios

class Radio(Medios):
    __frecuencia: str
    __emisora: str

    def __init__(self, nombre, audiencia, emisora, frecuencia):
        super().__init__(nombre, audiencia)
        self.__frecuencia = frecuencia
        self.__emisora = emisora

    def getFrecuencia(self):
        return self.__frecuencia

    def getEmisora(self):
        return self.__emisora

    def __str__(self):
        return f"{super().__str__()}, Frecuencia: {self.__frecuencia}, Emisora: {self.__emisora}"