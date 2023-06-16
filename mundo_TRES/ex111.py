# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from utilidadesCeV.moeda import resumo


preco = float(input("Digite o Preço: R$ "))
acrescimo = float(input("Digite o Acrescimo (%): "))
desconto = float(input("Digite o Desconto (%):  "))
resumo(preco, acrescimo, desconto)
