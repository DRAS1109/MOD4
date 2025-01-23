"""Implementar a ordenação bubble sort com um array"""

import numpy as np

Numeros = np.array([29000, 10, 37, 14, 14])

def Bubble_Sort(Vetor):
    Tamanho  = len(Vetor)
    for i in range(Tamanho):
        for j in range(0, Tamanho - i - 1):
            if Vetor[j] > Vetor[j + 1]:
                Temp = Vetor[j]
                Vetor[j] = Vetor[j + 1]
                Vetor[j + 1] = Temp


print(Numeros)
Bubble_Sort(Numeros)
print(Numeros)