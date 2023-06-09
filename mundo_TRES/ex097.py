# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def emoldurar(texto):
    moldura = '-'*(len(texto)+4)
    print(moldura)
    t = len(texto)+4
    frase = f'{{:^{t}}}'.format(f"{texto}")
    print(frase)
    print(moldura)

texto = input("Frase: ")
emoldurar(texto)