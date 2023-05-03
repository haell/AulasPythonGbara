# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-'*30)
titulo = '{:^30}'.format('SEQUÊNCIA FIBONACCI')
print(titulo)
print('-'*30)
quantos_termos = int(input("\nQuantos termos você quer mostrar? "))

termo_anterior = 0
termo_atual = 1
proximo_termo = 0
cont = 3

print('~'*(quantos_termos*3))
print(f"{termo_anterior} {termo_atual}", end=' ')

while cont < quantos_termos + 1:
    proximo_termo = termo_anterior + termo_atual
    print(proximo_termo, end=' ')
    termo_anterior, termo_atual = termo_atual, proximo_termo    
    cont += 1
print("\n"+'~'*(quantos_termos*3))