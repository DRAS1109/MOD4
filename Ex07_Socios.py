#Programa para identificar os socios que estão em 2 clubes ao mesmo tempo

import numpy as np

ClubeA = np.empty(["João", "Mario", "Maria", "Luiz", "Felipe"])
ClubeB = np.empty(["Joana", "Mario", "Mariana", "Luisa", "Gabriel"])

for Nome in ClubeA:
    if Nome in ClubeB:
        print(f"O nome do sócio nos 2 clubes é: {Nome}")