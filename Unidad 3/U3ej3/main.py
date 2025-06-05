from gestorEmpleado import gestorEmpleado
from gestorMatricula import gestorMatricula
from gestorPrograma import gestorPrograma

if __name__ == '__main__':
    empleado = gestorEmpleado()
    matricula = gestorMatricula()
    programa = gestorPrograma()

    empleado.cargar()
    matricula.cargar()
    programa.cargar()
    empleado.listar()
    programa.listar()
    matricula.listar()

    def menu(opcion, empleado, matricula, programa):
        if opcion == 1:
            idEmpleado = int(input("Ingrese el Id del empleado: "))
            empleado.informarDuracion(idEmpleado, matricula, programa)
        elif opcion == 2:
            prog = input("Ingrese el nombre del programa: ")
            programa.mostrarMatriculados(prog, matricula)
        elif opcion == 3:
            empleado.noFueMatriculado(matricula)
        elif opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opcion inválida. Vuelva a intentarlo.")
        
    opcion = 0
    while opcion != 4:
        print("1- Informe la duración de todos los programas de capacitación en los que está matriculado según Id del empleado.")
        print("2- Mostrar el/los empleados matriculados según el nombre del programa")
        print("3- Informar aquellos Empleados que no han sido matriculados en ningún programa de capacitación.")
        print("4- Salir")
        opcion = int(input("Ingrese una opcion: "))
        menu(opcion, empleado, matricula, programa)