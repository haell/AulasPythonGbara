# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def cabecalho():
    titulo = '{:^30}'.format("Controle de Terrenos")
    print(titulo)
    print("-"*30)

def pega_largura():
    largura = float(input("LARGURA (m): "))
    return largura

def pega_altura():
    altura = float(input("ALTURA (m): "))
    return altura

def calcula_area_retangulo(a, b):
    resultado = a * b
    return resultado

def exibe_resultado(a, b, r):
    print(f"A área de um terreno {a:.2f}m X {b:.2f}m é igual a {r:.2f}m²")

cabecalho()
a = pega_largura()
b = pega_altura()
r = calcula_area_retangulo(a, b)

exibe_resultado(a, b, r)
