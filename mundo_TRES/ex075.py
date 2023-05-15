# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
""" 
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""
valores = ()
n_pares = ()
cont_9 = 0
while True:
    while True:        
        n = input("Digite um número ou zero para sair: ")
        if n.isdigit():
            break
        else:
            print("Valor inválido")
    nI = int(n)
    if nI == 0: break

    if nI == 9: cont_9 += 1

    if nI % 2 == 0: n_pares += (n,)

    valores += (n,)
    
    if len(valores) == 4:
        print(f"Você digitou os valores {valores}")
        break
    
if not '0' in valores:
    print(f"\nO número 9 apareceu {cont_9} vez(es)." if cont_9 > 0 else "O número 9 não foi digitado." )
    print(f"O primeiro valor 3 foi digitado na posição {valores.index('3')+1}" if '3' in valores else "Não foi digitado o número 3")
    if len(n_pares) > 0:
        print(f"Números PARES: {sorted(n_pares)}\n")
    else:
        print(f"Nenhum número é PAR.")
