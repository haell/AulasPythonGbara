# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressão = input("Digite uma expressão: ")
abre_p = fecha_p = 0
inválida = False
for l in expressão:
    if l == "(":
        abre_p += 1
    elif l == ")":
        fecha_p += 1
        if fecha_p > abre_p:
            inválida = True
            break
if not inválida and abre_p == fecha_p:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está INCORRETA!')
