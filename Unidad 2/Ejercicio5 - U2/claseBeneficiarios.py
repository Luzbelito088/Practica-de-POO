# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 19:58:53 2025

@author: PC
"""

class Beneficiarios:
    __dni: int
    __nombre: str
    __apellido: str
    __carrera: str
    __facultad: str
    __anioCursa: int
    __promedio: int
    __idBeca: int
    
    def __init__(self, dni, nombre, apellido, carrera, facultad, anio, promedio, idBecas):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__anioCursa = anio
        self.__promedio = promedio
        self.__idBeca = idBecas
    
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_carrera(self):
        return self.__carrera
    def get_facultad(self):
        return self.__facultad
    def get_anioCursa(self):
        return self.__anioCursa
    def get_promedio(self):
        return self.__promedio
    def get_IdBecas(self):
        return self.__idBeca
    
    def __gt__(self, otro):
        return self.__facultad > otro.get_facultad()
    
    '''def __lt__(self, otro):
        return self.__apellido < otro.get_apellido()
    '''