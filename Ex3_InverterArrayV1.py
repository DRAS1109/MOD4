#Inverter array: o que esta no espaço 0, passa ao espaço 4 | esta versão utiliza 2 arrays

import numpy as np

#Criar arrays
Array_Normal = np.empty(5, dtype="U20")
Array_Invertido = np.empty(5, dtype="U20")

#tamanho Array
Tamanho = 5
k = Tamanho - 1

for i in range (Tamanho):   #Preencher o Array
    Array_Normal[i] = input("Introduza alguma coisa: ")

   #Inverter Array
    Array_Invertido [k] = Array_Normal[i]
    k = k - 1

print (Array_Invertido)