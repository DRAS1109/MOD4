import numpy as np

# Nº meses
Meses = 12

Maior = -99
Menor = 99
Maior_Moda = 0

Temp = np.zeros(Meses) #Definir array para a temp dos meses
Moda = np.zeros(Meses) #Definir array para a moda


#Ler notas
Soma = 0
for i in range (Meses):
    Temp[i] = int(input(f"Introduza a temp. do {i + 1}º mês: "))
    Soma = Soma + Temp[i] #Somar todas as notas

Media = Soma / Meses # Calcular a média
print (f"A média do ano: {Media}")

for Pos in range (Meses): #Percorrer as Temp. e verificar a maior e a menor
    if Temp[Pos] > Maior:
        Maior = Temp[Pos]
        N_Maior = Pos + 1

    if Temp[Pos] < Menor:
        Menor = Temp[Pos]
        N_Menor = Pos + 1

print (f"A maior média mensal foi {Maior}, do {N_Maior}º mês")
print (f"A menor média mensal foi {Menor}, do {N_Menor}º mês")


for Pos in range (Meses): #Percorrer as Temp. e verificar a inferior e superior à média
    if Temp[Pos] < Media:
        print(f"A media do {Pos + 1}º mês é inferior à média.")
    
    if Temp[Pos] > Media:
        print(f"A media do {Pos + 1}º mês é superior à média.")


for Pos in range (Meses): #Percorrer as Temp.
    for N in Temp:
        if Temp[Pos] == N:
            Moda[Pos] = Moda[Pos] + 1

for Pos in range (len(Moda)): #Identifica a moda
    if Moda[Pos] > Maior_Moda:
        Maior_Moda = Moda[Pos]
        Qual_Moda = Temp[Pos]

print (f"A moda é {Qual_Moda} e apareceu {Maior_Moda} vezes")