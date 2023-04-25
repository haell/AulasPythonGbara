# Programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
""" 
Até 9 anos: MIRIM

Até 14 anos: INFANTIL

Até 19 anos: JÚNIOR

Até 25 anos: SÊNIOR

Acima de 25 anos: MASTER
"""
from datetime import date


ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos - categoria MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos - categoria INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos - categoria JÚNIOR')
elif idade <= 25:
    print(f'Você tem {idade} anos - categoria SÊNIOR')
else:
    print(f'Você tem {idade} anos - categoria MASTER')