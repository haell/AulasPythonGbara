# Crie um programa que leia dois valores e mostre um menu na tela:
""" 
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
 """
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
import os

sair = False
while sair == False:
    primeiro_valor = int(input("PRIMEIRO valor: "))
    segundo_valor = int(input("SEGUNDO valor: "))

    jogo = 0
    while jogo == 0:
        print('-=-'*20)
        print(f'PRIMEIRO -> {primeiro_valor} | SEGUNDO -> {segundo_valor}')
        print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos valores\n[ 5 ] sair do programa")
        opcao =  int(input(">>>>> Qual é a sua opção? "))
        if opcao == 1:
            soma = primeiro_valor + segundo_valor
            print(f"\n\033[4mA soma entre {primeiro_valor} e {segundo_valor} é igual à {soma}\n\033[m")
            sleep(1)
        elif opcao == 2:
            multiplicacao = primeiro_valor * segundo_valor
            print(f"\n\033[4m{primeiro_valor} multiplicado por {segundo_valor} é igual à {multiplicacao}\n\033[m")
            sleep(1)
        elif opcao == 3:
            maior_valor = primeiro_valor if segundo_valor < primeiro_valor else segundo_valor
            print(f"\n\033[4mO maior entre os dois valores é o {maior_valor}\n\033[m")
            sleep(1)
        elif opcao == 4:
            jogo = 1
            sleep(1)
        elif opcao == 5:
            os.system("cls")
            print("Saindo.")
            sleep(1)
            os.system("cls")
            print("Saindo..")
            sleep(1)
            os.system("cls")
            print("Saindo...")
            sleep(1)
            os.system("cls")
            print("\033[1;32mAté a próxima!\033[m")
            jogo = 1
            sair = True
        else:
            print(" Opção inválida! ")