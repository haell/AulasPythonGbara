# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


from datetime import datetime
from ex098 import linha

def calcula_idade(ano=0):
    idade = datetime.today().year - int(ano)
    return idade

def get_ano_nasc():
    while True:
        a_n = input("Em que ano você nasceu: ")
        valido = a_n.isdigit() and len(a_n) == 4 and (
            1900 <= int(a_n) <= datetime.today().year)
        if valido:
            return a_n
        print("Valor inválido!")

def voto(idade):
    situacao = ''
    if idade in range(18, 66):
        situacao = 'É obrigatório'
    elif idade < 16:
        situacao = 'Não Vota.'
    elif idade in range(16, 18) or idade in range(66, 106):
        situacao = 'É opcional'
    else:
        situacao = 'Sabe o que é voto?'
    return f"Com {idade} anos: {situacao}"

if __name__ == '__main__':

    linha()
    idade = calcula_idade(get_ano_nasc())
    print(voto(idade))
