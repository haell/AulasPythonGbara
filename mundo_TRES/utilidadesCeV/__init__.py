def ln(x='-', y=100):
    print(x*int(y))
    print()


def rotulo(frase='RÓTULO'):
    print(f"-"*(len(frase)+15))
    texto_rotulo = '{:^30}'.format(f'{frase}')
    print(texto_rotulo.upper())
    print(f"-"*(len(frase)+15))