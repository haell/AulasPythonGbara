tipo = int(input("  \n......TIPOS.....\n( 1 ) R$ para US$ \n( 2 ) US$ para R$\n\nEscolha o tipo: "))
if(tipo == 1):
    valorReal: float = float(input('Insira o valor: R$'))
    dolar = 3.27
    valorDolar = valorReal / dolar
    print('Valor do dolar Hoje: R${}'.format(dolar))
    print('\nR${:.2f} convertido em dolar fica US${:.2f}'.format(valorReal, valorDolar))
else:
    valorDolar = float(input('Put the value: US$'))
    real = 0.3058103975535168
    valorReal = valorDolar / real
    print('Dollar value today: R${}'.format(real))
    print('\nUS${:.2f} converted into reais is R${:.2f}'.format(valorDolar, valorReal))
