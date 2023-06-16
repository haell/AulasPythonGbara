from utilidadesCeV import rotulo, ln
from rich import print


def aumentar(preco=0, taxa=0, formato=False):
    """
    Aumenta o preço pelo valor da taxa informada.

    Args:
        preco (float): O preço original.
        taxa (float): A taxa de aumento a ser aplicada.
        formato (bool, opcional): Se True, formata o resultado como uma string monetária.

    Returns:
        float ou str: O resultado do aumento, ou a string monetária formatada, se formato for True.

    Examples:
        >>> aumentar(100, 10)
        110.0
        >>> aumentar(100, 10, True)
        'R$ 110,00'

    By Haell
    """
    resultado = preco + (preco * taxa / 100)
    return resultado if not formato else moeda(resultado)


def diminuir(preco=0, taxa=0, formato=False):
    """
    Diminui o preço pelo valor da taxa informada.

    Args:
        preco (float): O preço original.
        taxa (float): A taxa de redução a ser aplicada.
        formato (bool, opcional): Se True, formata o resultado como uma string monetária.

    Returns:
        float ou str: O resultado da redução, ou a string monetária formatada, se formato for True.

    Examples:
        >>> diminuir(100, 10)
        90.0
        >>> diminuir(100, 10, True)
        'R$ 90,00'

    By Haell
    """
    resultado = preco - (preco * taxa / 100)
    return resultado if not formato else moeda(resultado)


def dobro(preco=0, formato=False):
    """
    Calcula o dobro do preço.

    Args:
        preco (float): O preço original.
        formato (bool, opcional): Se True, formata o resultado como uma string monetária.

    Returns:
        float ou str: O dobro do preço, ou a string monetária formatada, se formato for True.

    Examples:
        >>> dobro(100)
        200.0
        >>> dobro(100, True)
        'R$ 200,00'

    By Haell
    """
    resultado = preco * 2
    return resultado if not formato else moeda(resultado)


def metade(preco=0, formato=False):
    """
    Calcula a metade do preço.

    Args:
        preco (float): O preço original.
        formato (bool, opcional): Se True, formata o resultado como uma string monetária.

    Returns:
        float ou str: A metade do preço, ou a string monetária formatada, se formato for True.

    Examples:
        >>> metade(100)
        50.0
        >>> metade(100, True)
        'R$ 50,00'

    By Haell
    """
    resultado = preco / 2
    return resultado if not formato else moeda(resultado)


def moeda(preco=0, simbolo='R$'):
    """
    Formata um valor como uma string monetária.

    Args:
        preco (float): O valor a ser formatado.
        simbolo (str, opcional): O símbolo monetário a ser usado.

    Returns:
        str: O valor formatado como uma string monetária.

    Examples:
        >>> moeda(100)
        'R$ 100,00'
        >>> moeda(50.5, 'US$')
        'US$ 50,50'

    By Haell
    """
    return f'{ simbolo}{preco: .2f}'.replace('.', ',')

def resumo(preco = 0, acrescimo = 0, desconto = 0):
    rotulo('Resumo do valor')
    rotulo_analise = '{:<20}'.format(f"Preço analisado: ")
    preco_formatado = moeda(preco)
    print(f"{rotulo_analise} {preco_formatado}")

    rotulo_dobro = '{:<20}'.format(f"Dobro do preço: ")
    dobro_preco = dobro(preco, True)
    print(f"{rotulo_dobro} {dobro_preco}")

    rotulo_metade = '{:<20}'.format(f"Metade do preço: ")
    metade_preco = metade(preco, True)
    print(f"{rotulo_metade} {metade_preco}")

    rotulo_acrescimo = '{:<20}'.format(f"{acrescimo} % de aumento: ")
    acrescimo_preco = aumentar(preco, acrescimo, True)
    print(f"{rotulo_acrescimo} {acrescimo_preco}")

    rotulo_desconto = '{:<20}'.format(f"{desconto} % de redução: ")
    desconto_preco = diminuir(preco, desconto, True)
    print(f"{rotulo_desconto} {desconto_preco}")
    ln(y=30)