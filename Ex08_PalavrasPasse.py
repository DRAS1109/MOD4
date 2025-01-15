#Programa para dizer se a palavra passe é muito simples

import numpy as np

Password_Proibidas = np.empty(["M3DiA", "12345", "123456", "Password", "Admin"])

Password_Utilizador = input("Introduza a sua palavra passe: ")

if Password_Utilizador in Password_Proibidas:
    print("A sua palavra passe é obvia demais")