# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
import os
import ascii

aviso = '{:^60}'.format("\033[31mATENÇÃO:\033[m Apenas de 1 à 999!")
print(aviso)
cont = 0

PADRAO = 0
opcao = int(input("Digite um número: "))
while opcao != 0:
    os.system('cls')    
    numero = opcao if opcao > PADRAO else PADRAO
    for i in range(1, numero + 1):
            if numero % i == 0:
                print("\033[36m", end=" ")
                cont += 1
            else:
                print("\033[31m",end=" ")
            print(f"{i}", end=" ")
    print(f"\n\n\033[1;36m{numero}\033[m é divisivel pelos números da cor \033[1;36m▓▓▓\033[m")
    print(f"\033[m\nO número \033[1;36m{numero}\033[m foi divisivel \033[1;32m{cont}\033[m vezes!")
    if cont <= 2:
        print(f"E por isso \033[1;36m{numero}\033[m \033[4;32mÉ PRIMO\033[m\n")
    else:
        print(f"E por isso \033[1;36m{numero}\033[m \33[4;31mNÃO É PRIMO\033[m\n")

    opcao = int(input("Dige outro número ou 0 para sair: "))
    if opcao == 0:
        os.system('cls')    
        url = 'https://img2.gratispng.com/20180409/peq/kisspng-emoji-ok-emoticon-sticker-gesture-hand-emoji-5acbce7d4151d7.9497478815233061092676.jpg'

        output = ascii.loadFromUrl(url)
        saida = '{:^60}'.format(output)
        print(output)
     
