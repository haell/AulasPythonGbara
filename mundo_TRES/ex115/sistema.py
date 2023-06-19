# Vamos criar um menu em Python, usando modularização.
import os
from time import sleep
from rich import print
from lib.interface import *
from lib.arquivo import *

nome_arquivo = 'cursoemvideo.txt'
if not arquivo_existe(nome_arquivo):
    criar_arquivo(nome_arquivo)
     

while True:
        resposta = montar_menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
        if resposta == 1:
            os.system('cls')
            # Opção de listar as pessoas cadastradas
            ler_arquivo(nome_arquivo)
        elif resposta == 2:
            os.system('cls')
            # Opção de cadastrar pessoa no arquivo.
            rotulo('CADASTRAR PESSOA')
            nome = str(input("Digite o nome: "))
            idade = leia_inteiro('Digite a idade: ')
            cadastrar(nome_arquivo, nome, idade)
        elif resposta == 3:
            rotulo("Saindo do sistema")
            print("[bold green]Até logo![/bold green]".center(70))
            break
        else:
            os.system('cls')
            print("[red]Falha! Digite uma opção válida.[/red]".center(55))
        sleep(2)