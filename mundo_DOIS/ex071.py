import os

titulo = '{:^45}'.format("BANCO CEV")
print('='*45)
print(titulo)
print('='*45)

CEDULAS_DISPONIVEIS = [50, 20, 10, 1]
valor_solicitado = ''
nome_sacador = str(input("Qual seu nome? "))

os.system('cls')
print('='*45)
print(titulo)
print('='*45)

if valor_solicitado == '0':
    print(f"\nSr. {nome_sacador}")
    print("Obrigado por usar os nossos serviços!\n")
else:
    while valor_solicitado.isdigit() == False:
        valor_solicitado = input("Que valor você quer sacar? R$ ")
        if valor_solicitado.isdigit() == False:
            print("Valor inválido!\n")
    valor_restante = int(valor_solicitado)
    for cedula in range(len(CEDULAS_DISPONIVEIS)):
        valor_de_saque = valor_restante // CEDULAS_DISPONIVEIS[cedula]
        valor_restante -= valor_de_saque * CEDULAS_DISPONIVEIS[cedula]
        if valor_de_saque > 0:
            print(f"{valor_de_saque} notas de R${CEDULAS_DISPONIVEIS[cedula]}")
    print(f"\nSr. {nome_sacador}")
    print("Obrigado por usar os nossos serviços!\n")
