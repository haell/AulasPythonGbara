carteira = float(input("Digite um valor: R$"))
dolar = 3.27
convers = (carteira / dolar)
print('R${} convertido em dolares fica Us${:.2f}' .format(carteira, convers))
