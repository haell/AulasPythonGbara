# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista_num = [[], []]
for i in range(0, 7):
    while True:
        num = input(f'Digite o {i+1}° valor: ')
        if num.isdigit():
            num = int(num)
            if num % 2 == 0:
                lista_num[0].append(num)
            else:
                lista_num[1].append(num)
            break
        else:
            print("Digite apenas número INTEIRO.")

lista_num[0].sort()
lista_num[1].sort()

print(f"Lista de números PARES: {lista_num[0]}")
print(f"Lista de números ÍMPARES: {lista_num[1]}")
