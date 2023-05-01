# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

número = int(input("Digite um número: "))
contador = número
fator = 1

print(f"{número}! ->", end=' ')
while contador > 0:
    print(f"{contador}", end='')
    tela = ' x '  if contador > 1 else " = "
    print(tela, end='')
    fator *= contador
    contador -= 1
print(fator)
