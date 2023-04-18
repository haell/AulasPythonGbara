# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numeros = input('Digite 3 número separados por virgural: ')
# 5, 18, 9
numeros = numeros.split(',')
print(numeros)
menor = int
maior = int

for i, k in enumerate(numeros):
    # k > int(numeros[i])
    if i == 0:
        maior = int(k)
        menor = int(k)
    if int(k) > maior:
        maior = int(k)
    if int(k) < menor:
        menor = int(k)
    print(i, k.strip())

print('-'*20)
print(numeros)
print('Este é o menor número:', menor)
print('Este é o maior número:', maior)