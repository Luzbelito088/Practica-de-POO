class Habitaciones:
    __numero: int
    __piso: int
    __tipoHabitacion: str
    __precioPorNoche: float
    __disponibilidad: bool

    def __init__(self, numero, piso, tipoHabitacion, precio, disponibilidad):
        self.__numero = int(numero)
        self.__piso = int(piso)
        self.__tipoHabitacion = tipoHabitacion
        self.__precioPorNoche = float(precio)
        self.__disponibilidad = disponibilidad

    def getNumero(self):
        return self.__numero
    def getPiso(self):
        return self.__piso
    def getTipoHabitacion(self):
        return self.__tipoHabitacion
    def getPrecioPorNoche(self):
        return self.__precioPorNoche
    def getDisponibilidad(self):
        return self.__disponibilidad
    
    def __str__(self):
        return (f"Numero: {self.getNumero()}, Piso: {self.getPiso()}, Tipo de Habitacion: {self.getTipoHabitacion()}, Precio por Noche: {self.getPrecioPorNoche()}, Disponibilidad: {self.getDisponibilidad()}")
    
    def mostrar(self):
        print("Número: ", self.__numero, ", Piso:", self.__piso, ", Tipo:", self.__tipoHabitacion, ", Precio: $", self.__precioPorNoche, ", Disponible:", self.__disponibilidad, "\n")

    def reservar(self):
        if self.__disponibilidad == 'True':
            self.__disponibilidad = 'False'
            print("Habitación reservada.\n")
        else:
            print("La habitación está ocupada.\n")

    def liberar(self):
        if self.__disponibilidad == 'False':
            self.__disponibilidad = 'True'
            print("Habitación liberada.\n")
        else:
            print("La habitación está desocupada.\n")