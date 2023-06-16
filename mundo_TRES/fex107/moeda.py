def aumentar(preco, taxa):
    """
    Função para aumentar um valor em 1.

    Parâmetros:
    - preco (float): O valor a ser aumentado.

    Retorno:
    - O valor aumentado em 1.
    """
    resultado = preco + (preco * taxa /100)
    return resultado


def diminuir(preco, taxa):
    """
    Função para diminuir um valor em 1.

    Parâmetros:
    - preco (float): O valor a ser diminuído.

    Retorno:
    - O valor diminuído em 1.
    """
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(preco):
    """
    Função para calcular o dobro de um valor.

    Parâmetros:
    - preco (float): O valor a ser dobrado.

    Retorno:
    - O dobro do valor.
    """
    resultado = preco * 2
    return resultado


def metade(preco):
    """
    Função para calcular a metade de um valor.

    Parâmetros:
    - preco (float): O valor a ser dividido pela metade.

    Retorno:
    - A metade do valor.
    """
    resultado = preco / 2
    return resultado

