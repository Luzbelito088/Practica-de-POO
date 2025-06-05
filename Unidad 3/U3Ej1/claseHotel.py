from claseHabitacion import Habitaciones

class Hotel:
    __nombre: str
    __direccion: str
    __telefono: int
    __listaHabitacion: list

    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaHabitacion = []

    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    
    def agregar_habitacion(self, numero, piso, tipo, precio, disponibilidad):
        self.__listaHabitacion.append(Habitaciones(numero, piso, tipo, precio, disponibilidad))

    def __str__(self):
        return f"Nombre: {self.getNombre()}, Direccion: {self.getDireccion()}, Telefono: {self.getTelefono()}"

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Dirección: {self.__direccion}")
        print(f"Teléfono: {self.__telefono}")
        print("Habitaciones:")
        for habitacion in self.__listaHabitacion:
            habitacion.mostrar()
        print("-" * 30)

    def reservar(self, numero):
        long = len(self.__listaHabitacion)
        i = 0
        encontrado = False
        while i < long and encontrado == False:
            if numero == self.__listaHabitacion[i].getNumero():
                encontrado = True
            else: 
                i += 1
        if(encontrado):
            self.__listaHabitacion[i].reservar()     
        else:
            print("El número ingresado no se encuentra.\n")
    
    def liberar(self, num):
        long = len(self.__listaHabitacion)
        i = 0
        encontrado = False
        while i < long and encontrado == False:
            if num == self.__listaHabitacion[i].getNumero():
                encontrado = True
            else: 
                i += 1
        if(encontrado):
            self.__listaHabitacion[i].liberar()     
        else:
            print("El número ingresado no se encuentra.\n")
        
    def mostrarNyP(self, t):
        encontrado = False
        for habitacion in self.__listaHabitacion:
            if t.lower() == habitacion.getTipoHabitacion().lower():
                print("La Habitación número:", habitacion.getNumero(), "está en el piso número:", habitacion.getPiso())
                encontrado = True
        if not encontrado:
            print("No hay habitaciones de ese tipo.")

    def contarHabitacionesLibresPorPiso(self):
        piso1 = piso2 = piso3 = piso4 = 0
        for habitacion in self.__listaHabitacion:
            if habitacion.getDisponibilidad() == 'True':
                if habitacion.getPiso() == 1:
                    piso1 += 1
                elif habitacion.getPiso() == 2:
                    piso2 += 1
                elif habitacion.getPiso() == 3:
                    piso3 += 1
                elif habitacion.getPiso() == 4:
                    piso4 += 1
        print(f"En el piso 1 hay {piso1} habitaciones disponibles")
        print(f"En el piso 2 hay {piso2} habitaciones disponibles")
        print(f"En el piso 3 hay {piso3} habitaciones disponibles")
        print(f"En el piso 4 hay {piso4} habitaciones disponibles")
    
    def mostrarDetalle(self):
        for habitacion in self.__listaHabitacion:
            print(f"Tipo de habitacion: {habitacion.getTipoHabitacion():<20}")
            print(f"Numero: {habitacion.getNumero():<10} Piso: {habitacion.getPiso():<10} Precio por noche: {habitacion.getPrecioPorNoche():<10} Disponibilidad: {habitacion.getDisponibilidad()}")
            print("-" * 30)