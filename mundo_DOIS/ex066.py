# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = quantos_num_digitados = 0
lista_numeros = []

while True:
    valor_digitado = input("Digite um número: [999 para sair] ")
    if int(valor_digitado) == 999:
        break    
    soma += int(valor_digitado)
    quantos_num_digitados += 1
print(f"A soma dos \033[32m{quantos_num_digitados}\033[m valores digitados é: \033[36m{soma}\033[m")


