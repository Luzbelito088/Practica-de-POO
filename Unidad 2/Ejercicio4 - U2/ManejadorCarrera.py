# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:25:40 2025

@author: PC
"""

import numpy as np
import csv
from claseCarrera import Carrera

class ManejadorCarrera:
    __carrera = []

    def __init__(self):
        self.__carrera = []

    def agregar(self):
        with open("Carreras.csv", encoding='latin-1') as archivo:
            reader = csv.reader(archivo, delimiter=";")
            next(reader)  # Salta encabezado
            for fila in reader:
                codigo = int(fila[0])
                nombre = str(fila[1])
                titulo = str(fila[2])
                duracion = str(fila[3])
                grado = str(fila[4])
                idF = int(fila[5])
                self.__carrera.append(Carrera(codigo, nombre, duracion, titulo, idF, grado))

    def listar(self):
        for f in self.__carrera:
            f.mostrar()

    def otroListar(self):
        long = len(self.__carrera)
        for i in range(long):
            self.__carrera[i].mostrar()

    def buscar(self, nombre):
        bandera = False
        long = len(self.__carrera)
        i = 0

        while i < long and not bandera:
            if self.__carrera[i].get_nombre().lower() == nombre.lower():
                bandera = True
            else:
                i += 1

        if bandera:
            print("La carrera", nombre, "se dicta en la facultad", self.__carrera[i].get_codigo())
        else:
            print("Carrera no encontrada")

    def get_carreras(self):
        return self.__carrera
    
    def mostrar_carreras_facultad(self, id_facultad):
        carreras_facultad = [carrera for carrera in self.__carrera if carrera.get_idFacultad() == id_facultad]
        carreras_facultad.sort()  # Usa __lt__ que sobrecargaste

        if carreras_facultad:
            print(f"Carreras de la facultad {id_facultad}:")
            for carrera in carreras_facultad:
                print(f"- {carrera.get_nombre()} (Duración: {carrera.get_duracion()})")
        else:
            print("No se encontraron carreras para esa facultad.")

