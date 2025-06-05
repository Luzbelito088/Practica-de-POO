from claseHotel import Hotel
import csv

class GestorHotel:

    def __init__(self):
        self.__listaHotel = []

    def agregar(self, habitacion):
        self.__listaHotel.append(habitacion)
    
    def cargar(self):
        archivo = open('Hoteles.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        i = -1
        for fila in reader:
            if len(fila) == 3:
                nombre = fila[0]
                direccion = fila[1]
                telefono = fila[2]
                unHotel = Hotel(nombre, direccion, telefono)
                self.agregar(unHotel)
                i +=1
            else:
                numero = fila[0]
                piso = fila[1]
                tipo = fila[2]
                precio = fila[3]
                disponible = fila[4]
                self.__listaHotel[i].agregar_habitacion(numero, piso, tipo, precio, disponible)
        archivo.close()

        
    def listar(self):
        for unHotel in self.__listaHotel:
            unHotel.mostrar()  

    def agregar_hab(self, h, numero, piso, tipo, precio, disponible):
        i = 0
        encontrado = False
        while i < len(self.__listaHotel) and not encontrado:
            if h.lower() == self.__listaHotel[i].getNombre().lower():
                self.__listaHotel[i].agregar_habitacion(numero, piso, tipo, precio, disponible)
                encontrado = True
            i += 1

        if encontrado == True:
            print("La habitacion fue agregada.")
        else:
            print("No se encontró el hotel, por lo que la habitacion no fue agregada.")
        
    def habitacionesDisponibles(self, h):
        i = 0
        encontrado = False
        while i < len(self.__listaHotel) and not encontrado:
            if h.lower() == self.__listaHotel[i].getNombre().lower():
                encontrado = True
                print(f"Habitaciones disponibles en {self.__listaHotel[i].getNombre()}:")
                lista_hab = self.__listaHotel[i]._Hotel__listaHabitacion
                for habitacion in lista_hab:
                    if habitacion.getDisponibilidad():
                        print(f"  Número: {habitacion.getNumero()}, Piso: {habitacion.getPiso()}, Tipo: {habitacion.getTipoHabitacion()}, Precio: ${habitacion.getPrecioPorNoche()}")
            i += 1
        if not encontrado:
            print("No se encontró el hotel.")

    def reservar(self, h, numero):
        i = 0
        encontrado = False
        while i < len(self.__listaHotel) and not encontrado:
            if h.lower() == self.__listaHotel[i].getNombre().lower():
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            self.__listaHotel[i].reservar(numero)
        else:
            print("El nombre ingresado no se encuentra.\n")

    def liberar(self, h, num):
        i = 0
        encontrado = False
        while i < len(self.__listaHotel) and not encontrado:
            if h.lower() == self.__listaHotel[i].getNombre().lower():
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            self.__listaHotel[i].liberar(num)
        else:
            print("El nombre ingresado no se encuentra.\n")
    
    def mostrarNumeroYPiso(self,h, t):
        i = 0
        encontrado = False
        while i < len(self.__listaHotel) and not encontrado:
            if h.lower() == self.__listaHotel[i].getNombre().lower():
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            self.__listaHotel[i].mostrarNyP(t)
        else:
            print("El nombre ingresado no se encuentra.\n")

    def mostrarHabitacionesLibres(self):
        self.__listaHotel[0].contarHabitacionesLibresPorPiso()

    def mostrarDetallePorTipo(self):
        self.__listaHotel[0].mostrarDetalle()