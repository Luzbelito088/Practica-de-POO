# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:17:28 2025

@author: PC
"""
import numpy as np
import csv
import os
from claseBeneficiarios import *


class ManejadorBeneficiario:
    __beneficiarioB : np.ndarray
    __dimension: int
    __cantidad: int
    
    def __init__(self, dimension):
        self.__beneficiarioB = np.empty(dimension, dtype=Beneficiarios)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def get_Dimension(self):
        return self.__dimension
    def get_BeneficiarioB (self):
        return self.__beneficiarioB
    
    def agregar(self, beneficiarios):
        if self.__cantidad < self.__dimension:
            self.__beneficiarioB[self.__cantidad] = beneficiarios
            self.__cantidad += 1
        else:
            print("No hay mas espacio")
    
    def cargar(self):
        archivo = open("beneficiarios.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        
        for fila in reader:
            dni = int(fila[0])
            nombre = str(fila[1])
            apellido = str(fila[2])
            carrera = str(fila[3])
            facultad = str(fila[4])
            anio = int(fila[5])
            promedio = int(fila[6])
            idBecas = int(fila[7])
            self.agregar(Beneficiarios(dni, nombre, apellido, carrera, facultad, anio, promedio, idBecas))
        
        longitud = len(self.__beneficiarioB)
        for i in range(longitud):
            print(self.__beneficiarioB[i].get_dni(),self.__beneficiarioB[i].get_nombre(),self.__beneficiarioB[i].get_apellido(), self.__beneficiarioB[i].get_carrera(),self.__beneficiarioB[i].get_facultad(),self.__beneficiarioB[i].get_anioCursa(), self.__beneficiarioB[i].get_promedio(), self.__beneficiarioB[i].get_IdBecas())
    
    def informar_beneficiarios_por_tipo(self, beca):
        long = len(self.__beneficiarioB)
        cont = 0
        i = 0
        
        while i < long:
            if(self.__beneficiarioB[i].get_IdBecas() == beca):
                cont+=1
            i += 1
        
        return cont
        
    def informar_becas_por_dni(self, dni):
        large = len(self.__beneficiarioB)
        bandera = False
        i = 0
        count = 0
        while i < large:
            if(self.__beneficiarioB[i].get_dni == dni):
                count += 1
            else:
                i += 1
        
        if (count >= 2):
            print("El alumno ", self.__beneficiarioB[i].get_nombre, self.__beneficiarioB[i].get_apellido, "tiene mas de una beca")
        else:
            print("No hay beneficiarios de mas de una beca")
    
    def listar_beneficiarios_por_facultad(self):
        self.__beneficiarioB = np.sort(self.__beneficiarioB)
        for beneficiario in self.__beneficiarioB:
            print("facultad: {}, dni: {}".format(beneficiario.get_facultad(),beneficiario.get_dni()))
        