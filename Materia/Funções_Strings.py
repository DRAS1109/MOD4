Texto = "Olá Mundo"

Tamanho = len(Texto) #Nº de Caracacteres da String
print(Tamanho)

Texto = Texto.upper() #Recria a String mas tudo em Maiusculas
print(Texto)

Texto = Texto.lower() #Recria a String mas tudo em Minusculas
print(Texto)

Texto = Texto.capitalize() #Recria a String mas com a 1ª letra em Maiusculas
print(Texto)

Texto = "     Olá Mundo     "
Texto = Texto.strip() #Recria a String sem espaços em branco no Inicio e Final
print(Texto)

Texto = Texto.replace(" ", "-") #Recria a String mas substituindo o 1º parametro pelo 2º 
print(Texto)
Texto = Texto.replace("-", " ")

print(Texto.isdigit()) #Devolve Verdadeiro se todas as letras forem digitos (numeros)

Frase = "Olá Mundo, o computador é uma torradeira"
Palavras = Frase.split(" ") #Divide a Frase em palavras separadas por " " (Espaço)
print(Palavras)

Posição = Frase.index("m") #Devolve a posição do parametro ("m" neste caso), caso não exista da erro
print (Posição)

Posição = Frase.find("k") #Devolve a posição do parametro ("m" neste caso), caso não exista devolve -1

if Posição == -1:
    print("Não foi encontrado")
else:
    print(Posição)

Codigo = ord("a") #Devolve o codigo ascii de uma letra
print(Codigo)

Letra = chr(97) #Devolve a letra da posição ascii correspondente
print(Letra)