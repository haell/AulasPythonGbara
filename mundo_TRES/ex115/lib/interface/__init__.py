from rich import print

def leia_inteiro(texto='Digite um Inteiro: '):
    while True:
        try:
            numero = int(input(f'\033[32m{texto}\033[m').strip())
        except (TypeError, ValueError):
            print("[red]ERRO! Tivemos um problema com os dados informados.[/red]")
        except KeyboardInterrupt:
            print("[red]Execução interrompida pelo usuário.[/red]")
            break
        except Exception as e:
            print("[red]ERRO! Digite um valor INTEIRO válido.[/red]")
        else:
            return numero

def _ln(n=45):    
    return f'-'*n

def rotulo(frase=' RÓTULO ', modelo=1):
    if modelo == 1:
        print(_ln())
        print(f"[bold blue]{frase.center(45)}[/bold blue]")
        print(_ln())
    elif modelo == 2:
        print(_ln())
        print(f'')
        print(f"[yellow]\n{frase.center(45)}\n[/yellow]")
        print('')
        print(_ln())

def montar_menu(lista):
    rotulo("MENU PRINCIPAL")
    for indice, opcao in enumerate(lista):
        print(f"[bold green]{indice+1}[/bold green] - [black]{opcao}[/black]")
    print(_ln())
    opc = leia_inteiro('Sua Opção: ')
    return opc