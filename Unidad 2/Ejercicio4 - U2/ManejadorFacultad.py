# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:26:26 2025

@author: PC

 archivo = open("Facultades.csv")
        reader = csv.reader(archivo, delimiter=";")
        primeraFila = True
 for fila in reader:
            if primeraFila == False:
                id = str(fila[0])
                nom = str(fila[1])
                dir = str(fila[2])
                loc = str(fila[3])
                tel =str(fila[4])
                self.__listaFacultades.append(Facultad(id, nom, dir, loc, tel))

"""

import numpy as np
import csv
from claseFacultades import Facultad

class ManejadorFacultad:
    __facultades = []

    def __init__(self):
        self.__facultades = []

    def agregar(self):
        with open("Facultades.csv", encoding='latin-1') as archivo:
            reader = csv.reader(archivo, delimiter=";")
            next(reader)  # Salta encabezado
            for fila in reader:
                id = int(fila[0])
                nom = str(fila[1])
                dir = str(fila[2])
                loc = str(fila[3])
                tel = str(fila[4])
                self.__facultades.append(Facultad(id, nom, dir, loc, tel))

    def listar(self):
        for f in self.__facultades:
            f.mostrar()

    def otroListar(self):
        long = len(self.__facultades)
        for i in range(long):
            self.__facultades[i].mostrar()

    def buscar(self, codigo):
        bandera = False
        long = len(self.__facultades)
        i = 0

        while i < long and not bandera:
            if self.__facultades[i].get_codigoF() == codigo:
                bandera = True
            else:
                i += 1

        if bandera:
            return self.__facultades[i].get_codigoF()
        else:
            print("Facultad no encontrada")
            return None

    def contar(self, mc):
        long = len(mc)
        for facu in self.__facultades:
            indice = facu.get_codigoF()
            contador = 0
            for j in range(long):
                if mc[j].get_idFacultad() == indice:
                    contador += 1
            print("La facultad", facu.get_nombreF(), "tiene", contador, "carreras")

    def buscarFacultadPorNombre(self, nombre):
        bandera = False
        long = len(self.__facultades)
        i = 0

        while i < long and not bandera:
            if self.__facultades[i].get_nombreF().lower() == nombre.lower():
                bandera = True
            else:
                i += 1

        if bandera:
            return self.__facultades[i].get_codigoF()
        else:
            print("Facultad no encontrada")
            return None
