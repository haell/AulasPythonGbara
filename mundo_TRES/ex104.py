# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

from ex098 import linha


def leiaInt(texto):
    """
Função para ler um número inteiro a partir de uma entrada do usuário.

Parâmetros:
- texto (str): O texto a ser exibido para solicitar o número inteiro.

Retorno:
- numero (int): O número inteiro lido a partir da entrada do usuário.

Exemplo:
>>> idade = leiaInt("Digite sua idade: ")
Digite sua idade: 25
>>> print(idade)
25

- By Haell
"""

    while True:
        numero = input(texto).strip()
        if numero.isdigit():            
            return numero
        else:
            print("\033[1;31mErro! Digite um número inteiro válido.\033[m")

# Programa principal
linha()
n =  leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número - \033[32m{n}\033[m")