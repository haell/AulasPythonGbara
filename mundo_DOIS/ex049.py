# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n1 = int(input('Digite um número e veja a tabuada: '))
""" print('-' * 12)
print('{} x {:2} = {:2}'.format(n1, 1, (n1*1)))
print('{} x {:2} = {:2}'.format(n1, 2, (n1*2)))
print('{} x {:2} = {:2}'.format(n1, 3, (n1*3)))
print('{} x {:2} = {:2}'.format(n1, 4, (n1*4)))
print('{} x {:2} = {:2}'.format(n1, 5, (n1*5)))
print('{} x {:2} = {:2}'.format(n1, 6, (n1*6)))
print('{} x {:2} = {:2}'.format(n1, 7, (n1*7)))
print('{} x {:2} = {:2}'.format(n1, 8, (n1*8)))
print('{} x {:2} = {:2}'.format(n1, 9, (n1*9)))
print('-' * 12) """

for c in range(1, 11):
    print(f'{n1} x {c:2} = {n1*c:2}')

