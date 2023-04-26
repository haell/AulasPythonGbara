# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
cont = 0
contn = 0
soma = 0
for c in range(0, 6):
    n1 = int(input('Digite um número inteiro:'))
    contn += 1
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print(f"Você informou {contn} números, sendo {cont} números pares cuja soma é: {soma}")