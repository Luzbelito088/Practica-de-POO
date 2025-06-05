from claseMatricula import Matricula
import csv

class gestorMatricula:
    __listaMatricula: list

    def __init__(self):
        self.__listaMatricula = []

    def agregar(self, unaMatricula):
        self.__listaMatricula.append(unaMatricula)

    def cargar(self):
        archivo = open('matriculas.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            fecha = str(fila[0])
            empleado = str(fila[1])
            programa = str(fila[2])
            unaMatricula = Matricula(fecha, empleado, programa)
            self.agregar(unaMatricula)
        archivo.close()

    def listar(self):
        for matricula in self.__listaMatricula:
            print(matricula)

    def buscarPorNombre(self, NyA, programa):
        
        for matricula in self.__listaMatricula:
            if matricula.getEmpleado().lower() == NyA.lower():
                print("Esta inscripto en el programa: ", matricula.getProgramas())
                programa.buscarPorPrograma(matricula.getProgramas())
    
    def buscarPorPrograma(self, programa):
        for matricula in self.__listaMatricula:
            if matricula.getProgramas().lower() == programa.lower():
                print("El empleado ", matricula.getEmpleado(), "está inscripto en el programa de ", matricula.getProgramas())
    
    def verificarAsistencia(self, nombre):
        esta = False
        for matricula in self.__listaMatricula:
            if matricula.getEmpleado().lower() == nombre.lower():
                esta = True
        return esta