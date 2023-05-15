# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

import os


numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
      'seis',  'sete',  'oito',  'nove',  'dez',
          'onze',  'doze',  'treze',  'quatorze',  'quinze',
              'dezesseis',  'dezessete',  'dezoito',  'dezenove',  'vinte'
    )


while True:
    numero = input("Digite um número INTEIRO: ")
    if not numero.isdigit():
        os.system('cls')
        print("\033[31m\nValor inválido!\033[m\n")
        continue
    elif int(numero) > 20:
            os.system('cls')
            print("Digite um valor entre \033[32m0\033[m e \033[32m20\033[m!\n")
            continue
    else:
        os.system('cls')
        numero = int(numero)
        break

print(f"\033[32m{numero}\033[m por extenso é \033[32m{numeros_por_extenso[numero]}\033[m")