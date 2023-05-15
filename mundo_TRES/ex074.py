# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint


valores_sorteados = ()

for c in range(0, 5):
    n = randint(1, 10)
    valores_sorteados += (n,)

cont = 0
print(f"O valores sorteados foram: ", end='')
for p in valores_sorteados:
    cont += 1
    print(f"\033[3{cont}m{p}", end=' \033[m')

tupla_ordenada = sorted(valores_sorteados) # Necessário para a minha solução de imprimir.

# minha solução.
""" print(f"\nO maior valor sorteado foi \033[1;36m{tupla_ordenada[-1]}\033[m")
print(f"O menor valor sorteado foi \033[1;37m{tupla_ordenada[0]}\033[m") """

# solução do professor.
print(f"\nO \033[4mmaior\033[m valor sorteado foi \033[1;36m{max(valores_sorteados)}\033[m")
print(f"O \033[4mmenor\033[m valor sorteado foi \033[1;32m{min(tupla_ordenada)}\033[m")
