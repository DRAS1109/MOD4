"""
Agenda de contactos
Programa para criar uma agenda de contactos
Nome
Nº Telefone
Email
"""

import numpy as np

Max_Contactos = 20
Nr_Contactos = 0
Nomes = np.empty(Max_Contactos,dtype="U50")
Contactos = np.empty(Max_Contactos,dtype="U9")
Emails = np.empty(Max_Contactos,dtype="U50")

def AtualizarC():
    global Nr_Contactos
    Nr_Contactos = 0

    for i in range (Max_Contactos):
        if Nomes[i] != "":
            Nr_Contactos = Nr_Contactos + 1

    return Nr_Contactos

def main():
    Menu()

def Menu():
    MenuOpções = """
Introduza a letra correspondente á opção que deseja efetuar: 
    A = Adicionar (Adiciona um novo contacto)
    M = Mostrar (Mostra todos os contactos existentes)
    P = Procurar (Pesquisa um nome e aparece as suas informações)
    Ap = Apagar (Apaga um contacto)
    E = Editar (Edita um contacto)
    T = Terminar
    """
    Opção = "L"

    while Opção.upper() != "T":
        AtualizarC()
        Opção = input(MenuOpções)

        if Opção.upper() == "A":
            Adicionar()
        
        elif Opção.upper() == "M":
            Mostrar()
        
        elif Opção.upper() == "P":
            Procurar("Qual nome pretende ver? ")
        
        elif Opção.upper() == "AP":
            Apagar()
        
        elif Opção.upper() == "E":
            Editar()


def Adicionar():
    """
    Pedir o Nome, N Telefone e Email
    """

    if Nr_Contactos == Max_Contactos:
        print("A agenda de contactos está cheia")
        return 

    Temporario = input("Introduza o nome da pessoa que pretende adicionar: ")
    Nomes[Nr_Contactos] = Temporario.strip()

    Temporario = input("Introduza o contacto da pessoa que pretende adicionar: ")
    Contactos[Nr_Contactos] = Temporario.strip()

    Temporario = input("Introduza o email da pessoa que pretende adicionar: ")
    Emails[Nr_Contactos] = Temporario.strip()
    
def Mostrar():
    """
    Mostrar todos os Nomes guardados
    """

    print("Contactos existentes:")
    for i in range(Nr_Contactos):
        #if Nomes[i] != "":
        print("     ", Nomes[i])

def Procurar(Ação):
    """
    Caso procure Jo
    Aparece todos os Nomes com Jo, dá um tab e mostra po N Telefone e Email
    """

    MostrarNome = input(Ação)

    for i in range(Nr_Contactos):
        if MostrarNome in Nomes[i]:
            print(f"    {Nomes[i]}\t       {Contactos[i]}\t       {Emails[i]}\t")

def Apagar():
    """
    Apaga e todos os contactos seguintes ocupam a posição
    """

    Procurar("Procure o contacto: ")

    ApagarNome = input("Qual contacto pretende apagar? (Digite cancelar para cancelar a ação) ")
    if ApagarNome.lower() == "cancelar":
        return
    
    else:
        Confirmação = input("Tem certeza que pretende Eliminar o contacto? (S/N) ")
        if Confirmação.lower() in "s":
            for N in range(Nr_Contactos):
                if ApagarNome == Nomes[N]:
                    Nomes[N] = ""
                    Contactos[N] = ""
                    Emails[N] = ""

                if N == Max_Contactos - 1:
                    break                

                Nomes[N] = Nomes[N+1]
                Contactos[N] = Contactos[N+1]
                Emails[N] = Emails[N+1]

def Editar():
    """
    Procura o nome, procura o que pretende editar, edita
    """
    Procurar("Procure o contacto: ")

    EditarNome = input("Qual contacto pretende editar? (Digite 'cancelar' para cancelar a ação)")
    if EditarNome.lower() == "cancelar":
        return

    for N in range(Nr_Contactos):
        if EditarNome == Nomes[N]:
            break

    Ação = input("O que pretende editar? (Nome, Contacto, Email) ")

    Confirmação = input("Tem certeza que pretende Editar o contacto? (S/N) ")
    if Confirmação.lower() in "s":
        if Ação.lower() == "nome":
            Temporario = input("Insira o novo nome: ")
            Nomes[N] = Temporario.strip()

        elif Ação.lower() == "contacto":
            Temporario = input("Insira o novo contacto: ")
            Contactos[N] = Temporario.strip()

        elif Ação.lower() == "email":
            Temporario = input("Insira o novo email: ")
            Emails[N] = Temporario.strip()


if __name__ == "__main__":
    main()