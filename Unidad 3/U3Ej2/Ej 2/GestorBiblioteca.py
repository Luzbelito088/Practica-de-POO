import csv

from Biblioteca import Biblioteca as biblioteca
from Libro import Libro as libro

class GestorBiblioteca:
    __listaBiblioteca: list
    
    def __init__(self):
        self.__listaBiblioteca = []
        
    def agregarBiblioteca(self, unaBiblio):
        self.__listaBiblioteca.append(unaBiblio)
        
    def cargarArchivo(self):
        i = -1
        with open("Biblioteca.csv") as archivoBiblioteca:
            reader = csv.reader(archivoBiblioteca, delimiter = ";")
            for fila in reader:
                if len(fila) == 3:
                    unaBiblioteca = biblioteca(fila[0], fila[1], fila[2])
                    self.agregarBiblioteca(unaBiblioteca)
                    i += 1
                else:
                    unLibro = libro(fila[0], fila[1], fila[2], fila[3])
                    self.__listaBiblioteca[i].agregarLibro(unLibro)
            archivoBiblioteca.close()
            
    def buscarBiblioteca(self, biblio):
        encontrado = False
        i = 0
        indice = -1
        seguir = True
        while seguir and i < len(self.__listaBiblioteca):
            if self.__listaBiblioteca[i].getNombre() == biblio:
                encontrado = True
                indice = i
                seguir = False
            elif i == len(self.__listaBiblioteca):
                encontrado = False
                seguir = False
            else:
                i += 1
            self.estadoBiblioteca(encontrado)
        return indice
        
    
    def estadoBiblioteca(self, encontrado):
        if encontrado: 
            print("\nSe encontro la biblioteca.")
        else:
            print("\nNo se encontro la biblioteca. Por favor ingrese un nombre valido de la siguiente lista: ")
            self.listadoBiblioteca()
            
    def listadoBiblioteca(self):
        print("\nNombre biblioteca: ")
        for biblio in self.__listaBiblioteca:
            print("\n{}".format(biblio.getNombre()))
            
    def agregarLibro(self, indice, nombre, autor, ISBN, genero):
        unLibro =  libro(nombre, autor, ISBN, genero)
        try:
            self.__listaBiblioteca[indice].agregarLibro(unLibro)
            self.__listaBiblioteca[indice].mostrarLibros()
        except TypeError:
            print('Solo se permiten objetos del tipo libro')
        
        
    def eliminarLibro(self, biblioteca, libro):
        indice = self.buscarBiblioteca(biblioteca)
        self.__listaBiblioteca[indice].buscarLibro(libro)
        
    def buscarLibro(self, libro):
        i = 0
        indice = None
        seguir = True
        while seguir and i < len(self.__listaBiblioteca):
            encontrado = self.__listaBiblioteca[i].encontrarBiblioteca(libro)
            if encontrado:
                seguir = False
                indice = i
            elif i == len(self.__listaBiblioteca):
                seguir = False
            else:
                i += 1
        self.imprimirBiblioteca(encontrado, indice)
            
    def imprimirBiblioteca(self, encontrado, indice):
        if encontrado:
            print("\nEl libro ingresado pertenece a la biblioteca:  {}".format(self.__listaBiblioteca[indice].getNombre()))
        else:
            print("\nEl libro ingresado no pertenece a ninguna biblioteca. ")
            
    def mostrarLibros(self, biblioteca):
        indice = self.buscarBiblioteca(biblioteca)
        self.__listaBiblioteca[indice].mostrarLibros()