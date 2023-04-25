# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
""" 
 Média abaixo de 5.0: REPROVADO

 Média entre 5.0 e 6.9: RECUPERAÇÃO

 Média 7.0 ou superior: APROVADO 
"""

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media_das_notas = (nota_1 + nota_2) / 2

REPROVADO = media_das_notas < 5.0
RECUPERACAO = media_das_notas >= 5.0 and media_das_notas <= 6.99
APROVADO = media_das_notas > 6.99

if REPROVADO :
    print(f'Sua média foi {media_das_notas:.2f} - Você está REPROVADO.')
elif RECUPERACAO :
    print(f'Sua média foi {media_das_notas:.2f} - Você está de RECUPERAÇÃO.')
elif APROVADO:
    print(f'Sua média foi {media_das_notas:.2f} - Você está APROVADO.')

