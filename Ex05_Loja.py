"""
Este programa deve guardar o nome dos clientes que entraram num determinado dia e o valor das suas compras
No final deve mostrar qual o cliente que mais dinheiro gastou na loja juntamente com o seu nome
"""

import numpy as np

Max_Clientes = int(input("Quantos clientes entraram na loja: "))
Nomes = np.empty(Max_Clientes,dtype="U50")
Compras = np.empty(Max_Clientes, dtype="f")

def main():
    Clientes(Max_Clientes)
    Premiado(Max_Clientes)

def Clientes(Max_Clientes):
    for i in range (Max_Clientes):
        Nomes[i] = input("Introduza o nome do cliente: ")
        Compras[i] = input(f"Quanto o {Nomes[i]} gastou? ")

def Premiado(Max_Clientes):
    Maior = 0
    for N in range (Max_Clientes):
        if Compras[N] > Compras[Maior]:
            Maior = N
    
    print(f"O cliente que mais gastou na loja foi {Nomes[Maior]} e gastou {Compras[Maior]}")

if __name__ == "__main__":
    main()