"""
10 Alunos
5 Disciplinas

Ler Notas
Media (P/ Aluno) (P/ Disciplina)
"""

import numpy as np

def main():
    Tamanho = np.array([10,5])

    Matriz = np.zeros((Tamanho[0], Tamanho[1]), dtype="i")

    Ler_Dados(Tamanho, Matriz)
    Media_A(Tamanho, Matriz)
    Media_D(Tamanho, Matriz)
    

def Ler_Dados(Tamanho, Matriz):
    
    for C in range (Tamanho[1]):
        Disciplinas = input(f"Introduza as notas da {C + 1}º disciplina separadas por ',': ")
        Disciplinas = Disciplinas.split(",")

        for L in range (Tamanho[0]):
            Matriz[L, C] = int(Disciplinas[L].strip())


def Media_A(Tamanho, Matriz):
    for L in range (Tamanho[0]):
        Soma = 0
        for C in range (Tamanho[1]):
            Soma = Soma + Matriz[L,C]

        print(f"A Media do {L + 1}º aluno é: {round((Soma / Tamanho[1]), 2)}")
    
    print("")


def Media_D(Tamanho, Matriz):
    for C in range (Tamanho[1]):
        Soma = 0
        for L in range (Tamanho[0]):
            Soma = Soma + Matriz[L,C]

        print(f"A Media da {C + 1}º Disciplina é: {round((Soma / Tamanho[0]), 2)}")


if __name__ == "__main__":
    main()