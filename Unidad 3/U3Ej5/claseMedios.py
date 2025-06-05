class Medios:
    __nombre: str
    __audiencia: int

    def __init__(self, nombre, audiencia):
        self.__nombre = nombre
        self.__audiencia = audiencia

    def getNombre(self):
        return self.__nombre
    def getAudiencia(self):
        return self.__audiencia

    def __str__(self):
        return f"Nombre: {self.__nombre}, Audiencia: {self.__audiencia}"