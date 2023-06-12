# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
from ex098 import linha


def gera_param(qtd_digitos):
    from random import randint
    numeros = list()
    for i in range(int(qtd_digitos)):
        n = randint(0, 100)
        numeros.append(n)
    return numeros


def maior(*param):        
    print(f"Analisando os valores passados...")
    if not param or not param[0]:
        sem_valor = 'Foi informado 0 ou nenhum valor.'    
        print(sem_valor)
    else:
        for i in param[0]:
            print(f"{i}", end=' ')
            sleep(0.5)
        maior_valor = max(param[0])

        print(f"Foram informados {len(param[0])} valores ao todo.")    
        print(f"O maior valor informado foi {maior_valor}")
        linha()

maior(gera_param(6))
sleep(0.5)
maior(gera_param(3))
sleep(0.5)
maior(gera_param(2))
sleep(0.5)
maior(gera_param(1))
sleep(0.5)
maior()
