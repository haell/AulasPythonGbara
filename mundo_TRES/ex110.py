# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from fex107.moeda import resumo


preco = float(input("Digite o Preço: R$ "))
acrescimo = float(input("Digite o Acrescimo (%): "))
desconto = float(input("Digite o Desconto (%):  "))
resumo(preco, acrescimo, desconto)
