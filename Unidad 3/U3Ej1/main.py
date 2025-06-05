from gestorHotel import GestorHotel

if __name__ == '__main__':
    ver = GestorHotel()
    ver.cargar()
    ver.listar()

    def menu(opcion, ver):
        if opcion == 1:
            print("Para agregar una habitacion, ingrese los siguientes datos:")
            hotel = input("Ingrese el nombre del Hotel para agregar habitación: ")
            num = int(input("Ingrese el numero de habitacion: "))
            piso = int(input("Ingrese el piso de la habitacion: "))
            tipo = input("Ingrese el tipo de habitacion: ")
            precio = float(input("Ingrese el precio de la habitacion: "))
            disponible = input("Ingrese la disponibilidad: ")
            ver.agregar_hab(hotel, num, piso, tipo, precio, disponible)
            ver.listar()
        elif opcion == 2:
            hotel = input("Ingrese el nombre del Hotel donde desea reservar: ")
            ver.habitacionesDisponibles(hotel)
            numero = int(input("Ingrese el numero de habitacion que desea reservar: "))
            ver.reservar(hotel, numero)
        elif opcion == 3:
            hotel = input("Ingrese el nombre del hotel: ")
            numero = int(input("Ingrese el numero de habitacion que desea liberar: "))
            ver.liberar(hotel, numero)
        elif opcion == 4:
            hotel = input("Ingrese el nombre del Hotel: ")
            tipo = input("Ingrese el tipo de habitacion que desea ver (suite, doble, sencilla): ")
            ver.mostrarNumeroYPiso(hotel, tipo)
        elif opcion == 5:
            ver.mostrarHabitacionesLibres()
        elif opcion == 6:
            ver.mostrarDetallePorTipo()
        elif opcion == 7:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente de nuevo.")

    opcion = 0
    while opcion != 7:
        print("1. Agregar habitaciones al hotel.")
        print("2. Reservar una habitación.")
        print("3. Liberar una habitación.")
        print("4. Dado un tipo de habitación (sencilla, doble, suite), mostrar número y piso de las habitaciones de ese tipo.")
        print("5. Mostrar la cantidad de habitaciones libres por piso.")
        print("6. Para cada tipo de habitación mostrar el detalle")
        print("7. Salir")
        opcion = int(input("Ingrese una opcion: "))
        menu(opcion, ver)