import numpy
import numpy as np

def Definido():
    numeros = numpy.array([10,14,-5,33,120])
    for i in range (5):
        print (numeros[i])

    array_0d = numpy.array(40) #Criar um Array com 1 variavel

    print(type(numeros)) #Tipo de array
    print(type(array_0d)) #Tipo de Array
    print(array_0d) #O que está no array

    print(numeros.ndim) #Nº de dimenções do Array

    for X in numeros:   #Imprimir todas as variaveis do Array
        print(X)

    for j in range (len(numeros)):  #Imprimir todas as variaveis do Array
        print(numeros[j])


def Indefinido():
    #Criar um array vazio
    Vazio = np.empty(10)
    print (Vazio)

    #Criar um array com zeros
    Array_a_Zeros = np.zeros(10)
    print (Array_a_Zeros)