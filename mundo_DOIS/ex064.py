# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
lista_numeros_digitados = []
soma = 0

while numero != 999:
    inteiro = int(input("Digite um número: "))
    if inteiro != 999:
        lista_numeros_digitados.append(inteiro)
        soma += inteiro    
    numero = inteiro

# print(f"Números digitados: {lista_numeros_digitados}")
print(f"Soma de todos os {len(lista_numeros_digitados)} números digitados: {soma}")