def Familiares():
    """
    Determina que 2 pessoas são da mesma familia se tiverem o mesmo ultimo nome
    """
    print("Versão 1:")

    Nome1 = input("Introduza o nome completo: ")
    Nome1 = Nome1.strip()

    Nome2 = input("Introduza o nome completo: ")
    Nome2 = Nome2.strip()

    Nome1 = Nome1.split(" ")
    Nome2 = Nome2.split(" ")

    if Nome1[(len(Nome1) - 1)] == Nome2[(len(Nome2) - 1)]:
        print(f"{Nome1[0]} e {Nome2[0]} são da mesma familia")
    
    else:
        print(f"{Nome1[0]} e {Nome2[0]} não são da mesma familia")

def Familiares2():
    """
    Determina que 2 pessoas são da mesma familia se tiverem o mesmo ultimo ou penultimo nome (ordem aleatoria)
    """
    print("Versão 2:")

    Nome1 = input("Introduza o nome completo: ")
    Nome1 = Nome1.strip()

    Nome2 = input("Introduza o nome completo: ")
    Nome2 = Nome2.strip()

    Nome1 = Nome1.split(" ")
    Nome2 = Nome2.split(" ")

    if len(Nome1) != 1 and len(Nome2) != 1:
        if Nome1[(len(Nome1) - 2)] == Nome2[(len(Nome2) - 1)] or Nome1[(len(Nome1) - 1)] == Nome2[(len(Nome2) - 2)] or Nome1[(len(Nome1) - 1)] == Nome2[(len(Nome2) - 1)]:
            print(f"{Nome1[0]} e {Nome2[0]} São da mesma familia")
    
    else:
        print("Para verificar se são familiares introduza pelo menos 2 nomes")

def main():
    Familiares()
    Familiares2()

if __name__ == "__main__":
    main()