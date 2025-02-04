"""
O cliente insere o dinheiro para comprar (5€), o preco do produto(3€) e depois devolve o troco (2€)
"""

import numpy as np

Disponivel = np.array([[2    , 1], 
                       [1    , 1], 
                       [0.5  , 1], 
                       [0.2  , 1], 
                       [0.1  , 1],
                       [0.05 , 1],
                       [0.02 , 1], 
                       [0.01 , 1]])


Preço = float(input("Quanto custa o produto: "))
Cliente = float(input("Introduza o dinheiro para pagar: "))

Troco = Cliente - Preço

if Troco < 0:
    print("O dinheiro inserido não chega para comprar o produto")


for i in range(Disponivel.shape[0]):
    Moedas = 0
    while Troco - Disponivel[i, 0] >= 0 and Disponivel[i,1] > 0:
        Troco = Troco - Disponivel[i, 0]
        Troco = round(Troco, 2)
        Moedas = Moedas + 1
    
        Disponivel[i,1] = Disponivel[i,1] - 1

    if Moedas != 0:
        print(f"Troco: {Moedas} moedas de {Disponivel[i, 0]}€ ")

if Troco > 0:
    print("Não tenho moedas suficientes para completar o troco.")

print(Disponivel)