# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 19:59:48 2025

@author: PC
"""

"""
formas de crear una matriz
1)
def __init__(self):
  self.__lista = [[0]*3 for i in range(4) 
2)
filas=4
columnas=6
Matriz=[]
n=1
for i in range(filas):
  lista=[]
  for j in range(columnas):
  n=n+1
  lista.append(n)
  Matriz.append(lista)  
3)
 __Matriz = []
  def __init__(self): 
     self.__Matriz= np.empty((3, 4))
     """
from ManejadorDepartamento import ManejadorDepartamento

class Accidente:
    __lista = []
    
    def __init__(self):
        filas = 3
        columnas = 12
        n = 1
        matriz = []
        for i in range(filas):
            lista[i]
            for j in range(columnas):
             n = n + 1
             lista.append(n)
             matriz.append(lista)
    
    def cargar(self):
        self.__lista[dpto - 1][mes - 1] - cantidad
        
    def accientes_almes(self, n_mes):
        listaDepartamentos = ManejadorDepartamento()
        print("Accidentes en el mes: ", self.n_mes)
        for i in range(19):
            print("Nombre departamento: ", listaDepartamentos.__listaDepartamento[i].get_nombre())
            print("Accidente: ", self.__lista[i, n_mes])
            
            