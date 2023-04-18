# Promoção 5% de desconto em TUDO!
valorN = float(input('Informe o preço do produto: R$'))
valorD = 5
valorPromoção = valorN - ((valorN*valorD)/100)

print('\nO valor de R${:.2f} com {:.2f}% de desconto fica R${:.2f}'.format(valorN, valorD, valorPromoção))