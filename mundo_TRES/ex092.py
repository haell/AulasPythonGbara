# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime


pessoa = {}
nome = input("Nome: ")
ano_nascimento = int(input("Ano de Nascimento: "))
carteira_trabalho = int(input("N° da carteira de trabalho: "))
tempo_aposentar = 0
idade_aposentado = 0
if carteira_trabalho != 0:
    ano_contratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: "))
    tempo_aposentar = ano_contratacao + 35
    idade_aposentado = tempo_aposentar - ano_nascimento
    #--------------------------------------------------------------------------------
    pessoa['Nome'] = nome
    pessoa['Idade'] = datetime.datetime.now().year - ano_nascimento
    pessoa['CTPS'] = carteira_trabalho
    pessoa['Salário'] = f"R$ {salario:.2f}"
    pessoa['Ano de aposentadoria'] = tempo_aposentar
    pessoa['Aposentadoria'] = idade_aposentado
    #--------------------------------------------------------------------------------
else:    
    pessoa['Nome'] = nome
    pessoa['Idade'] = datetime.datetime.now().year - ano_nascimento
    pessoa['CTPS'] = "0 'Nunca trabalhou.'"
    #--------------------------------------------------------------------------------
print('-'*45)
for k, v in pessoa.items():
    print(f"- {k} tem o valor {v}")
print('-'*45)
