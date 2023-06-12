# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
""" 
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
 """

from time import sleep

def linha():
    print()
    print('-='*36)

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}: ")
    if passo == 0:
        passo = 1
    if fim < inicio and passo > 0:
        for n in range(inicio, fim-1, -passo):
            print(n, end=' ', flush=True)
            #sleep(0.45)
    for n in range(inicio, fim+1, passo):
        print(n, end=' ', flush=True)
        #sleep(0.45)
    linha()    

contador(1,10,1)

contador(10, 0, -2)

print("Agora é a sua vez de personalizar a contagem: ")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: ") or 1) 
    

contador(inicio, fim, passo)