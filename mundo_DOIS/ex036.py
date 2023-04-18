# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

PORCENTAGEM = 0.30

def _trinta_por_cento(salario_bruto):
    limite_parcela = salario_bruto*PORCENTAGEM
    return limite_parcela

def _calcula_valor_parcela(valor_casa, quantos_anos):
    quantidade_meses = quantos_anos*12
    valor_parcela = valor_casa / quantidade_meses
    return quantidade_meses, valor_parcela

def _aprova_emprestimo(salario_bruto, valor_casa, quantos_anos):
    _, valor_parcela = _calcula_valor_parcela(valor_casa, quantos_anos)
    limite_parcela = _trinta_por_cento(salario_bruto)
    
    if valor_parcela > limite_parcela or quantos_anos > 30:
        print('Reprovado!')
    else:
        print('Aprovado!')

def main(salario, valor_casa, quantos_anos):
    while True:

        _aprova_emprestimo(salario, valor_casa, quantos_anos)

        desliga = input('Deseja sair? "Sim" ou "Não": ')
        if "sim" in desliga[0:3].lower():
            break
        

if __name__ == '__main__':
    
    valor_casa = float(input('valor casa: '))
    salario = 1200.01
    quantos_anos = 30
    main(salario, valor_casa, quantos_anos)
