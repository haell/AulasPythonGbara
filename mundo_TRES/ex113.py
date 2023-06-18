# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
import os
from rich import print

def leia_inteiro(texto):
    while True:
        try:
            numero = int(input(f"{texto}"))
        except (TypeError, ValueError):
            print("[red]ERRO: Por favor, digite um número INTEIRO válido.[/red]")
            continue
        except KeyboardInterrupt:
            print("[red]Interrompido pelo usuário...[/red]")
            return 0
        else:
            return numero

def leia_real(texto):
    while True:
        try:
            numero = float(input(f"{texto}").replace(',','.'))
        except (TypeError, ValueError):
            print("[red]ERRO: Por favor, digite um número REAL válido.[/red]")
            continue
        except KeyboardInterrupt:
            print("[red]Interrompido pelo usuário...[/red]")
            return 0.0
        else:
            return numero

# Programa principal
num_inteiro =  leia_inteiro('Digite um INTEIRO: \033[32m')
num_real = leia_real('\033[mDigite um número REAL: \033[36m')
print('\033[m')
os.system('cls')
print(f"O valor [bold green]INTEIRO[/bold green] foi [bold green]{num_inteiro}[/bold green] \
e o [bold blue]REAL[/bold blue] foi [bold blue]{num_real:.2f}[/bold blue]".replace('.',','))