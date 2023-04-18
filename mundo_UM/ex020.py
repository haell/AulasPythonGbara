import random

a1 = str(input('Digite o nome do 1° aluno: '))
a2 = str(input('Digite o nome do 2° aluno: '))
a3 = str(input('Digite o nome do 3° aluno: '))
a4 = str(input('Digite o nome do 4° aluno: '))
lt = [a1, a2, a3, a4]
random.shuffle(lt)
print('{}\n{}\n{}\n{}'.format(lt[0], lt[1], lt[2], lt[3]))
