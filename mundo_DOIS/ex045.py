# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
import os
from random import randint

# Título
print('\033[1;35;40mJO - KEN - PO\033[m\n')

# Opções
print('[ 1 ] PEDRA\n[ 2 ] PEPEL\n[ 3 ] TESOURA')

# Pega escolha do usuário e do computador.
escolha_do_usuario = input('Qual é a sua opção: ')
escolha_do_computador = str(randint(1, 3))

opcoes_do_jogo = {
    '1': 'PEDRA',
    '2': 'PAPEL',
    '3': 'TESOURA',
}

### Animação do print ###
os.system('cls')
linha_jo = '{:^40}'.format('JO')
print(linha_jo)
sleep(1)
os.system('cls')
linha_ken = '{:^40}'.format('KEN')
print(linha_ken)
sleep(1)
os.system('cls')
linha_po = '{:^40}'.format('PO')
print(linha_po)
sleep(0.5)
os.system('cls')
linha_jokenpo = '{:^60}'.format('\033[1;35;40mJO - KEN - PO\033[m\n')
print(linha_jokenpo)
sleep(1)
### = ###

print('\n'+'-*-'*16)
linha_escolha_jogador = '{:^60}'.format(
    f"O JOGADOR escolheu \033[1;32;40m{opcoes_do_jogo[escolha_do_usuario]}\033[m\n")
print(linha_escolha_jogador)

# TODO
# LÓGICA FUNCIONAL


def print_quem_ganha(quem):
    if quem == 'jogador':
        linha_jogador_ganha = '{:^60}'.format("\033[1;32;40mO jogador ganhou!\033[m\n")
        print(linha_jogador_ganha)
    elif quem == 'computador':
        linha_computador_ganha = '{:^60}'.format("\033[1;31;40mO computador ganhou!\033[m\n")
        print(linha_computador_ganha)
    else:
        linha_empate = '{:^60}'.format("\033[1;35;40mDeu empate!\033[m\n")
        print(linha_empate)

if escolha_do_usuario == escolha_do_computador:
    print_quem_ganha("empate")

elif int(escolha_do_usuario) == 3:
    if int(escolha_do_computador) == 2:
        print_quem_ganha('jogador')
    else:
        print_quem_ganha('computador')

elif int(escolha_do_usuario) == 2:
    if int(escolha_do_computador) == 3:
        print_quem_ganha('jogador')
    else:
        print_quem_ganha('computador')

elif int(escolha_do_usuario) == 1:
    if int(escolha_do_computador) == 3:
        print_quem_ganha('jogador')
    else:
        print_quem_ganha('computador')

linha_escolha_computador = '{:^60}'.format(
    f"O COMPUTADOR escolheu \033[1;33;40m{opcoes_do_jogo[escolha_do_computador]}\033[m")
print(linha_escolha_computador)
print('-*-'*16)
