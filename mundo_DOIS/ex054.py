# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

conte_anos = 0
maior_de_idade = 0
menor_de_idade = 0

for c in range(1, 8):
    ano_de_nascimento = int(input(f"Em que ano a {c}ª pessoa nasceu? "))
    conte_anos += 1
    idade = date.today().year - ano_de_nascimento
    if idade < 18:
        menor_de_idade += 1
    else:
        maior_de_idade += 1

print(f"\nAo todo tivemos {maior_de_idade} pessoas \033[7;30mmaiores\033[m de idade.")
print(f"E também tivemos {menor_de_idade} pessoas \033[7;30mmenores\033[m de idade.\n")