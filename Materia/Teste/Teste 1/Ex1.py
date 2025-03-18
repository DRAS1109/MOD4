import numpy as np

Nomes = input("Nomes: ")
Tempos = input("Tempos: ")

Pilotos = np.array(Nomes.split(", "))
Voltas = np.array(Tempos.split(", "))

i = 0
while(i<5):
    if int(Voltas[i]) < 0:
        Voltas[i] = int(input(f"Introduza o tempo do {i} piloto"))

    else:
        i = i + 1

PM = 0
PP = 0

for i in range(5):
    if int(Voltas[i]) < int(Voltas[PM]):
        PM = i

    if int(Voltas[i]) > int(Voltas[PP]):
        PP = i
    
    Diferenca = int(Voltas[PP]) -  int(Voltas[PM])


print(f"Primeiro: {Pilotos[PM]}")
print(f"Ultimo: {Pilotos[PP]}")
print(f"Diferença: {Diferenca} \n")

for i in range(5):
    print(f"{Pilotos[i]}: {Voltas[i]}")