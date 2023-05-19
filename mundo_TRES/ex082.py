# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
import os


n_digitados = []
n_pares = []
n_impares = []
resp = 'S'
while resp != 'N':
    while True:
        os.system('cls')
        n = input("\nDige um número INTEIRO: ") or 'vazio'
        if n == 'vazio':
            print('\nNão pode ser vazio!')
        elif n.isdigit():
            n_digitados.append(int(n))
            if int(n) % 2 == 0:
                n_pares.append(int(n))
                break
            else:
                n_impares.append(int(n))
                break
        else:
            print("\nValor inválido!")
    while True:
        resp = input("\nDeseja continuar? [S/N]: ").strip().upper() or 'vazio'
        if resp == 'vazio':
            print("\nNão pode ser vazio! Digite  S  ou  N")
        elif resp[0] in 'SN':
            break
        else:
            print("\nValor inválido! Digite  S  ou  N")
print("\nTodos os números:", end=' ')
for n in n_digitados:
    print(f"{n}", end=' ')
print("\nSó os números PARES:", end=' ')
for n in n_pares:
    print(f"{n}", end=' ')
print("\nSó os números IMPARES:", end=' ')
for n in n_impares:
    print(f"{n}", end=' ')
    