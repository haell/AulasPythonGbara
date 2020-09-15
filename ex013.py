# aumentando salário do funcionário em 15%
salario = float(input('Qual o salário atual do funcionário: R$'))
aumento = salario*15/100
nSalario = salario+aumento
print('Com aumento de {:.2f}% o novo salário do funcionário é de R${:.2f}'.format(aumento, nSalario))
