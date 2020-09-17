

# aumentando salário do funcionário em 15%
salario = float(input('Qual o salário atual do funcionário: R$'))
pcent = float(input('Digite a diferença '))
nSalario = salario+salario*pcent/100

print('Com aumento de {:.2f}% o novo salário do funcionário é de R${:.2f}'.format(pcent, nSalario))