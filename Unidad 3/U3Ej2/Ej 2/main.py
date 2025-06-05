from GestorBiblioteca import GestorBiblioteca as gestorBiblioteca

def menuOpciones():
    print("\n Menu de opciones: ")
    print("\n A. Agregar un libro: ")
    print("\n B. Eliminar libro: ")
    print("\n C. Ingrese el titulo de un libro (se mostrara el nombre de la biblioteca en la que se encuentra, el nombre del autor y el genero del libro).")
    print("\n D. Lista de libros disponibles en una biblioteca.")
    opcion = input("\nIngrese una opcion: ")
    opciones(opcion)
    
def opciones(opcion):
    if opcion == "A":
        opcionA()
    if opcion == "B":
        opcionB()
    if opcion == "C":
        opcionC()
    if opcion == "D":
        opcionD()
        
def opcionA():
    GestorB.listadoBiblioteca()
    biblioteca = input("\nIngrese el nombre de la biblioteca a la que desea agregarle un nuevo libro: ")
    indice = GestorB.buscarBiblioteca(biblioteca)
    if indice != -1:
        nombre = input("\nIngrese el nombre del libro que desea agregar: ")
        autor = input("\nIngrese el nombre del autor del libro que desea agregar: ")
        ISBN = input("\nIngrese el ISBN del libro que desea agregar: ")
        genero = input("\nIngrese el genero  del libro que desea agregar: ")
        GestorB.agregarLibro(indice, nombre, autor, ISBN, genero)
        
def opcionB():
    GestorB.listadoBiblioteca()
    biblioteca = input("\nIngrese el nombre de la biblioteca a la que desea agregarle un nuevo libro: ")
    libro = input("\nIngrese el titulo del libro que desea eliminar: ")
    GestorB.eliminarLibro(biblioteca, libro)
    
def opcionC():
    libro = input("\nIngrese el titulo del libro que desea eliminar: ")
    GestorB.buscarLibro(libro)
    
def opcionD():
    biblioteca = input("\nIngrese el nombre de la biblioteca a la que desea agregarle un nuevo libro: ")
    GestorB.mostrarLibros(biblioteca)

if __name__ == "__main__":
    GestorB = gestorBiblioteca()
    GestorB.cargarArchivo() 
    menuOpciones()