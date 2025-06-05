# -*- coding: utf-8 -*-
"""
Created on Fri May  2 14:32:08 2025

@author: PC
"""

from manejadorBeneficiario import *
from manejadorBecas import *

if __name__ == '__main__':
    becas = ManejadorBecas(6)
    beneficiario = ManejadorBeneficiario(14)
    becas.agregar()
    beneficiario.cargar()
    
    def menu(opcion, becas, beneficiario):
        if opcion == 1:
            tipo = input("Ingrese tipo de beca: ")
            becas.buscar_Beca(tipo,beneficiario)
            
        elif opcion == 2:
            dni = input("Ingrese DNI: ")
            beneficiario.informar_becas_por_dni(dni)
        elif opcion == 3:
            beneficiario.listar_beneficiarios_por_facultad()
        elif opcion == 4:
            beneficiario.listar_estudiantes_sin_beca_ayuda()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente de nuevo.")
            
    opcion = 0
    while opcion != 5:
        print("\n------ MENÚ DE OPCIONES ------")
        print("1 - Mostrar beneficiarios por tipo de beca y total a pagar")
        print("2 - Verificar si un beneficiario tiene más de una beca")
        print("3 - Listar beneficiarios ordenados por facultad (descendente)")
        print("4 - Estudiantes con promedio > 8 sin beca de ayuda económica")
        print("5 - Salir")
        opcion = int(input("Seleccione una opción: "))
        menu(opcion, becas, beneficiario)
    

    
    