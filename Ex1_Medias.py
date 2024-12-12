import numpy as np

def Nº_Alunos():
    N_Alunos = int(input("Quantos alunos tem a turma? ")) #Nº de notas que pretende inserir
    return N_Alunos

def Notas(N_Alunos):
    Array_Notas = np.zeros(N_Alunos) #Definir array para as notas

    #Ler notas
    Soma = 0
    for X in range (N_Alunos):
        Array_Notas[X] = int(input(f"Introduza a nota do {X + 1}º aluno: "))
        Soma = Soma + Array_Notas[X] #Somar todas as notas
    
    yield Array_Notas
    return Soma
        
def Media(Soma, N_Alunos, Array_Notas):
    Media = Soma / N_Alunos # Calcular a média
    print (f"A média dos alunos é: {Media}")

    for N in range (N_Alunos): #Percorrer as notas
        if Array_Notas[N] > Media:
            print(f"A nota do {N + 1}º aluno inserido é superior à média.")

def main():
    N_Alunos = Nº_Alunos()
    Soma = Notas(N_Alunos)
    Media (Soma, N_Alunos)

if __name__=="__main__":
    main()