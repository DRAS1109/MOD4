"""
Slicing - Permite ter acesso a subconjunto de uma sequencia ou coleção
sintaxe: dequencia[inicio:fim:passo]
inicio - a posição do primeiro a incluir
fim    - a posição onde termina o slice (não é incluido)
passo  - intervalo entre elementos a incluir no slice
"""
Nome = "Joaquim Silva"

def Primeiras_Letras(Nome):
    Nome_5_Letras = Nome[0:5:1] #Variavel passa a ter as primeiras 5 letras da variavel Nome
    print(Nome_5_Letras)

    Nome_5_Letras = Nome[:5:1]
    print(Nome_5_Letras)

def Ultimas_Letras(Nome):
    Nome_Ultimas_Letras = Nome[7:] #Variavel passa a ter das 7 letras até ao fim da variavel Nome
    print(Nome_Ultimas_Letras)

    Nome_Ultimas_Letras = Nome[7:100]
    print(Nome_Ultimas_Letras)

def Inverter(Nome):
    Nome_Invertido = Nome[::-1] #Variavel passa a ter todas as letras da variavel Nome mas invertidas
    print(Nome_Invertido)

def De_X_em_X(Nome):
    Nome_2_em_2 = Nome[::2] #Variavel passa a ter todas as letras da variavel Nome mas de 2 em 2
    print(Nome_2_em_2)

def Nomes():
    for i in range (len(Nome)):
        if Nome[i] == " ":
            Nome_Proprio = Nome[:i:1]
            Sobrenome = Nome[i + 1:] #i + 1 : Tira o espaço em branco no inicio
            Sobrenome_Inverso = Nome[:i:-1]

    #OU
    Nome_Separados = Nome.split(" ")
    Nome_Proprio = Nome_Separados[0]
    Sobrenome = Nome_Separados[1]

    print(Nome_Proprio)
    print(Sobrenome)
    print(Sobrenome_Inverso)