from claseTelevision import Television
from clasePrensa import PrensaEscrita
from claseRadio import Radio
from clasePrograma import Programa
import csv

class nodo:
    __dato: None
    __siguiente: None

    def __init__(self, medio):
        self.__dato = medio
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, nodo):
        self.__siguiente = nodo

class Lista:
    __comienzo: None
    __actual: None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
        return dato

    def agregar(self, medio):
        nuevoNodo = nodo(medio)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevoNodo
        self.__actual = nuevoNodo
        self.__tope += 1

    def listarMedios(self):
        auxiliar = self.__comienzo
        while auxiliar is not None:
            print(auxiliar.getDato())
            auxiliar = auxiliar.getSiguiente()

    def cargarLista(self):
        archivo = open('medios.csv', "r")
        reader = csv.reader(archivo, delimiter=',')
        next(reader)
        for fila in reader:
            if fila[0] == 'T':
                nombre = fila[1]
                numero = fila[2]
                audiencia = fila[3]
                cantidadProgramas = fila[4]
                self.agregar(Television(nombre, canal, audiencia, cantidadProgramas))
                archivo2 = open('programa.csv' 'r')
                reader2 = csv.reader2(archivo2, delimiter=';')
                next(reader2)
                for fila2 in reader2:
                    if fila2[0] == canal:
                        nombre=fila[2]
                        horaInicio=fila[3]
                        horaFin=fila[4]
                        programa=Programa(nombre,horaInicio,horaFin)
                        unaTele.agregar(programa)
                        self.agregar(unaTele)
            elif fila[0] == 'R':
                nombre = fila [1]
                audiencia = fila[2]
                emisora = fila[3]
                frecuencia = fila[4]
                unaRadio = Radio(nombre, audiencia frecuncia, emisora)
                archivo3 = open3('programa.csv', 'r')
                reader3 = csv.reader3(archivo3, delimiter=';')
                pass