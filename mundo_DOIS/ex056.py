# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
média_idade = 0
nome_homem = str
homem_mais_velho = 0
mulher_menos_20 = 0
for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    soma_idade += idade
    média_idade = soma_idade / p
    if sexo == 'M':
        if int(idade) > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem = nome
    if sexo == 'F':
        if idade < 20:
            mulher_menos_20 +=1 

print(f"A média de idade do grupo é de {média_idade:.2f} ")
print(f"O homem mais velho tem {homem_mais_velho} anos e se chama {nome_homem}")
print(f"Ao todo são {mulher_menos_20} mulheres com menos de 20 anos.")
              
