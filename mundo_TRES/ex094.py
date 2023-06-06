# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

import os


sair = False
cont = 0
grupo_pessoas = list()

while sair != 'N':    
    pessoa = dict()    
    pessoa['nome'] = input(f"Nome da {cont+1}ª pessoa: ")    
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper() or 'vazio'
        if sexo[0] in 'MF':
            pessoa['sexo'] = sexo[0]
            break
        print("Erro! Digite M ou F")

    while True:
        idade = input("Idade: ")
        if idade.isdigit():
            pessoa['idade'] = idade
            break
        else: print("Digite um valor válido!")
    
    grupo_pessoas.append(pessoa)
    cont += 1
    
    while True:
        sair = input("Cadastrar nova pessoa? ").strip().upper() or 'S'
        if sair[0] in 'SN':
            break
        print("Erro! Responda apenas S ou N")

print(grupo_pessoas)
soma_idade = 0
mulheres = list()
idade_acima_media = list()
for pessoa in grupo_pessoas:
    soma_idade += int(pessoa['idade'])
    media_idade = soma_idade / cont
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    if int(pessoa['idade']) > media_idade:
        idade_acima_media.append(pessoa['nome'])

os.system('cls')
print(f"Foram cadastradas {cont} pessoas.")
print(f"A média de todas as idades é: {media_idade:.0f}")
print(f"Lista de mulheres: {mulheres}")
print(f"Pessoas com idade acima da média: {idade_acima_media}\n")
