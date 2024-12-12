import numpy as np

# Nº meses
Meses = 12

Maior = -99
Menor = 99

Temp = np.zeros(Meses) #Definir array para a tem dos meses
Moda = np.zeros(Meses) #Definir array para a tem dos meses


#Ler notas
Soma = 0
for i in range (Meses):
    Temp[i] = int(input(f"Introduza a temp. do {i + 1}º mês: "))
    Soma = Soma + Temp[i] #Somar todas as notas

Media = Soma / Meses # Calcular a média
print (f"A média do ano: {Media}")

for N in range (Meses): #Percorrer as Temp. e verificar a maior e a menor
    if Temp[N] < Maior:
        Maior = Temp[N]
        N_Maior = N

    if Temp[N] > Menor:
        Menor = Temp[N]
        N_Menor = N

print (f"A maior média mensal foi {Maior}, do {N_Maior + 1}º mês")
print (f"A menor média mensal foi {Menor}, do {N_Menor + 1}º mês")


for N in range (Meses): #Percorrer as Temp. e verificar a inferior e superior à média
    if Temp[N] < Media:
        print(f"A media do {N + 1}º mês é inferior à média.")
    
    if Temp[N] > Media:
        print(f"A media do {N + 1}º mês é superior à média.")

for N in range (Meses):
    if Temp[N]