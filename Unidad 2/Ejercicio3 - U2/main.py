# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 20:29:30 2025

@author: PC
"""

from claseDepartamento import Departamento
from ManejadorDepartamento import ManejadorDepartamento
from claseAccidente import Accidente

if __name__ == '__main__':
    manejador = ManejadorDepartamento()
    accidente = Accidente()
    manejador.agregar()
    manejador.mostrar()
    
    for i in range(12):
        numero = int(input("ingrese el numero de departamento: "))
        mes = int(input("ingrese el mes: "))
        cantidad = int(input("ingrese el numero de accidentes: "))
        accidente.cargar(numero, mes, cantidad)