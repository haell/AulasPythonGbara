# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
""" 
 Quantidade de notas
 A maior nota
 A menor nota
 A média da turma
 A situação (opcional)
 """

def notas(*nota, sit=False):
    """
Calcula estatísticas das notas fornecidas.

Parâmetros:
- nota (float): Uma ou mais notas a serem consideradas.
- sit (bool): Indica se deve ser calculada a situação do aluno (opcional, padrão: False).

Retorno:
Um dicionário com as seguintes informações:
- 'Total': Total de notas fornecidas.
- 'Maior': Maior nota.
- 'Menor': Menor nota.
- 'Média': Média das notas.
- 'Situação': Situação do aluno (apenas se o parâmetro 'sit' for True).

Exemplo:
>>> notas(7.5, 8.0, 6.5, sit=True)
{
    'Total': 3,
    'Maior': 8.0,
    'Menor': 6.5,
    'Média': 7.333333333333333,
    'Situação': 'BOA'
}

- By Haell
"""

    if not nota:
        return "Digite pelo menos uma nota."
    else:
        lista = list()    
        notas = dict()
        for i in nota:
            lista.append(i)        
        notas['Total'] = len(lista)
        notas['Maior'] = max(lista)
        notas['Menor'] = min(lista)
        notas['Média'] = sum(lista) / len(lista)
        if sit:
            if notas['Média'] >= 9:
                notas['Situação'] = 'ÓTIMA'
            elif notas['Média'] > 7:
                notas['Situação'] = 'BOA'
            elif notas['Média'] >= 5:
                notas['Situação'] = 'REGULAR'
            elif notas['Média'] < 5 :
                notas['Situação'] = 'RUIM'
        return notas

resp = notas(1.5, 1.5, 3)
print(resp)