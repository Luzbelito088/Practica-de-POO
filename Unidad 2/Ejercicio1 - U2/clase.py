# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:06:28 2025

@author: PC
"""
from claseTarjetaSube import TarjetaSube


class Controlador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
    
    def agregar(self, tarjeta):
        if(type(tarjeta) == type(TarjetaSube)):
            self.__lista.append(tarjeta)
            
    def mostrar(self):
        long = len(self.__lista)
        for i in range(long):
            print("Numero: ", self.__lista[i].get_numero(), "Saldo: $", self.__lista[i].get_saldo())
            
    def saldoNegativo(self):
        long = len(self.__lista)
        for t in range(long):
            if(t.get_saldo() < 0):
                print("Numero: ", t.get_saldo())
                
    def buscar_saldo(self, numero):
        long = len(self.__lista)
        i = 0
        encontrado = False
        
        while i < long and encontrado == False:
            if(self.__lista[i].get_numero() == numero):
                encontrado = True
            else:
                i += 1
        if encontrado == True:
            print("El saldo es: $", self.__lista[i].get_saldo())
        else:
            print("El saldo no fue encontrado.")
        
        