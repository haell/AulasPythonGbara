# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
jogador['nome'] = input("Nome do jogador: ")
while True:
    n_partidas = input(f"Quantas partidas o {jogador['nome']} jogou: ")
    if n_partidas.isdigit():
        if n_partidas != '0':
            lista_gols = []
            for partida in range(int(n_partidas)):
                lista_gols.append(int(input(f"Quantos gols na {partida+1}ª partida: ")))
            jogador['gols'] = lista_gols            
            break        
        else: break    
soma = 0
for i in jogador['gols']:
    soma += i
jogador['Total'] = soma
print('-'*30)
print(jogador)
print('-'*30)
for k, i in jogador.items():
    print(f"O campo {k} tem o valor {i}")
print('-'*30)
print(f"O jogador {jogador['nome']} jogou {n_partidas} partidas.")
for partida in range(int(n_partidas)):
    result = '{:>35}'.format(f"=> Na {partida+1}ª partida, fez {jogador['gols'][partida]} gols.")
    print(result)
print(f"Foi um total de {jogador['Total']} gols.\n")
