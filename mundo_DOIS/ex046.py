# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from os import system
from time import sleep


for c in range(10, -1, -1):
    linha = '{:^60}'.format(f'{c}')
    print(linha)
    sleep(1)
    system('cls')

z = 0
while z < 10:
    n = 0
    for e in range(0, 20):
        linha = '{:^60}'.format('*'*(n-6))
        print(linha)
        linha = '{:^60}'.format('*'*(n-4))
        print(linha)
        linha = '{:^60}'.format('*'*(n-2))
        print(linha)
        linha = '{:^60}'.format('*'*n)
        print(linha)
        linha = '{:^60}'.format('*'*(n-2))
        print(linha)
        linha = '{:^60}'.format('*'*(n-4))
        print(linha)
        linha = '{:^60}'.format('*'*(n-6))
        print(linha)
        n += 1
        system('cls')
    z += 1