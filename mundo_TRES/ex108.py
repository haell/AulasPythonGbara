#  Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from fex107.moeda import moeda, dobro, diminuir, aumentar, metade
from fex107.util import ln
from rich import print


preco = float(input("Digite o preço: R$\033[32m "))
taxa = float(input("\033[mDigite a taxa: "))
metade_preco = f"A metade de {moeda(preco)} é {moeda(metade(preco))}"
ln(y=len(metade_preco)+2)
print(metade_preco)
print(f"Diminuindo {taxa:.1f}%, temos {moeda(diminuir(preco, taxa))}")
print(f"O dobro de {moeda(preco)} é {moeda(dobro(preco))}")
print(f"Aumentando {taxa:.0f}%, temos {moeda(aumentar(preco, taxa))}")