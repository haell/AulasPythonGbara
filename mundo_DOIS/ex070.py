# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
""" 
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
 """
import os


titulo = '{:-^60}'.format(" CADASTRAR PRODUTO ")
print(titulo)

total_compra = quantos_mais_1000 = mais_barato = 0
produto_mais_barato = ' '

while True:
    produto = str(input("\nNome do produto: "))
    preço = float(input("Preço: "))
    # ----------------------------------------------------------- #
    if mais_barato == 0 or mais_barato > preço:
        mais_barato = preço
        produto_mais_barato = produto
    if preço > 1000:
        quantos_mais_1000 += 1      
    total_compra += preço
    # ----------------------------------------------------------- #
    sair = ' '
    while sair not in 'SN':
        sair = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if sair != '' and sair.isalpha():
        if sair == 'N':
            break
os.system('cls')
print(f"\n\033[32m{quantos_mais_1000}\033[m dos podutos custam mais de R$1000,00!")
print(f"\033[4;36m{produto_mais_barato.capitalize()}\033[m é o produto mais barato. Valor: R${mais_barato:.2f}")
print(f"Valor total da compra: \033[1;34mR${total_compra:.2f}\033[m")
        
