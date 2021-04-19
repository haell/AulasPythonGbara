# O usuário deverá acertar o número escolhido pelo computador.

from random import randint
from time import sleep

print('-=-' * 20)
print("Vou pensar em um número de 0 a 5, tente adivinhar!")
num_computador = randint(0, 5) # computador gera um número aleatório entre 0 e 5
print('-=-' * 20)
num_usuario = int(input("Digite um número de 0 a 5: ")) # usuário tenta adivinhar
print('Pensando...')
sleep(2)
if num_usuario == num_computador:
    print("Pensei no {}, você acertou, PARABÉNS!".format(num_computador))
else:
    print("Pensei no número {}, você errou, TENTE NOVAMENTE!".format(num_computador))

