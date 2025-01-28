"""
Programa para registar as matriculas e o tempo (Segundos) de utilização de um estacionamento.
O programa deve ler as matriculas separadas por "," e os segundos separados por ","
Mostrar:
A media dos tempos de estacionamento
O carro que esteve mais tempo 
Os carros que estiveram mais tempo estacionados do que a media
Verificar se alguma matricula está repetida
Permitir a pesquisa de uma matricula inserida pelo utilizador e mostrar os tempos dessa matricula caso existam
Mostrar a lista das matriculas ordenadas pelos tempos de estacionamento (maior para o menor)
Mostrar os tempos de estacionamento convertidos em minutos:segundos
"""

import numpy as np

def main():
    Max = 10

    Matriculas = np.zeros(Max, dtype = "U8")
    Segundos = np.zeros(Max)

    TdsMatruculas = input("Introduza a matricula do carro: ")
    TdsSegundos = input("Intrduza o tempo e segundos que o carro esteve estacionado: ")

    if "," in TdsMatruculas and "," in TdsSegundos:
        Matriculas_Temp = TdsMatruculas.split(",")
        Segundos_Temp = TdsSegundos.split(",")

        if len(Matriculas_Temp) == len(Segundos_Temp):
            for i in range (len(Matriculas_Temp)):
                Matriculas[i] = Matriculas_Temp[i].strip()
                Segundos[i] = int(Segundos_Temp[i].strip())
        
        else:
            print("O nº de matriculas tem de ser igual ao nº de tempos")
            return

    else:
        print("Ação invalida")
        return

    """Media = C_Media(Segundos)
    Mais_tempo(Segundos, Matriculas)
    Mais_Media(Segundos, Matriculas, Media)
    Matricula_R(Matriculas)
    Pesquisa(Matriculas, Segundos)"""
    Ordenadas(Segundos, Matriculas)

def C_Media(Segundos):

    Soma = 0
    for i in Segundos:
        Soma = Soma + int(i)

    Media = Soma / len(Segundos)
    print(f"A media do tempo de estacionamento é: {round(Media, 3)}s")

    return Media

def Mais_tempo(Segundos, Matriculas):
    Maior = 0
    for i in range(len(Segundos)):
        if Segundos[i] > Maior:
            Maior = Segundos[i]
            Carro = Matriculas[i]

    print(f"O tempo de estacionamento mais longo é: {Maior}s, do carro: {Carro}")

def Mais_Media(Segundos, Matriculas, Media):
    print("Carros que estiveram estacionados a cima da media dos tempos:")
    for i in range(len(Matriculas)):
        if Segundos[i] > Media:
            print(Matriculas[i])

def Matricula_R(Matriculas):
    X = 0
    for i in range (len(Matriculas)):
        if Matriculas[i] == "":
            break

        for j in range (i, len(Matriculas)):
            if Matriculas[i] == Matriculas[j]:
                X = X + 1
        if X > 1:
            print(f"O Carro com a matricula: {Matriculas[i]} estve aqui {X} vezes")

        X = 0

def Pesquisa(Matriculas, Segundos):
    Pesquisar = input("Qual matricula pretende encontrar? ")
    for i in range(len(Matriculas)):
        if Pesquisar in Matriculas[i]:
            print(f"Matricula: {Matriculas[i]} | Tempo: {Segundos[i]}")

def Ordenadas(Segundos, Matriculas):
    Segundos_Ordenados = np.array(Segundos)

    Bubble_Sort(Segundos_Ordenados)

    for i in range(len(Segundos)):
        for f in range(len(Segundos_Ordenados)):
            if Segundos[i] == Segundos_Ordenados[f] and Segundos[i] != 0:
                print(f"Matricula: {Matriculas[i]} | Tempo: {Segundos[i]}")

#TODO:
def Bubble_Sort(Vetor):
    Tamanho = len(Vetor)
    for i in range(Tamanho):
        for j in range(0, Tamanho - i - 1):
            if Vetor[j] > Vetor[j + 1]:
                Temp = Vetor[j]
                Vetor[j] = Vetor[j + 1]
                Vetor[j + 1] = Temp

if __name__ == "__main__":
    main()