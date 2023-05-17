# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_numero = []
while True:
    numero = input("\nDigite um valor: ")
    if numero.isdigit():
        if numero not in lista_numero:
            lista_numero.append(numero)            
        else:
            print(f"{numero} já foi digitado e não será adicionado!")
        while True:
            resp = input("Deseja continuar [S/N]: ").strip().upper() or 'vazio'
            if resp == 'vazio':
                print("O valor não pode ser vazio!\n")
            elif resp[0] not in 'SN':
                print("Valor inválido! S para continuar ou N para sair!\n")
            else:
                break
        if resp == 'N': 
            break 
    else:
        print("Valor inválido!")
lista_numero.sort()
print(f"\nValores digitados:", end=' ') 
for numero in lista_numero:
    print(f"{numero} ", end='') 
print('\nFim do programa!')
