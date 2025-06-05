class Libro:
    __titulo: str
    __autor: str
    __ISBN: str
    __genero: str
    
    def __init__(self, titulo, autor, ISBN, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__ISBN = ISBN
        self.__genero = genero
        
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getISBN(self):
        return self.__ISBN
    
    def getGenero(self):
        return self.__genero
    
    def __str__(self):
        #return print("\nTitulo: {}          Autor: {}           ISBN: {}            Genero: {}".format(self.getTitulo(), self.getAutor(), self.getISBN(), self.getGenero()))
        return f"Título: {self.__titulo} - Autor: {self.__autor} - ISBN: {self.__ISBN} - Género: {self.__genero}"