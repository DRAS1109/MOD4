Contar = 0

Email = input("Email: ")
PP = input("Password: ")

if len(PP) >= 8:
    Contar = Contar + 1

if PP not in Email:
    Contar = Contar + 1

for Letra in PP:
    if Letra >= "a" and Letra <= "z":
        Contar = Contar + 1
        break

for Letra in PP:
    if Letra >= "A" and Letra <= "Z":
        Contar = Contar + 1
        break

for Letra in PP:
    if Letra >= "0" and Letra <= "9":
        Contar = Contar + 1
        break

if Contar == 5:
    print("Senha segura")

else:
    print("Senha não é segura")