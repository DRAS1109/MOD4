"""
O partido comunista Chines pediu um codigo para trocar palavras proibidas pelo seu inverso. Ex: Pessimo -> Otimo
"""

import numpy as np

Proibidas = np.array(["mau", "pobre", "infeliz", "péssimo", "horrivel"])
Alternativas = np.array(["bom", "rico", "feliz", "otimo", "perfeito"])

Frase = input("Introduza uma frase que expresse o que sente pelo partido comunista: ")

for i in range(len(Proibidas)):
    Frase = Frase.replace(Proibidas[i], Alternativas[i])
    
print(f"Não quis dizer '{Frase}'?")