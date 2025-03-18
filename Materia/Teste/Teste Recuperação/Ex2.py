Telefone = input("Insira o nº de telefone: ")
Valido = True

#Se o nº tem 9 digitos
if len(Telefone) != 9:
    print("Deve ter 9 digitos")
    Valido = False

#Se só tem digitos numericos
for L in Telefone:
    if L < "0" or L > "9":
        print("Só deve ter digitos")
        Valido = False

#Se o numero começa por 91, 92, 93, 96
if Telefone[0] != "9" or Telefone[1] not in "1236":
    print("Deve começar por 91, 92, 93 ou 96")
    Valido = False

#Se o numero (excluindo o indicativo de rede) não tem tudo zeros (0)
Contar = 0
for Pos in range (2, len(Telefone)):
    if Telefone[Pos] == "0":
        Contar += 1
if Contar == 7:
    print("Não pode ser composto só por 0 (depois do indicativo)")
    Valido = False

#Indicar se é valido
if Valido == True:
    print("É válido")