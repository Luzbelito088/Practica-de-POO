# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 20:17:23 2025

@author: PC
"""

"""
Codigo Para leer un archivo
archivo = open("Departamentos.csv")
        reader = csv.reader(archivo, delimiter=";")
        primeraFila = True  
"""
import csv
from claseDepartamento import Departamento

class ManejadorDepartamento:
    
    def __init__(self):
        self.__dpto = []
        
    def agregar(self):
        archivo = open("Departamentos.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            id = str(fila[0])
            nom = str(fila[1])
            self.__dpto.append(Departamento(id, nom))
        archivo.close()
        
    def mostrar(self):
        long = len(self.__dpto)
        for i in range(long):
            self.__dpto[i].mostrar()
    