diasalugado = float(input('Quantos dias ficou alugado? '))
kmrodado = float(input('Quantos kilometros rodados? '))
pagar = (diasalugado*60)+(kmrodado*0.15)
print('\nVocê andou {:.0f}Km e ficou com o carro por {:.0f} dia(s) \nO valor a pagar é = R${:.2f}'.format(kmrodado, diasalugado, pagar))
