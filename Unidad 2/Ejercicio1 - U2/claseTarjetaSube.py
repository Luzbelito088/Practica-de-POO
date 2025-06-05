# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:03:00 2025

@author: PC
"""
class TarjetaSube:
    __saldo = int
    __numero = int
    
    def __init__(self, saldo = 0, numero = 0):
        self.__numero = numero
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def get_numero(self):
        return self.__numero
        
    def cargarSaldo(self, importe):
        if (importe > 0):
            self.__saldo += importe
        else:
            print("El importe a cargar debe ser mayor a 2000.")
        
    def pagarPasaje(self, importe):
        if (self.__saldo >= importe):
            self.__saldo -= importe
            print("Saldo: $ ", self.__saldo)
        else:
            print("No hay saldo disponible")
        
    def consultar_saldo(self):
        print(f"El saldo actual es de: ${self.saldo}")
        
    def mostrar(self):
        print(f"mostrar numero: ${self.__numero}")
        print(f"mostrar saldo: ${self.__saldo}")
