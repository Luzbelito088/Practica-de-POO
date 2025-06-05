# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 18:38:00 2025

@author: PC
"""

from ManejadorCarrera import ManejadorCarrera
from ManejadorFacultad import ManejadorFacultad

if __name__ == '__main__':
    carreras = ManejadorCarrera()
    facultades = ManejadorFacultad()

    print("Cargando carreras...")
    carreras.agregar()

    print("\nListado de Carreras:")
    carreras.otroListar()

    print("\nCargando facultades...")
    facultades.agregar()

    print("\nListado de Facultades:")
    facultades.otroListar()

    # Buscar una carrera por nombre
    nombre = input("\nIngrese el nombre de la carrera que desea buscar: ")
    idFacultad = carreras.buscar(nombre)

    if idFacultad is not None:
        nombreFacultad = facultades.buscar(idFacultad)
        if nombreFacultad is not None:
            print(f"La carrera '{nombre}' se dicta en la facultad '{nombreFacultad}'.")
    else:
        print("No se encontró la carrera.")

    # Contar carreras por facultad
    print("\nCantidad de carreras por facultad:")
    facultades.contar(carreras.get_carreras())

    # Buscar facultad por nombre
    nombre_facultad = input("\nIngrese el nombre de la facultad que desea buscar: ")
    codigo_facultad = facultades.buscarFacultadPorNombre(nombre_facultad)
    if codigo_facultad is not None:
        print(f"El código de la facultad '{nombre_facultad}' es {codigo_facultad}.")
        
    nombre_facultad = input("Ingrese el nombre de la facultad: ")
    id_facultad = facultades.buscarFacultadPorNombre(nombre_facultad)

    if id_facultad is not None:
        carreras.mostrar_carreras_facultad(id_facultad)
