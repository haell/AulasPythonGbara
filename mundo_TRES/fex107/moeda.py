def aumentar(preco = 0, taxa = 0):
    """
    Função para aumentar um valor em 1.

    Parâmetros:
    - preco (float): O valor a ser aumentado.

    Retorno:
    - O valor aumentado em 1.
    """
    resultado = preco + (preco * taxa /100)
    return resultado


def diminuir(preco = 0, taxa = 0):
    """
    Função para diminuir um valor em 1.

    Parâmetros:
    - preco (float): O valor a ser diminuído.

    Retorno:
    - O valor diminuído em 1.
    """
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(preco = 0):
    """
    Função para calcular o dobro de um valor.

    Parâmetros:
    - preco (float): O valor a ser dobrado.

    Retorno:
    - O dobro do valor.
    """
    resultado = preco * 2
    return resultado


def metade(preco = 0):
    """
    Função para calcular a metade de um valor.

    Parâmetros:
    - preco (float): O valor a ser dividido pela metade.

    Retorno:
    - A metade do valor.
    """
    resultado = preco / 2
    return resultado

def moeda(preco = 0, simbolo = 'R$'):
    return f'{simbolo}{preco: .2f}'.replace('.',',')