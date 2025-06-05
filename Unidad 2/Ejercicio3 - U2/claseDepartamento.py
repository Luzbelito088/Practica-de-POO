# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 19:59:46 2025

@author: PC
"""

class Departamento:
    __numero: int
    __nombre: str
    
    def __init__(self, numero, nombre):
        self.__numero = numero
        self.__nombre = nombre
    
    def get_numero(self):
        return self.__numero
    
    def get_nombre(self):
        return self.__nombre
    def mostrar(self):
        print("Departamento: ", self.__numero)
        print("Nombre: ", self.__nombre)
        