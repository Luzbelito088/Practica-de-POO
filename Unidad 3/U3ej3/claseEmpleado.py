class empleado:
    __nombreYApellido: str
    __idEmpleado: int
    __puesto: str

    def __init__(self, nombreYapellido, idEmpleado, puesto):
        self.__nombreYApellido = nombreYapellido
        self.__idEmpleado = idEmpleado
        self.__puesto = puesto

    def getNyA(self):
        return self.__nombreYApellido
    def getIdEmpleado(self):
        return self.__idEmpleado
    def getPuesto(self):
        return self.__puesto
    
    def __str__(self):
        return f"Nombre y Apellido: {self.getNyA()} Id de Empleado: {self.getIdEmpleado()} Puesto: {self.getPuesto()}"
    
