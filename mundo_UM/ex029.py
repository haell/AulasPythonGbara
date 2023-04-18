# Ler a velocidade de um carro e aplicar multa de R$7,00 por KM caso ultrapasse 80km/h

velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80Km/h.')
    print('{}Km/h acima do permitido!'.format(velocidade - 80))
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R${:.2f}!'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
