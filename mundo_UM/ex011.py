larguraParede = float(input('Digite a largura da parede em metros: '))
alturaParede = float(input('Digite a altura da parede em metros: '))
areaParede = larguraParede * alturaParede

# convertendo para cm
areaEmCm = areaParede * 100 #cm

# informações fixas (1L == 1000ml) e (2m² == 200m²) para melhorar a precisão
tinta = 5 #ml por cm²

# calculo do gasto de tinta em ml
tintaMl = tinta * areaEmCm #ml

# converter resultado para litros
tintaL = tintaMl / 1000 #l

print('\nA área total da parede é {:.2f}m²'.format(areaParede))
print('Precisa de {:.2f} litros de tinta para pintar'.format(tintaL))
