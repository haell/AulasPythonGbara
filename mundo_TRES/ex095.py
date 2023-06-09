# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

""" Exercício 93:
    # Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    # O programa vai ler o nome do jogador e quantas partidas ele jogou.
    # Depois vai ler a quantidade de gols feitos em cada partida.
    # No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
def fim():
    while True:
        sair = input("Deseja continuar? [S/N]: ").strip().upper() or 'vazio'
        if sair[0] in 'SN':
            return sair
        print("Digite alguma coisa.")

def qtd_partidas(nome):
    while True:            
        numero_partidas = input(f"Quantas partidas {nome} jogou: ")
        if numero_partidas.isdigit():
            return  int(numero_partidas)
        print("Digite um número Inteiro. ")

def qual_nome():
    while True: 
        nome = input("Nome do jogador: ")
        if not nome.isnumeric() and len(nome.split()) > 0:
            return nome.capitalize()
        print("O nome deve ser uma String.")

def gols_jogador(nome, numero_partidas):
    gols = list()
    for partida in range(numero_partidas):
        while True:       
            numero_gols = input(f"Quantos gols {nome} fez na {partida+1}ª partida: ")
            if numero_gols.isdigit():
                gols.append(int(numero_gols))
                break
            print("Valor inválido!")
    return gols

def qtd_gols(gols):
    total_gols = 0
    for gol in gols:
        total_gols += gol
    return total_gols

def cria_jogador(nome, numero_partidas, gols, total_gols):
    jogador = dict()
    jogador['nome'] = nome
    jogador['numero_partidas'] = numero_partidas
    jogador['gols'] = gols
    jogador['total_gols'] = total_gols
    return jogador

def cabecalho():        
    import os
    os.system('cls')
    print("-="*40)
    title_cod = '{:^5}'.format("Cod")
    title_nome = '{:^25}'.format("Nome")
    title_gols = '{:^35}'.format("Gols")
    title_total = '{:^10}'.format("Total")
    print(title_cod, end='')
    print(title_nome, end='')
    print(title_gols, end='')
    print(title_total)
    print("-"*80)

def exibir_jogadores(time):
    for index, jogador in enumerate(time):
        cod = '{:<14}'.format(f"  {index}")
        nome_jogador = '{:<25}'.format(f"{jogador['nome']}")
        gols_jgd = '{:<28}'.format(f"{jogador['gols']}")
        total = '{:<10}'.format(f"{jogador['total_gols']}")
        print(cod, nome_jogador, gols_jgd, total)
    print('-'*80)

def escolha_jogador(time):
    while True:
        opcao = input("De qual jogador quer saber os detalhes? [999 para encerrar]: ")
        if opcao.isdigit():
            if opcao == '999':
                break
            elif int(opcao) in range(len(time)):
                titulo_detalhes = '{:^60}'.format(f"INFORMAÇÕES DO JOGADOR -> {time[int(opcao)]['nome'].upper()}")
                print(titulo_detalhes)
                for i, g in enumerate(time[int(opcao)]['gols']):
                    if g == 0:
                        partida = '{:^60}'.format(f"No {i+1}° jogo, não fez gols")
                        print(partida)
                    else:
                        partida = '{:^60}'.format(f"No {i+1}° jogo, fez {g} gols")
                        print(partida)
            else:
                print(f"Não existe jogador com o código {opcao}.")
        else:
            print("Valor inválido!")

def main():
    time = list()

    sair = 'S'
    while sair != 'N':
        
        nome = qual_nome()
        numero_partidas = qtd_partidas(nome)

        gols = gols_jogador(nome, numero_partidas)
        total_gols = qtd_gols(gols)
        jogador = cria_jogador(nome, numero_partidas, gols, total_gols)
        time.append(jogador)
        
        # Finaliza os cadastros
        sair = fim()
    cabecalho()
    exibir_jogadores(time)
    escolha_jogador(time)

###################################### MAIN ####################################################
if __name__ == "__main__":
    main()