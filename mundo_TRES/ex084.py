# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
""" 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
 """
import os
resp = ''
pessoas = []
pessoas_mais_pesadas = []
pessoas_mais_leves = []
conta_cadastro = 0
while resp != 'sair':
    pessoa = []
    # recebimento dos dados.
    os.system('cls')
    nome = str(input("Digite o nome: "))
    peso = float(input("Qual o peso: "))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa)
    conta_cadastro += 1
    
    # validação de saida.
    resp = str(input('\nDeseja contnuar? [S/N]: ')).strip().upper() or 'vazio'
    if resp == 'vazio':
        print("Por favor, digite S ou N.")
    elif resp[0] in 'NS':
        if resp[0] == 'N':
            resp == 'sair'
            break
    else:
        print("Valor inválido!")

# Inciando maior e menos peso
maior_peso = pessoas[0][1]
menor_peso = pessoas[0][1]

# Teste lógico na lista
for pessoa in pessoas:    
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

# Encontrando as pessoas mais pesadas e mais leves
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        pessoas_mais_pesadas.append(pessoa[0])
    if pessoa[1] == menor_peso:
        pessoas_mais_leves.append(pessoa[0])
os.system('cls')
print(f"Foram cadastradas {conta_cadastro} pessoa(s).")
print(f"O maior peso foi {maior_peso:.1f}Kg: {pessoas_mais_pesadas}")
print(f"O menor peso foi {menor_peso:.1f}Kg: {pessoas_mais_leves}")
print(pessoas)
print("\nFim do programa!")