# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero_inteiro = int(input('Digite um número inteiro: '))
base = input("\033[1;32;40m 1\033[m - binario    \033[1;33;40m 2\033[m - octeto    \033[1;35;40m 3\033[m - hexadecimal\
             \nEscolha a base de conversão: ")
position = int

if numero_inteiro < 0:
    position = 0
else:
    position = 2

def menu(n):

    if n == '1':
        print(f'\nO número {numero_inteiro} em binário é: \033[1;32;40m{str(bin(numero_inteiro)[position:])}\033[m\n')
    elif n == '2':
        print(f'\nO número {numero_inteiro} em octeto é: \033[1;33;40m{str(oct(numero_inteiro)[position:])}\033[m\n')
    elif n == '3':
        print(f'\nO número {numero_inteiro} em hexadecimal é: \033[1;35;40m{str(hex(numero_inteiro)[position:])}\033[m\n')

menu(base)
