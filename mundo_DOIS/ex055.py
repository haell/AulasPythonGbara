# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 0
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    if peso > maior_peso:
        maior_peso = peso
        if menor_peso == 0:
            menor_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f"\nO maior peso lido foi : {maior_peso}Kg.")
print(f"O menor peso lido foi : {menor_peso}Kg.\n")

