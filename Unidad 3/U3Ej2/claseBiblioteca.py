from claseLibro import Libro

class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: int
    __listaLibro: list

    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaLibro = []

    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def __str__(self):
        cadena = f"Nombre: {self.__nombre} Direccion: {self.__direccion} Telefono: {self.__telefono}\nLibros:"
        if len(self.__listaLibro) == 0:
            cadena += " Sin libros"
        else:
            for libro in self.__listaLibro:
                cadena += f"\n  {libro}"
        return cadena
    
    def agregarLibro(self, unLibro):
        if isinstance(unLibro, Libro):
            self.__listaLibro.append(unLibro)
        else:
            raise TypeError
    
    def eliminarLibro(self, t):
        long = len(self.__listaLibro)
        i = 0
        encontrado = False
        while i < long and encontrado == False:
            if self.__listaLibro[i].getTitulo().lower() == t.lower():
                self.__listaLibro.pop(i)
                encontrado = True
            else:
                i+=1
        if encontrado:
            print("El libro fue eliminado.")
            print("-" * 30)
        else:
            print("El libro no se eliminó")
            print("-" * 30)
