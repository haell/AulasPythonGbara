# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

import os


alunos = []

while True:
    aluno = []
    notas = []
    nome = str(input("Nome do aluno: "))
    for nota in range(2):
        notas.append(float(input(f"{nota+1}ª nota: ")))
    aluno.append(nome)
    aluno.append(notas)    
    alunos.append(aluno)
    resp = input("Cadastrar mais aluno? [S/N]: ").strip()
    if resp[0] in "nN":
        break
os.system('cls')
############################
print("=-"*20)             ###
print(f"{'N°':<6}", end='')  ###
print(f"{'NOME':<26}", end='') ### É só o cabeçalho.
print(f"{'MÉDIA':<13}")      ###
print("-"*40)              ###
############################

for indice, aluno in enumerate(alunos):
    media = (alunos[indice][1][0] + alunos[indice][1][1])/2
    print(f"{indice:<6}{alunos[indice][0]:<26}{media:<13}")
print('-'*40)

resp = ''
while resp != '999':
    resp = input("Exibir notas de qual aluno? (999 interrompe): ")
    if resp.isdigit():
        if int(resp) in range(0, len(alunos)):
            print(f"As notas de {alunos[int(resp)][0]} são {alunos[int(resp)][1]}")
            print('-'*40)
