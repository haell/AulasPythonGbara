# Ler um número de 0 a 9999
# Mostrar digitos separados e classificar por posição.

while True:
    try:
        num = int(input('Digite um número inteiro entre 0 e 9999: '))
        if not 0 <= num <= 9999:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)  # Quando substituo por mensagem, o programa quebra.
num1 = str(num+10000) #convertendo para string
print('Unidade: {}'.format(num1[4]))
print('Dezena : {}'.format(num1[3]))
print('Centena: {}'.format(num1[2]))
print('Milhar : {}'.format(num1[1]))
