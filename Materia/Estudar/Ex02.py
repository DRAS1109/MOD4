import numpy as np

def Soma():
    """Criar um array, preencher e fazer a soma"""

    Numeros = np.array([1,2,3,4,5,6,7,8,9])

    Soma = 0
    for i in Numeros:
        Soma = Soma + i

    print(f"A Soma é: {Soma}")

def Maior_Menor():
    """Criar um array com numeros e apresentar o maior e o menor"""

    Numeros = np.array([12,3,6,1,8,3,5,10])

    Maior = Numeros[0]
    Menor = Numeros[0]

    for i in Numeros:
        if i > Maior:
            Maior = i
        
        if i < Menor:
            Menor = i
    
    print(f"O Maior é {Maior} e o Menor é {Menor}")

def Duplicado():
    """Array com numeros repetidos e retirar os repetidos"""

    Numeros = np.array([2,3,2,6,9,3,1,1,1,134,7,4])
    Numeros2 = np.zeros(len(Numeros))
    Contagem = 0

    for i in Numeros:
        if i not in Numeros2:
            Numeros2[Contagem] = i

            Contagem = Contagem + 1

    for i in Numeros2:
        if i != 0.0:
            print(i)

def Rodar():
    """Rodar todos os numeros de um array para a direita"""
    Numeros = np.array([2,3,2,6,9,3,1,1,1,134,7,4])
    Numeros2 = np.empty(len(Numeros))

    for i in range(len(Numeros)):
        if i != len(Numeros) - 1:
            Numeros2[i + 1] = Numeros[i]
        
        else:
            Numeros2[0] = Numeros[len(Numeros) - 1]

    print(Numeros, Numeros2)

def C_Vogais():
    Palavra = "Olá Mundo"
    Vogais = "aeiouáéíóúàèìòù"
    Contar = 0

    for i in Palavra:
        if i in Vogais or i in Vogais.upper():
            Contar = Contar + 1
    
    print(Contar)

def Palindrome():
    Palavra = "ana"
    Palavra2 = ""

    """for i in range(len(Palavra) - 1, -1, -1):
        Palavra2 = Palavra2 + Palavra[i]"""
    
    Palavra2 = Palavra[::-1]

    if Palavra == Palavra2:
        print("É um palindrome")
