# Crie um programa que vai ler vários números e colocar em uma lista.
""" 
# Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
 """
import os
from time import sleep

lista_numero = []
n_elementos_repetidos = n_elementos_digitados = n_elementos_fixados = 0
while True:
    os.system('cls')
    numero = input("\nDigite um valor: ")
    n_elementos_digitados += 1
    if numero.isdigit():
        numero = int(numero)
        if numero not in lista_numero:
            lista_numero.append(numero)
            n_elementos_fixados += 1
        else:
            os.system('cls')
            print(f"{numero} já foi digitado e não será adicionado!")
            n_elementos_repetidos += 1
        while True:
            resp = input("Deseja continuar [S/N]: ").strip().upper() or 'vazio'
            if resp == 'vazio':
                os.system('cls')
                print("O valor não pode ser vazio!\n")
                sleep(1)
            elif resp[0] not in 'SN':
                os.system('cls')
                print("Valor inválido! S para continuar ou N para sair!\n")
                sleep(1)
            else:
                break
        if resp == 'N': 
            break 
    else:
        print("Valor inválido!")
        sleep(1)
lista_numero.sort(reverse=True)
os.system('cls')
cores = [1, 2, 3, 4]
print(f"Você digitou {n_elementos_digitados} elementos.")
print(f"{n_elementos_repetidos} elementos repetidos.")
print(f"Foram adicionados {n_elementos_fixados} elementos não repetidos a lista.")
divisor = '\033[36m=-\033[m'*35
print(divisor)
print(f"Lista com os valores em ordem decrescente: \033[32m>>-\033[4m", end=' ') 
for numero in lista_numero:
    print(f"{numero} ", end='')
print("\033[m\033[32m-->\033[m")
print(divisor)
print(f'O valor \033[32m5\033[m {"consta" if 5 in lista_numero else "não consta"} na lista!')
print('\nFim do programa!')
