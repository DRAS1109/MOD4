"""
O Sr Joaquim tem um restaurante muito popular e precisa de ajuda para gerir a flia de espera dos clientes
Pretende-se criar um programa para registar o nome dos clientes em espera e de cada vez registar o primeiro 
a chegar à fila (FIFO)
Menu: 1.Entrada 2.Saida 3.Consultar fila 4.Terminar
"""

import numpy as np

Menu = """
O que pretende executar?
    1.Entrada
    2.Saida
    3.Consultar Fila
    4.Terminar Programa"""

def Menu():
    MAXClientes = 5
    Fila = np.zeros(MAXClientes, dtype="U20")

    Opção = ""

    while Opção != "4":
        Opção = input(Menu)

        if Opção == "1":
            Entrada(Fila, MAXClientes)
        
        elif Opção == "2":
            Saida(Fila, MAXClientes)

        elif Opção == "3":
            Consultar(Fila, MAXClientes)
        
        elif Opção == "4":
            pass

        else:
            print("Opção inválida")


def Entrada(Fila, MAXClientes):
    Vazios = 0

    for i in Fila:
        if i == "":
            Vazios = Vazios + 1

    if Vazios == 0:
        print("A fila está cheia")
    else:
        E_Nome = input("Qual o nome do cliente? ")
        for Posição in range (MAXClientes):
            if Fila[Posição] == "":
                Fila[Posição] = E_Nome
                return
    

def Saida(Fila, MAXClientes):
    Cheios = 0
    for i in Fila:
        if i != "":
            Cheios += 1
    
    if Cheios == 0:
        print("A fila está vazia")
    
    else:
        print(f"O cliente: {Fila[0]} acabou de sair.")
        for Posição in range(MAXClientes):
            if Posição == MAXClientes - 1:
                return
            
            Fila[Posição] = Fila[Posição + 1]

        Fila[MAXClientes - 2] = ""


def Consultar(Fila, MAXClientes):
    Cheios = 0
    for i in Fila:
        if i != "":
            Cheios += 1
    
    if Cheios == 0:
        print("A fila está vazia")
    
    else:
        if Cheios == MAXClientes:
            print("A fila está cheia")

        print("Na Fila:")
        for Posição in range(MAXClientes):
            if Fila[Posição] != "":
                print(f"{Posição + 1}- {Fila[Posição]}")

if __name__ == "__main__":
    Menu()