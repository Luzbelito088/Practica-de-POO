from claseEmpleado import empleado
import csv

class gestorEmpleado:
    __listaEmpleado: list

    def __init__(self):
        self.__listaEmpleado = []

    def agregar(self, unEmpleado):
        self.__listaEmpleado.append(unEmpleado)

    def cargar(self):
        archivo = open('empleados.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nomYape = str(fila[0])
            idEmpleado = int(fila[1])
            puesto = str(fila[2])
            unEmpleado = empleado(nomYape, idEmpleado, puesto)
            self.agregar(unEmpleado)
        archivo.close()

    def listar(self):
        for emp in self.__listaEmpleado:
            print(emp)
    
    def informarDuracion(self, idEmp, matricula, programa):
        encontrado = False
        i = 0
        long = len(self.__listaEmpleado)
        while i < long and not encontrado:
            if self.__listaEmpleado[i].getIdEmpleado() == idEmp:
                print("El empleado es: ", self.__listaEmpleado[i].getNyA())
                encontrado = True
                matricula.buscarPorNombre(self.__listaEmpleado[i].getNyA(), programa)
            else:
                i += 1

    def noFueMatriculado(self, matriculado):
        noEsta = None
        for empl in self.__listaEmpleado:
            noEsta = matriculado.verificarAsistencia(empl.getNyA())
            if noEsta == False:
                print("El empleado ", empl.getNyA(), "no fue matriculado en ningun programa.")
            noEsta = None