# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 19:52:58 2025

@author: PC
"""

class Becas:
    __idBecas: int
    __tipo: str
    __importe: float
    
    def __init__(self, idBecas, tipo, importe):
        self.__idBecas = idBecas
        self.__tipo = tipo
        self.__importe = importe
        
    def get_IdBecas(self):
        return self.__idBecas
    def get_tipo(self):
        return self.__tipo
    def get_importe(self):
        return self.__importe
    
    