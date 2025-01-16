def Nomes():
    Nome = input("Introduza um nome: ")
    Lista_Nomes = Nome.split(" ")
    
    print(f"{Lista_Nomes[len(Lista_Nomes) - 1]}", end="")

    if (len(Lista_Nomes)) != 1:
        print(",", end=" ")

    for i in range(len(Lista_Nomes) - 1):
        print(f"{Lista_Nomes[i]}", end=" ")

def Nomes2():
    Nome = input("Introduza um nome: ")
    Lista_Nomes = Nome.split(" ")
    
    Nome_Completo = (Lista_Nomes[len(Lista_Nomes) - 1])

    if (len(Lista_Nomes)) != 1:
        Nome_Completo += ", "
 
    for i in range(len(Lista_Nomes) - 1):
        Nome_Completo += (Lista_Nomes[i])
        Nome_Completo += " "

    Nome_Completo = Nome_Completo.strip()

    print(Nome_Completo)

if __name__ == "__main__":
    Nomes()
    Nomes2()