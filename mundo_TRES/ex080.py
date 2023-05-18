# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

valores = list()
while len(valores) < 5:
    valor = input("Digite um valor: ")
    if valor.isdigit():
        valor = int(valor)
        if len(valores) == 0:
            valores.append(valor)
            print(f"Valor adicionado a lista vazia...")
            continue
        for i, v in enumerate(valores):
            if valor <= v:
                valores.insert(i, valor)
                print(f"Valor adicionado na posição {i}...")
                break
        else:
            valores.append(valor)
            print(f"Valor adicionado ao final da lista...")
    else:
        print("Valor inválido\n")
print(valores)


# Aplicando o metódo do professor para simples comparação.
""" 
lista2 = []
cont_elementos = 0
for c in range(0, 5):
    n = int(input("Digite um número: "))
    cont_elementos += 1
    if c == 0 or n > lista2[-1]:
        lista2.append(n)
        print(f"{n} foi adicionado na posiçao {c}")
    else:
        pos = 0
        while pos < len(lista2):
            if n < lista2[pos]:
                lista2.insert(pos, n)
                print(f"{n} foi adicionado na posição {pos}")
                break
            pos += 1
    faltam = "nenhum" if cont_elementos == 5 else "mais um" if cont_elementos == 4 else 5 - cont_elementos
    print(f"Lista com {cont_elementos} elemento(s): {lista2} - faltam {faltam}.")
print(f"Fim do programa!")
"""