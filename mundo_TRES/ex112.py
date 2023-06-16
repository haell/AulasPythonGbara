# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidadesCeV.moeda import resumo
from utilidadesCeV.dado import valida_valor


preco = valida_valor('Digite o preço: R$ ')
acrescimo = valida_valor("Digite o Acrescimo (%): ")
desconto = valida_valor("Digite o Desconto (%):  ")
resumo(preco, acrescimo, desconto)
