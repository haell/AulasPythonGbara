# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
"""
################### COM USO DA BIBLIOTECA RICH! #############################
from rich.table import Table
from rich import print


table = Table()
table.add_column('')
for coluna in range(3):
    table.add_column(f'Coluna {coluna+1}')

for linha in range(3):
    lista = []
    for coluna in range(3):
        while True:
            try:
                valor = int(
                    input(f"Digite um valor para  [{linha}, {coluna}]:"))
                lista.append(valor)
                break
            except KeyboardInterrupt as error:
                print("Deu erro!", " Tente novamente.")
                continue
            except Exception as errr:
                print(f"Erro: {errr}")
    table.add_row(f'{linha+1}ª linha ->',
                  f'{lista[0]}', f'{lista[1]}', f'{lista[2]}')
print(table)"""
################################################################################

# UTILIZANDO APENAS LISTAS
colunas = []
for c in range(3):
    linha = []
    for l in range(3):
        valor = input(f"Digite um valor para: [{len(colunas)}, {l}] ")
        linha.append(valor)
    colunas.append(linha)
for linha in colunas:    
    for coluna in range(3):
        print(f" {linha[coluna]}  | ", end='')
    print('')