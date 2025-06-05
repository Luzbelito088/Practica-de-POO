from clasePrograma import  programa
import csv

class gestorPrograma:
    __listaProgramas: list

    def __init__(self):
        self.__listaProgramas = []

    def agregar(self, unPrograma):
        self.__listaProgramas.append(unPrograma)

    def cargar(self):
        archivo = open('programas.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nombre = str(fila[0])
            codigo  = str(fila[1])
            duracion = int(fila[2])
            unPrograma = programa(nombre, codigo, duracion)
            self.agregar(unPrograma)
        archivo.close()

    def listar(self):
        for prog in self.__listaProgramas:
            print(prog)

    def buscarPorPrograma(self, programa):
        i = 0
        long = len(self.__listaProgramas)
        encontrado = False
        while i < long and not encontrado:
            if self.__listaProgramas[i].getNombre().lower() == programa.lower():
                print("La duracion del programa es: ", self.__listaProgramas[i].getDuracion())
                encontrado = True
            else:
                i += 1

    def mostrarMatriculados(self, programa, matricula):
        i = 0
        long = len(self.__listaProgramas)
        encontrado = False
        while i < long and not encontrado:
            if self.__listaProgramas[i].getNombre().lower() == programa.lower():
                matricula.buscarPorPrograma(self.__listaProgramas[i].getNombre())
                encontrado = True
            else:
                i += 1
    