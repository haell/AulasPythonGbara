#Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia():
    numeros = list()
    for _ in range(5):
        numeros.append(randint(0, 10))
    return numeros    

def somaPar(lista):
    soma = 0
    print(f"Valores sorteados: {lista}", end='')
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"\nSoma dos valores PARES: {soma}")

somaPar(sorteia())