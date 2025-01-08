"""
Agenda de contactos
Programa para criar uma agenda de contactos
Nome
Nº Telefone
Email
"""

import numpy as np

Max_Contactos = 20
Nomes = np.empty(Max_Contactos,dtype="U50")
Contactos = np.empty(Max_Contactos,dtype="U50")
Emails = np.empty(Max_Contactos,dtype="U50")

def main():
    Menu()
    Adicionar()
    Procurar()
    Apagar()

def Menu():
    MenuOpções = """
Introduza a letra correspondente á opção que deseja efetuar: 
    A = Adicionar (Adiciona um novo contacto)
    M = Mostrar (Mostra todos os contactos existentes)
    P = Procurar (Pesquisa um nome e aparece as suas informações)
    Ap = Apagar (Apaga um contacto)
    T = Terminar
    """
    Opção = input(MenuOpções)

    if Opção.upper == "A":
        Adicionar()
    
    elif Opção.upper == "M":
        Mostrar()
    
    elif Opção.upper == "P":
        Procurar()
    
    elif Opção.upper == "AP":
        Apagar()


def Adicionar():
    """
    Pedir o Nome, N Telefone e Email
    """
    Cheios = 0
    for i in range (Max_Contactos):
        if Nomes[i] != "":
            Cheios = Cheios + 1
    
    Nomes[Cheios + 1] = input("Introduza o nome da pessoa que pretende adicionar")
    Contactos[Cheios + 1] = input("Introduza o contacto da pessoa que pretende adicionar")
    Emails[Cheios + 1] = input("Introduza o email da pessoa que pretende adicionar")

def Mostrar():
    """
    Mostrar todos os Nomes guardados
    """
    print("Contactos existentes:")
    for i in range(Max_Contactos):
        print("     ", Nomes[i])

def Procurar():
    """
    Caso procure Jo
    Aparece todos os Nomes com Jo, dá um tab e mostra po N Telefone e Email
    """
    MostrarNome = input("Qual nome pretende ver? ")

    for i in range(Max_Contactos):
        if MostrarNome in Nomes[i]:
            print(Nomes[i], end="   ", Contactos[i], end="   ", Emails[i] )

def Apagar():
    """
    Apaga e todos os contactos seguintes ocupam a posição
    """

if __name__ == "__main__":
    main()