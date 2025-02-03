"""
O cliente insere o dinheiro para comprar (5€), o preco do produto(3€) e depois devolve o troco (2€)
"""

import numpy as np

Disponivel = np.array([[2   , 10], 
                       [1   , 10], 
                       [0.5 , 10], 
                       [0.2 , 10], 
                       [0.1 , 10],
                       [0.05 , 10],
                       [0.02 , 10], 
                       [0.01 , 1000]])


Preço = float(input("Quanto custa o produto: "))
Cliente = float(input("Introduza o dinheiro para pagar: "))

Troco = Cliente - Preço

if Troco < 0:
    print("O dinheiro inserido não chega para comprar o produto")


for i in range(Disponivel.shape[1]):
    while Troco - Disponivel[i, 0] > 0:
        Moedas = 0
        Troco = Troco - Disponivel[i, 0]
        Moedas = Moedas + 1
    print(f"Troco: {Moedas} moedas de {Disponivel[i, 0]}€ ")