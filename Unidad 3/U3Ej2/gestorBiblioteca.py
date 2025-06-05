from claseBiblioteca import Biblioteca
from claseLibro import Libro
import csv

class gestorBiblioteca:

    def __init__(self):
        self.__listaBiblioteca = []

    def agregarBiblioteca(self, unaBiblioteca):
        self.__listaBiblioteca.append(unaBiblioteca)

    def cargar(self):
        archivo = open('Biblioteca.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        i = -1
        for fila in reader:
            if len(fila) == 3:
                unaBiblioteca = Biblioteca(fila[0], fila[1], fila[2])
                self.agregarBiblioteca(unaBiblioteca)
                i += 1
            else:
                titulo = fila[0]
                autor = fila[1]
                isbn = fila[2]
                genero = fila[3]
                unLibro = Libro(titulo, autor, isbn, genero)
                self.__listaBiblioteca[i].agregarLibro(unLibro)
        archivo.close()
    
    def listar(self):
        for biblioteca in self.__listaBiblioteca:
            print(biblioteca)

    def agregarNuevoLibro(self,t,a,isbn,g,b):
        long = len(self.__listaBiblioteca)
        i = 0
        encontrado = False
        while i < long and encontrado == False:
            if self.__listaBiblioteca[i].getNombre().lower() == b.lower():
                nuevoLibro = Libro(t, a, isbn, g)
                self.__listaBiblioteca[i].agregarLibro(nuevoLibro)
                encontrado = True
            else:
                i +=1
        
        if encontrado == True:
            print("El libro se agregó de manera correcta.")
            print("-" * 30)
        else:
            print("El libro no se agregó")
            print("-" * 30)

    def eliminarLibro(self,t,b):
        long = len(self.__listaBiblioteca)
        i = 0
        encontrado = False
        while i < long and encontrado == False:
            if self.__listaBiblioteca[i].getNombre().lower() == b.lower():
                self.__listaBiblioteca[i].eliminarLibro(t)
                encontrado = True
            else:
                i +=1
        
    def mostrar(self, titulo):
        encontrado = False
        for biblioteca in self.__listaBiblioteca:
            for libro in biblioteca._Biblioteca__listaLibro:
                if libro.getTitulo().lower() == titulo.lower():
                    print(f"Biblioteca: {biblioteca.getNombre()} | Autor: {libro.getAutor()} | Género: {libro.getGenero()}")
                    encontrado = True
        if not encontrado:
            print("No se encontró el libro en ninguna biblioteca.")