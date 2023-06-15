# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#   o primeiro que indique o número a calcular e outro chamado show,
#   que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from ex098 import linha

def fatorial(numero=1, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
        - numero (int): O número para o qual o fatorial será calculado.
        - show (bool): Indica se os passos da fatoração devem ser exibidos.

    Retorna:
        int: O resultado do fatorial.

    """
    fator = 1
    for contador in range(numero, 0, -1):
        fator *= contador
        if show:
            if contador == 1:
                print(f"{contador}", end=' = ')
            else:            
                print(f"{contador}", end=' X ')
    return fator

# Programa principal
linha()
print(fatorial(5))