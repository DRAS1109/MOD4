import numpy
Meses_2022 = numpy.array(["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
Mortes_2022 = numpy.array([42, 49, 44, 55, 57, 66, 49, 82, 66, 71, 55, 32])

#Mostrar o numero de mortes ocorridas em Março
for Pos in range(len(Meses_2022)):
    if Meses_2022[Pos] == "Março":
        print(f"Mortes do mês de MArço: {Mortes_2022[Pos]}")
        break

#Mostrar o numero total de mortes ocorridas em 2022
Soma = 0
for N in Mortes_2022:
    Soma = Soma + N
print(f"Soma: {Soma}")

#Mostrar a media de mortes por dia em 2022
Media_D = Soma / 365
print(f"Media: {Media_D}")

#Mostrar o numero de mortes registadas no 1º trimestre
Trimestre = Mortes_2022[0] + Mortes_2022[1] + Mortes_2022[2]
print(f"Mortes do 1º Trimestre: {Trimestre}")

#Mostrar o mês com maior nº de mortes
Maior = Mortes_2022[0]
for Pos in range(len(Mortes_2022)):
    if Mortes_2022[Pos] > Maior:
        Maior = Meses_2022[Pos]
        PosM = Pos #PosM = Posição do maior
print(f"Mês com maior nº de mortes: {Meses_2022[PosM]}")

#Contar e mostrar o nº de meses onde as mortes foram superiores à media
Media_M = Soma / len(Meses_2022)
Contagem = 0
for Morte in Mortes_2022:
    if Morte > Media_M:
        Contagem += 1
print(f"Em 2022, foram registadas mais mortes do que a média mensal em {Contagem} meses")