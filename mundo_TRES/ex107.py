# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from fex107 import moeda
from fex107 import util


preco = float(input("Digite o preço: R$ "))
taxa = float(input("Digite a taxa: "))
metade_preco = f"A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}"
util.ln(y=len(metade_preco)+2)
print(metade_preco)
print(f"Diminuindo {taxa:.1f}%, temos R${moeda.diminuir(preco, taxa):.2f}")
print(f"O dobro de R${preco:.1f} é R${moeda.dobro(preco):.2f}")
print(f"Aumentando {taxa:.0f}%, temos R${moeda.aumentar(preco, taxa):.2f}")