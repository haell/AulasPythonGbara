# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = str, gools = 0):
    """
    Função para exibir a ficha de um jogador.

    Parâmetros:
    - nome (str): Nome do jogador (opcional, padrão: "<desconhecido>").
    - gols (int): Número de gols do jogador (opcional, padrão: 0).

    Exemplo:
    >>> ficha("João", 5)
    O jogador João fez 5 gol(s) no campeonato.

    - By Haell
    """
    if not gools.isdigit():
        gools = 0
    if not nome:
        nome = "<desconhecido>"
    print(f"O jogador {nome.capitalize()} fez {gools} gol(s) no campeonato.")
    
nome_jogador = input("Nome do jogador: ")
n_gols = input("Quantos gols: ")

ficha(nome_jogador, n_gols)