# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('-=-' * 20)
print("Vou pensar em um número de 0 a 10, tente adivinhar!")
print('-=-' * 20)
num_usuario = ''#int(input("Digite um número de 0 a 10: ")) # usuário tenta adivinhar
num_computador = 0
mais_numero = 0
menos_numero = 0
conte = 0
num_computador = randint(0, 10) # computador gera um número aleatório entre 0 e 10
while num_usuario != num_computador:
    conte += 1
    num_usuario = int(input("Digite um número de 0 a 10: ")) # usuário tenta adivinhar
    print('Pensando...\n')
    sleep(1)
    if num_usuario < num_computador:
        print(f'Mais... Tente outra uma vez!\n')                
    elif num_usuario > num_computador:
        print(f'Menos... Tente outra uma vez!\n')                
    elif num_usuario == num_computador:
        print("Pensei no {}, você acertou na \033[1m{}ª\033[m tentativa, \033[1;32mPARABÉNS!\033[m\n".format(num_computador, conte))
        break
