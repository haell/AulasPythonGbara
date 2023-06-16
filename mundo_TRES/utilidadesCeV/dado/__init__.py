from rich import print

def valida_valor(texto):
    while True:
        valor = input(f'{texto}').strip()
        valor = valor.replace(',', '.')        
        if valor.replace('.', '', 1).isnumeric():
            break
        print(f"[red]ERRO! [green]\"{valor}\"[/green] é um valor inválido![/red]")

    return float(valor)