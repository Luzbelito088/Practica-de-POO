# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:15:48 2025

@author: PC
"""
import numpy as np
import csv
import os
from claseBecas import *


class ManejadorBecas:
    __becasE: np.ndarray
    __dimension: int
    __cantidad: int
    
    def __init__(self, dimension):
        self.__becasE = np.empty(dimension, dtype=Becas)
        self.__cantidad = 0
        self.__dimension = dimension
        
    def get_dimension(self):
        return self.__dimension
    def get_becasE(self):
        return self.__becasE
        
    def agregarB(self,beca):
        if self.__cantidad < self.__dimension:
            self.__becasE[self.__cantidad] = beca
            self.__cantidad += 1
        else:
            print("No hay mas espacio")
    
    def agregar(self):
        archivo = open("becas.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        
        for fila in reader:
            idBecas = int(fila[0])
            tipo = str(fila[1])
            importe = float(fila[2])
            self.agregarB(Becas(idBecas, tipo, importe))
            
        longitud = len(self.__becasE)
        for i in range(longitud):
            print(self.__becasE[i].get_IdBecas(),self.__becasE[i].get_tipo(),self.__becasE[i].get_importe())
            
    def buscar_Beca(self, nombre,beneficiario):
        bandera = False
        long = len(self.__becasE)
        i = 0
        
        while i < long and not bandera:
            if(self.__becasE[i].get_tipo() == nombre):
                bandera = True
            else:
                i += 1
        if(bandera == True):
            cont=beneficiario.informar_beneficiarios_por_tipo(self.__becasE[i].get_IdBecas())
            print("el importe total es {}".format(cont*self.__becasE[i].get_importe()))
        else:
            print("Beca no encontrada")
            
    