"""
Criar uma agenda que regista os nomes por ordem alfabetica.
Guardar o nome e data de nascimento das pessoas ordenadas por ordem crescente aos nomes
Menu: 1.Adicionar 2.Listar Contactos 3. Pesquisar 4.Terminar
"""
import numpy as np

def Menu():
    MaxContactos = 20
    Contactos = np.zeros(MaxContactos, dtype="U50")

    Menu = """
O que pretende executar?
    1.Adicionar
    2.Listar Contactos
    3.Pesquisar
    4.Terminar Programa
"""

    Opção = ""

    while Opção != "4":
        Opção = input(Menu)

        if Opção == "1":
            Adicionar(Contactos, MaxContactos)
        
        elif Opção == "2":
            Listar(Contactos)

        elif Opção == "3":
            Pesquisar(Contactos)
        
        elif Opção == "4":
            pass

        else:
            print("Opção inválida")

def Adicionar(Contactos, MaxContactos):
    Vazios = 0

    for i in Contactos:
        if i == "":
            Vazios = Vazios + 1

    if Vazios == 0:
        print("Excedeu o limite de contactos")

    else:
        Novo_Nome = input("Qual o nome do novo contacto? ")
        Nova_Data = input("Qual a data de nascimento do novo contacto? ")
        if Contactos[0] == "":
            Contactos[0] = f"{Novo_Nome} | {Nova_Data}"

        else:
            for Posição in range (MaxContactos):
                Nome = Contactos[Posição]
                if Nome=="":
                    break
                Nome = Nome.split(" | ")
                if Novo_Nome < Nome[Posição]:
                    break
            
            for i in range(MaxContactos - 1, Posição , -1):
                if Contactos[i] != "":
                    Contactos[i] = Contactos[i-1]

            Contactos[Posição] = f"{Novo_Nome} | {Nova_Data}"


def Listar(Contactos):
    for Nome in Contactos:
        if Nome != "":
            Partes = Nome.split(" | ")
            print(f"Nome: {Partes[0]} | Data de Nascimento: {Partes[1]}")

def Pesquisar(Contactos):
    NomeP = input("Qual nome pretende porcurar? ")
    Primeiro = 0
    Ultimo = 0

    for k in Contactos:
        if k == "":
            break

        Ultimo = Ultimo + 1

    while Primeiro <= Ultimo:
        Meio = (Primeiro + Ultimo) // 2
        Valor_Meio = Contactos[Meio]
        if NomeP in Valor_Meio:
            print(f"Contacto encontrado: {Valor_Meio}")
            return

        elif Valor_Meio < NomeP:
            Primeiro = Meio + 1
        
        else:
            Ultimo = Meio - 1
    print(f"O contacto {NomeP} não existe")

if __name__ == "__main__":
    Menu()