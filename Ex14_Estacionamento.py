"""
Programa para registar as matriculas e o tempo (Segundos) de utilização de um estacionamento.
O programa deve ler as matriculas separadas por "," e os segundos separados por ","
"""

import numpy as np

Max = 10

Matriculas = np.zeros(Max, dtype = "U8")
Segundos = np.zeros(Max, dtype = "U10")

TdsMatruculas = input("Introduza a matricula do carro: ")
TdsSegundos = input("Intrduza o tempo e segundos que o carro esteve estacionado: ")

for i in range (Max):
    if "," in TdsMatruculas:
        Matriculas[i] = TdsMatruculas.split(",")[i].strip()

    if "," in TdsSegundos:
        Segundos[i] = TdsSegundos.split(",")[i].strip()
    else:
        print("Ação invalida")
        break
    
"""
Tamanho  = len(Matriculas)
for i in range(Tamanho):
    for j in range(0, Tamanho - i - 1):
        if Matriculas[j] > Matriculas[j + 1]:
            Temp = Matriculas[j]
            Matriculas[j] = Matriculas[j + 1]
            Matriculas[j + 1] = Temp"""