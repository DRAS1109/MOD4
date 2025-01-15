import numpy as np
Nomes = np.array(["Joaquim", "Mariana", "António", "Mario","Miguel"])

#Mostrar todos os nomes por ordem inversa
print(Nomes[::-1])

#Mostrar os 2 ultimos nomes
print(Nomes[(len(Nomes) - 2):])

#Mostrar o 1ª, o 3ª e o 5ª
print(Nomes[::2])