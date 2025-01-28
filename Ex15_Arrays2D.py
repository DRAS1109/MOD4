"""
Definir uma matriz 5,3
"""

import numpy as np

Matriz = np.zeros((5,3), dtype="i")

#Ciclo p/ percorrer a Matriz
for L in range(Matriz.shape[0]):
    for C in range(Matriz.shape[1]):
        Matriz[L, C] = L*C

print(Matriz)