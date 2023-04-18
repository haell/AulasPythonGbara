# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

""" tamanho_retas = [4, 2, 7]

print(sorted(tamanho_retas))

#TODO
###Um menu utilizando while para digitar ou usar os valores já existentes no exemplo.###
###Opções poder verificar quantas vezes quiser sem fechar o programa ou encerrar com comando.###

#função que organiza lista recebida e retorna maior número e soma entre os menores.
def _verifica_maior_soma_menores(lista_numeros):
    lista_organizada = sorted(lista_numeros)
    maior = lista_organizada[2]
    soma_menores = lista_organizada[0] + lista_organizada[1]
    print('-'*20)
    print(lista_organizada)
    print('Este é o maior número:', maior)
    print('Este é a soma dos menores números:', soma_menores)
    return maior, soma_menores

#Função que organiza a lista recebida e retorna a diferença entre os menores valores.
def _verifica_diferenca_menores(lista_numeros):
    lista_organizada = sorted(lista_numeros)
    diferenca_menores = lista_organizada[1] - lista_organizada[0]
    print('Este é a diferença entre menores números:', diferenca_menores)
    return diferenca_menores

#Método que verifica se é possível formar triângulo e mostra o resultado no console.
def verifica_se_triangulo():
    maior_numero, soma_menores_numeros = _verifica_maior_soma_menores(tamanho_retas)
    diferenca_menores = _verifica_diferenca_menores(tamanho_retas)
    if maior_numero > diferenca_menores and maior_numero < soma_menores_numeros:
        print(f'Os valores {tamanho_retas} podem formar um triângulo.')
    else:
        print(f'Os valores {tamanho_retas} não podem formar um triângulo.')

#Chamada da função principal
verifica_se_triangulo()
    # print(maior_numero, soma_menores_numeros, diferenca_menores) """
import os

def cabecalho():
    linha1 = '_<^>'*15
    linha2 = '{:^60}'.format('TESTANDO SE FORMA TRIÂNGULO')
    linha3 = '_<^>'*15
    print(linha1)
    print(linha2)
    print(linha3)

cabecalho()
reta_1 = float(input('\nInforme o tamanho da primeira reta: '))
os.system("cls")

cabecalho()
reta_2 = float(input('\nInforme o tamanho da segunda reta: '))
os.system("cls")

cabecalho()
reta_3 = float(input('\nInforme o tamanho da terceira reta: '))
os.system("cls")

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print(f'As retas {reta_1:.0f}, {reta_2:.0f} e {reta_3:.0f}: PODEM formar um triângulo!')
else:
    print(f'As retas {reta_1:.0f}, {reta_2:.0f} e {reta_3:.0f}: NÃO formam um triângulo!')