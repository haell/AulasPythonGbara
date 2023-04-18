# Um programa que receba um ano qualquer e diga se ele é bissesto ou não.
from datetime import datetime

# ano = 2000 input('Digite o ano: ')
ano_atual = datetime.today().year


continua = True

while continua:
    digita_ano = str(input("Quer digitar o ano?(Responda Sim ou Não) "))
    if digita_ano[0].strip().lower() == "s":
        ano = int(input("Digite o ano: "))
    else:
        ano = ano_atual
    divide_por_4 = (ano % 4) == 0
    divide_por_100 = (ano % 100) == 0
    divide_por_400 = (ano % 400) == 0


    if divide_por_4:
        if divide_por_100 and divide_por_400:
            print(f'O ano {ano} é Bissexto!')
        elif divide_por_100 and not divide_por_400:
            print(f'O ano {ano} não é Bissexto!')
        else:
            print(f'O ano {ano} é Bissexto!')
    else:
        print(f'O ano {ano} não é Bissexto!')

    continua = str(input("Quer continuar, responda sim ou não: "))[0].strip().lower() == "s"