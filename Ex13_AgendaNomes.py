"""
Criar uma agenda que regista os nomes por ordem alfabetica.
Guardar o nome e data de nascimento das pessoas ordenadas por ordem crescente aos nomes
Menu: 1.Adicionar 2.Listar Contactos 3. Pesquisar 4.Terminar
"""
import numpy as np

def Menu():
    MaxContactos = 20
    Nomes = np.zeros(MaxContactos, dtype="U50")
    Datas = np.zeros(MaxContactos, dtype="U50")

    Menu = """
O que pretende executar?
    1.Adicionar
    2.Listar Contactos
    3.Pesquizar
    4.Terminar Programa
"""

    Opção = ""

    while Opção != "4":
        Opção = input(Menu)

        if Opção == "1":
            Adicionar(Nomes, Datas, MaxContactos)
        
        elif Opção == "2":
            Listar(Nomes, Datas, MaxContactos)

        elif Opção == "3":
            Pesquisar(Nomes, Datas, MaxContactos)
        
        elif Opção == "4":
            pass

        else:
            print("Opção inválida")

def Adicionar(Nomes, Datas, MaxContactos):
    Vazios = 0

    for i in Nomes:
        if i == "":
            Vazios = Vazios + 1

    if Vazios == 0:
        print("Excedeu o limite de contactos")

    else:
        Novo_Nome = input("Qual o nome do novo contacto? ")
        Nova_Data = input("Qual a data de nascimento do novo contacto? ")
        if Nomes[0] == "":
            Nomes[0] = f"{Novo_Nome} | {Nova_Data}"

        else:
            for Posição in range (MaxContactos):
                Nome = Nomes.split(" ")
                if Novo_Nome < Nome:
                    break
            
            for i in range(MaxContactos - 2, Posição, -1):
                if Nomes[i] != "":
                    Nomes[i + 1] = Nomes[i]

            Nomes[Posição] = Novo_Nome


def Listar(Nomes, Datas, MaxContactos):
    print(Nomes)

def Pesquisar(Nomes, Datas, MaxContactos):
    pass

if __name__ == "__main__":
    Menu()