numero = int(input('Digite um  número: '))

if (numero % 2 == 0):
    print(f'O número {numero}, é PAR')
elif (numero % 2 == 1):
    print(f'O número {numero}, é IMPAR')
else:
    print('Digite um número INTEIRO.')