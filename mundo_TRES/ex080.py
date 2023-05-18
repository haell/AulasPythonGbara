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
