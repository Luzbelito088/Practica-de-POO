from gestorBiblioteca import gestorBiblioteca

if __name__ == '__main__':
    ver = gestorBiblioteca()

    ver.cargar()
    ver.listar()

    def menu(opcion, ver):
        if opcion == 1:
            t = input("Ingrese el nombre del libro: ")
            a = input("Ingrese el nombre del autor: ")
            isbn = input("Ingrese el numero de isbn: ")
            g = input("Ingrese el genero del libro: ")
            b = input("Ingrese el nombre de la biblioteca donde quiere agregar el libro: ")
            ver.agregarNuevoLibro(t,a,isbn,g,b)
        elif opcion == 2:
            t = input("Ingrese el nombre del libro: ")
            b = input("Ingrese el nombre de la biblioteca donde quiere eliminar el libro: ")
            ver.eliminarLibro(t,b)
        elif opcion == 3:
            titulo=input("Ingrese el titulo del libro: ")
            ver.mostrar(titulo)
        elif opcion == 4:
            ver.listar()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opcion inválida. Intente de nuevo.")

    opcion = 0
    while opcion != 5:
        print("1- Agregar un nuevo libro a su colección")
        print("2- Eliminar un libro de su colección")
        print("3- Mostrar nombre de la biblioteca y nombre del Autor y Género para un titulo")
        print("4- Mostrar el nombre de todos los libros disponibles en la biblioteca.")
        print("5- Salir")
        opcion = int(input("Ingrese una opcion: "))
        menu(opcion, ver)