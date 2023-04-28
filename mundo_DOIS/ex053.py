# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
""" 
APOS A SOPA,
A SACADA DA CASA,
A TORRE DA DERROTA,
O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
 """
frase = input("Digite uma frase: ")
frase_sem_espaço =''.join(frase.split())
frase_ao_contrario = ''
for letra in range(len(frase_sem_espaço)-1, -1, -1):
    frase_ao_contrario += frase_sem_espaço[letra]

print(f'\n\033[1;34m{frase}\033[m Sem espaço: \033[1;32m{frase_sem_espaço}\033[m\n')
print(f'\033[1;32m{frase_sem_espaço}\033[m ao contrário: \033[1;36m{frase_ao_contrario}\033[m\n')

palindromo = f'\033[1;34m{frase}\033[m É um palindromo!\n'
nao_palindromo = f'\033[1;34m{frase}\033[m NÃO é um palindromo!\n'

print(palindromo) if frase_sem_espaço == frase_ao_contrario else print(nao_palindromo)
