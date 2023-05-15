# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
""" 
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
 """
from rich import print
from rich.table import Table
from rich.console import Console
from rich.columns import Columns

times_brasileirao = ("Botafogo", "Palmeiras", "Fluminense", "Cruzeiro", "Athletico", "Atlético", "Santos", "Fortaleza", "Flamengo",
                     "São Paulo", "Grêmio", "Internacional", "Bragantino", "Bahia", "Goiás", "Vasco", "Corinthians", "Cuiabá",
                     "Coritiba", "América")
times_coluna_1 = times_brasileirao[:10]
times_coluna_2 = times_brasileirao[10:]

table = Table(show_header=False)
table.add_column(justify="left")
table.add_column(justify="left")

for time1, time2 in zip(times_coluna_1, times_coluna_2):
    table.add_row(time1, time2)

console =  Console()
console.print(table)

""" for colocação, time in enumerate(times_brasileirao):
    print(f"{colocação+1}° {time}")
     """
print(f"\nOs 5 primeiros colocados: {times_brasileirao[0:5]}\n")
print(f"Os últimos 4 colocados: {times_brasileirao[-4:]}\n")
print(f"Times em ordem alfabética: {sorted(times_brasileirao)}\n")
print(f"O melhor time do mundo está em: {times_brasileirao.index('Corinthians')+1}°\n")
