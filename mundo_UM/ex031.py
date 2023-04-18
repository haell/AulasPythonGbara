# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem acrescentando R$0,50 por km para viagens de até 200km.
# e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distância da viagem em km: '))
valor_ate_200 = 0.50
valor_maior_200 = 0.45

if distancia <= 200:
    passagem = distancia*valor_ate_200
    print(f'Distância percorrida de {distancia}km, valor da passagem é: R${passagem}')
else:
    passagem = distancia*valor_maior_200
    print(f'Distância percorrida de {distancia}km, Valor da passagem: {passagem}')
