# Vamos criar um menu em Python, usando modularização.
import os
from time import sleep
from rich import print
from lib.interface import *

while True:
        resposta = montar_menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
        if resposta == 1:
            os.system('cls')
            rotulo("Opção 1", 2)
        elif resposta == 2:
            os.system('cls')
            rotulo("Opção 2", 2)
        elif resposta == 3:
            rotulo("Saindo do sistema")
            print("[bold green]Até logo![/bold green]".center(70))
            break
        else:
            os.system('cls')
            print("[red]Falha! Digite uma opção válida.[/red]")
        sleep(2)