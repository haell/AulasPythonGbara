# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
""" 
 à vista dinheiro/cartão: 10% de desconto

 à vista no cheque: 5% de desconto

 em até 2x no cartão: preço formal 

 3x ou mais no cartão: 20% de juros 
 """
import os

produtos  = {
    'maçã': 7.85,
    'pera': 8.10,
    'uva': 5.44
}

produto = input('Escolha um produto - \033[1;31;40mmaçã\033[m  - \033[1;32;40mpera\033[m  - \033[1;34;40muva\033[m: ')
os.system('cls')

forma_de_pagamento = input('Forma de pagamento: \033[1;36;40m1\033[m-À Vista   \033[1;35;40m2\033[m-Parcelado: ')
os.system('cls')

item = produtos[produto]

if forma_de_pagamento == '1':
    metodo_pagamento = int(input(f'Qual método? \033[1;35;40m1\033[m-Dinheiro   \033[1;36;40m2\033[m-Cartão   \033[1;33;40m3\033[m-Cheque: '))
    if metodo_pagamento == 1 or metodo_pagamento == 2:
        os.system('cls')
        print(f'O valor do Kg de {produto.upper()} é R$ {item}')
        print(f'À vista no dinheiro ou cartão, tem desconto de 10% \nVocê deve pagar = R${item - (item*0.10):.2f}\n')
    elif metodo_pagamento == 3:
        os.system('cls')
        print(f'O valor do Kg de {produto.upper()} é R$ {item}')
        print(f'À vista no cheque, tem desconto de 5% \nVocê deve pagar = R${item - (item*0.05):.2f}\n')
    else: 
        os.system('cls')
        print("Erro: Escolha uma forma de pagamento entre 1 e 3.")
        
elif forma_de_pagamento == '2':
    os.system('cls')
    print('\033[1;31;40mATENÇÃO\033[m\nAcima de 2 vezes tem juros!\n')
    numero_vezes = int(input('Quantas parcelas: '))

    if 0 < numero_vezes <= 2:
        os.system('cls')
        print(f'O valor do Kg de {produto.upper()} é R$ {item:.2f}')
        print(f'Dividido em {numero_vezes} vezes, é sem desconto e sem acrescimo. \nVocê deve pagar {numero_vezes} parcelas de R${(item/numero_vezes):.2f}')
        print(f'Totalizando o valor de R${item:.2f}')
    elif 3 <= numero_vezes <= 12:
        os.system('cls')
        print(f'O valor do Kg de {produto.upper()} é R$ {item:.2f}')
        print(f'Dividido em {numero_vezes} vezes, tem um acrescimo de 20% no valor do produto. \nVocê deve pagar {numero_vezes} parcelas de R${((item + (item*0.2))/numero_vezes):.2f}')
        print(f'Totalizando o valor de R${item + (item*0.2):.2f}')
    else:
        os.system("cls")
        print("ERRO (012): Você só pode dividir de 2 até 12 parcelas.\n")

else:
    print("ERRO (011): Você só pode escolher 1 ou 2")
