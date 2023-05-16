# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

while True:
    lista_valores = []
    maior_valor = 0
    menor_valor = 0
    while len(lista_valores) < 5:
        valor = input("Digite um valor: ")
        if valor.isdigit():
            lista_valores.append(valor)
            if maior_valor == 0:
                maior_valor = valor
                menor_valor = valor
            else:
                if int(valor) > int(maior_valor):
                    maior_valor = valor
                if int(valor) < int(menor_valor):
                    menor_valor = valor
        else:
            print("Valor inválido!\n")
    print(f" Valores digitados: {lista_valores}")
    for p, n in enumerate(lista_valores):
        if n == menor_valor:
            print(f"Menor valor digitado: Indice {p} -> Valor: {n}")
        if n == maior_valor:
            print(f"Maior valor digitado: Indice {p} -> Valor: {n}")    
    break
print("Fim do programa")
