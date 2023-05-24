# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint


while True:
    jogos_solicitados = input("Quantos jogos da MEGA-SENA você quer fazer? ")
    if not jogos_solicitados.isdigit():
        print("Valor inválido!")
    else:
        jogos_solicitados = int(jogos_solicitados)
        break
n_de_jogos = 0
grupo_de_jogos = []

while n_de_jogos < jogos_solicitados:
    jogo = []
    n_dezenas = 0
    while n_dezenas != 6:
        dezena = randint(1, 60) 
        if dezena not in jogo:
            jogo.append(dezena)
            n_dezenas += 1
    grupo_de_jogos.append(jogo)
    n_de_jogos += 1  
for indice, jogo in enumerate(grupo_de_jogos):
    print(f"{indice+1}°  Jogo => {jogo}")


