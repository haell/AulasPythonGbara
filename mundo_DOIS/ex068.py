# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint


def titulo():
    print("=-"*20)
    titulo = '{:^50}'.format("\033[32mVAMOS JOGAR PAR OU IMPAR\033[m")
    print(titulo)
    print("=-"*20)

titulo()
vezes_de_vitoria = 0
while True:
    valor_usuario = input("Diga um valor: ")
    valor_computador = randint(1, int(valor_usuario))
    soma_dos_valores = int(valor_usuario) + int(valor_computador)
    par_ou_impar = 'PAR' if soma_dos_valores % 2 == 0 else 'IMPAR'
    escolha_usuario = input("Par ou Ìmpar? ").upper()
    escolha_computador = 'PAR' if escolha_usuario != 'PAR' else 'IMPAR'

    print('-'*40)
    print(f"Você jogou {valor_usuario} e o computador {valor_computador}.", end=' ')
    print(f"Total {soma_dos_valores} DEU \033[4m{par_ou_impar}\033[m")
    print('-'*40)
    if escolha_usuario == par_ou_impar:
        print("Você \033[32mGANHOU\033[m")
        vezes_de_vitoria += 1
    else:
        print("Você \033[1;31mPERDEU\033[m")
        print("=-"*20)
        print(f"\033[7;367mGAME OVER!\033[m Você venceu {vezes_de_vitoria} vezes.\n")
        break
    


