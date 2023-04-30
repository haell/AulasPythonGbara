# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('-=-' * 20)
print("Vou pensar em um número de 0 a 10, tente adivinhar!")
print('-=-' * 20)
num_usuario = ''#int(input("Digite um número de 0 a 10: ")) # usuário tenta adivinhar
num_computador = 0
while num_usuario != num_computador:
    num_computador = randint(1, 10) # computador gera um número aleatório entre 0 e 5
    num_usuario = int(input("Digite um número de 0 a 10: ")) # usuário tenta adivinhar
    print('Pensando...')
    sleep(2)
    if num_usuario == num_computador:
        print("Pensei no {}, você acertou, PARABÉNS!".format(num_computador))
        break
    else:
        print("Pensei no número {}, você errou, TENTE NOVAMENTE!".format(num_computador))
        