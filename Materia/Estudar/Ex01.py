"""
Nivel 1
"""

import numpy as np 

def E01():
    # Criar um array com numeros de 1 a x
    X = int(input("Introduza um Nº inteiro: "))

    Arr = np.empty(X)
    for i in range (X):
        Arr[i] = i + 1  

    print(Arr)

def E02():
    # Exibir o primeiro e o ultimo elememto de um array
    Arr = np.array([10, 20, 30, 40, 50])

    print(Arr[0])
    print(Arr[len(Arr) - 1])

"""
Nivel 2
"""

def E03():
    #Apagar 1 elemento do array
    Arr = np.array([10, 20, 30, 40, 50])

    X = int(input("Introduza um Nº inteiro: "))

    for i in range (X - 1, (len(Arr) - 1)):
        Arr[i] = Arr[i + 1]

    Arr[len(Arr) - 1] = X

    print(Arr)

def E04():
    #Calcular a soma e a media de todos os numeros do array
    Arr = np.array([3, 6, 9, 12, 15])
    Soma = 0

    for i in Arr:
        Soma = Soma + (i)

    print(f"Soma: {Soma} | Media: {Soma / (len(Arr))}")

def E05():
    #Inverter elementos do array
    Arr = np.array([5, 4, 3, 2, 1, 0])

    for i in range(len(Arr) // 2):
        Ultimo = len(Arr) - (i + 1)
        Temp = Arr[i]
        Arr[i] = Arr[Ultimo]
        Arr[Ultimo] = Temp

    print(Arr)

"""
Nivel 3
"""


def E06():
    #Encontrar o 2º maior numero
    Arr = np.array([10, 20, 5, 8, 12])
    Arr = Bubble_Sort(Arr)
    
    print(f"O segundo maior numero é: {Arr[len(Arr) - 2]}") 

def E07():
    #Remover do Array todos os numeros duplicados
    Arr = np.array([1, 2, 2, 3, 3, 4])
    Duplicados = 0
    Posição = -1

    for i in range(len(Arr) - 1):
        if Arr[i] == Arr[i + 1]:
            Duplicados = Duplicados  + 1
    
    Arr2 = np.zeros(len(Arr) - Duplicados)

    for i in range(len(Arr) - 1):
        if Arr[i] != Arr[i + 1]:
            Posição = Posição + 1
            Arr2[Posição] = Arr[i]
    
    Arr2[len(Arr2) - 1] = Arr[len(Arr) - 1]
    
    print(Arr2)

def E08():
    #Multiplicar os elementos do array pelo seu indice
    Arr = np.array([2, 3, 4, 5])
    for i in range(len(Arr)):
        Arr[i] = Arr[i] * i

    print(Arr)

"""
Nivel 4
"""

def E09():
    #Multiplicar os elementos de um array pelo respectivo de outro array
    Arr1 = np.array([1, 2, 3])
    Arr2 = np.array([4, 5, 6])
    Produto = np.zeros(len(Arr1), dtype= "U20")

    for i in range(len(Produto)):
        Produto[i] = f"{Arr1[i]} * {Arr2[i]} = {Arr1[i] * Arr2[i]}"

    print(Produto)

def E10():
    #Rotacionar os elementos de um array para a direita k vezes
    k = 2
    Arr = np.array([1, 2, 3, 4, 5])
    Arr2 = np.zeros(len(Arr))
    Posição = 0

    for i in range(len(Arr)):

        if (i + k) > (len(Arr) - 1):
            i = i - (len(Arr)) + k
        else: 
            i = i + k

        Arr2[i] = Arr[Posição]
        Posição = Posição + 1
    
    print(Arr2)

"""
Funções de ajuda
"""

def Bubble_Sort(Vetor):
    Tamanho  = len(Vetor)
    for i in range(Tamanho):
        for j in range(0, Tamanho - i - 1):
            if Vetor[j] > Vetor[j + 1]:
                Temp = Vetor[j]
                Vetor[j] = Vetor[j + 1]
                Vetor[j + 1] = Temp
    
    return Vetor

E03()