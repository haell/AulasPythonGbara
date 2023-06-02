# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
# import os
# import pyautogui


jogadas = {}
print("Valores sorteados: \n")
for numero in range(4):
    numero_sorteado = randint(1, 6)
    jogador = f"\033[3{numero+2}mJogador {numero+1}\033[m"
    jogadas[jogador] = numero_sorteado

ranking = list()
print("Valores sorteados: ")
for k, v in jogadas.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-'*35)
for i, v in enumerate(ranking):
    print(f"Em {i+1}° Lugar o {v[0]} com {v[1]} pontos.")
    
""" n_vezes = 0
lista_de_cor = []
while n_vezes != 33:
    os.system('cls')

    cor = randint(2, 6)
    lista_de_cor.append(f"\033[3{cor}m▓\033[m")
    resultado = '▓▓▓▓▓'*cor
    print('Calculando', end='')
    print('.'*cor)
    print(f"\033[3{cor}m{resultado}\033[m")
    sleep(0.1)
    n_vezes += 1 
from collections import Counter

ocorrencias = Counter(lista_de_cor)

for elemento, frequencia in ocorrencias.items():
    print(f"A cor {elemento} ocorre {frequencia} vezes no seu dia!")
 """







