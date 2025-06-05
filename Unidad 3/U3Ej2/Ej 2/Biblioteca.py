from Libro import Libro as libro

class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaLibros: list
    __libro: object
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaLibros = []
    
    def agregarLibro(self, unLibro):
        if isinstance(unLibro, libro):
            self.__listaLibros.append(unLibro)
        else:
            raise TypeError
    
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def mostrarLibros(self):
        for libro in self.__listaLibros:
            print("\nTitulo del libro{}         Autor: {}           ISBN: {}           Genero: {}".format(libro.getTitulo(), libro.getAutor(), libro.getISBN(), libro.getGenero()))
            #print(libro)
            
    def buscarLibro(self, libro):
        encontrado = False
        i = 0
        seguir = True
        while seguir and i < len(self.__listaLibros):
            if libro == self.__listaLibros[i].getTitulo():
                del self.__listaLibros[i]
                seguir = False
                encontrado = True
            elif i == len(self.__listaLibros):
                seguir = False
            else:
                i += 1
        self.confirmacionLibroEncontrado(encontrado)
    
    def confirmacionLibroEncontrado(self, encontrado):
        if encontrado:
            print("\nLibro encontrado y eliminado.")
            print("\nNueva lista de libros: ")
        else:
            print("\nLibro no encontrado.")
        self.mostrarLibros()
    
    def mostrarLibros(self):
        print("\nTitulo libro:          Autor del libro:            ISBN:           Genero del libro: ")
        for libro in self.__listaLibros:
            print("\n{}          {}            {}           {}".format(libro.getTitulo(), libro.getAutor(), libro.getISBN(), libro.getGenero()))
    
    def encontrarBiblioteca(self, libro):
        encontrado = False
        i = 0
        seguir = True
        while seguir and i < len(self.__listaLibros):
            if libro == self.__listaLibros[i].getTitulo():
                encontrado = True
                seguir = False
            elif i ==  len(self.__listaLibros):
                seguir = False
            else:
                i += 1
        return encontrado 