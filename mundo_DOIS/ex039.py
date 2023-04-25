# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime


ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = datetime.now().year
idade_individuo = ano_atual - ano_nascimento
IDADE_ALISTAMENTO = 18

diferença_de_tempo = idade_individuo - IDADE_ALISTAMENTO

print(f'Você está com {idade_individuo} anos.\n')

if idade_individuo > IDADE_ALISTAMENTO:
    print(f'Você está com \033[1;33;40m{diferença_de_tempo}\033[m ano(s) a mais que a idade de alistamento')
elif idade_individuo < IDADE_ALISTAMENTO:
    print(f'Faltam \033[1;33;40m{-diferença_de_tempo}\033[m ano(s) para a idade de alistamento')
elif idade_individuo == IDADE_ALISTAMENTO:
    print(f'Você deve se alistar ainda este ano!, ({ano_atual})')
else:
    print('Idade inválida!')