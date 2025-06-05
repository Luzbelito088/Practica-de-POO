# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:25:15 2025

@author: PC
"""

class Facultad:
    __codigoF: int
    __nombreF: str
    __direccion: str
    __localidad: str
    __telefono: int
    
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigoF = codigo
        self.__nombreF = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
    
    def get_codigoF(self):
        return self.__codigoF
    def get_nombreF(self):
        return self.__nombreF
    def get_direccion(self):
        return self.__direccion
    def get_localidad(self):
        return self.__localidad
    def get_telefono(self):
        return self.__telefono
    
    def mostrar(self):
        print(self.get_codigoF(), self.get_direccion(), self.get_localidad(), self.get_nombreF(), self.get_telefono())
        
    