# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:18:10 2025

@author: PC
"""

class Carrera:
    __codigo: int
    __nombre: str
    __titulo_Otorga: str
    __duracion: str
    __grado: str
    __id_facultad: int
    
    
    def __init__(self, codigo, nombre, duracion, titulo, iD, grado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo_Otorga = titulo
        self.__id_facultad = iD
        self.__grado = grado
    
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_duracion(self):
        return self.__duracion
    def get_titulo(self):
        return self.__titulo_Otorga
    def get_idFacultad(self):
        return self.__id_facultad
    def get_grado(self):
        return self.__grado
    
    def mostrar(self):
        print(self.get_codigo(), self.get_duracion(), self.get_grado(), self.get_idFacultad(), self.get_nombre(), self.get_nombre(), self.get_titulo())
    
    def __lt__(self, other):
        return self.__nombre.lower() < other.__nombre.lower()
