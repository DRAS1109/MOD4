#Inverter array: o que esta no espaço 0, passa ao espaço 4 | esta versão utiliza 1 array

import numpy as np

#Criar arrays
Array_Normal = np.empty(5, dtype="U20")

#Tamanho Array
Tamanho = 5
k = Tamanho - 1

for i in range (Tamanho):
    #Preencher o Array
    Array_Normal[i] = input("Introduza alguma coisa: ")

#Variavel para chegar a meio do Array
N = round(Tamanho / 2)

for i in range (N):
        Variavel_Descartavel = Array_Normal[k]

        Array_Normal[k] = Array_Normal[i]
        Array_Normal[i] = Variavel_Descartavel
        k = k - 1
   
print (Array_Normal)