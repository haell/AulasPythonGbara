# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas, vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from fex107.moeda import moeda, dobro, diminuir, aumentar, metade
from fex107.util import ln
from rich import print


preco = float(input("Digite o preço: R$\033[32m "))
taxa = float(input("\033[mDigite a taxa: "))
metade_preco = f"A metade de {moeda(preco)} é {metade(preco, True)}"
ln(y=len(metade_preco)+2)
print(metade_preco)
print(f"O dobro de {moeda(preco)} é {dobro(preco, True)}")
print(f"Aumentando {taxa:.1f}%, temos {aumentar(preco, taxa, True)}")
print(f"Diminuindo {taxa:.1f}%, temos {diminuir(preco, taxa, True)}")

help(aumentar)