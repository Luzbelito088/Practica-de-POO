# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:44:17 2025

@author: PC
"""

from claseTarjetaSube import TarjetaSube
from clase import Controlador

def test(self):
    tarjeta = TarjetaSube()
    tarjeta.mostrar()
    tarjeta.cargarSaldo()
    tarjeta.mostrar()
    tarjeta.pagarPasaje()
    tarjeta.cargarSaldo()
    
if __name__ == '__main__':
    
    controlador = Controlador()
    for i in range(3):
        numero = int(input("ingrese numero: "))
        saldo = int(input("Ingrese saldo: "))
        tarjeta = TarjetaSube(saldo, numero)
        controlador.agregar(tarjeta)
    controlador.mostrar()
    controlador.saldoNegativo()
    controlador.buscar_saldo(345)
        