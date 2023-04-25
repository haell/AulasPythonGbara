# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
""" 
EQUILÁTERO: todos os lados iguais

ISÓSCELES: dois lados iguais, um diferente

ESCALENO: todos os lados diferentes
"""
import os


def cabecalho():
    linha1 = '_<^>'*10
    linha2 = '{:^60}'.format('       \033[4;32;40mTESTANDO\033[m \033[4;36;40mSE\033[m \033[4;34;40mFORMA\033[m \033[4;35;40mTRIÂNGULO\033[m')
    linha3 = '_<^>'*10
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

def testa_tipo_triangulo(segmento_1, segmento_2, segmento_3):

    tipo = str
    if segmento_1 == segmento_2 and segmento_2 == segmento_3:
        tipo = 'Equilátero'

    elif segmento_1 != segmento_2 and segmento_2 != segmento_3 and segmento_1 != segmento_3:
        tipo = 'Escaleno'
    
    elif segmento_1 != segmento_2 or segmento_1 != segmento_3:
        tipo = 'Isóceles'
    return tipo


if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print(f'As retas {reta_1:.0f}, {reta_2:.0f} e {reta_3:.0f}: \
\033[1;34;40mPODEM\033[m formar um triângulo do tipo \033[4;33;40m{testa_tipo_triangulo(reta_1, reta_2, reta_3)}\033[m\n')
    
else:
    print(f'As retas {reta_1:.0f}, {reta_2:.0f} e {reta_3:.0f}: \033[1;31;40mNÃO\033[m formam um triângulo!\n')