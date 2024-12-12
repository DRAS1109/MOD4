import numpy as np
"""





U - 
M - datetime
"""

nomes = np.empty(10,dtype="U20") # 10 -> 10 variaveis | dtype="U20" -> Cada variavel com 20 caracteres

for i in range (len(nomes)):
    nomes[i] = input("Introduza o nome: ")

print(nomes)