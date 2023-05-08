# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:

    resultado = valor_para_tabuada = 0    
    pergunta = '{:->80}'.format('\nQuer ver a tabuada de qual valor? ')
    valor_digitado =  int(input(f'{pergunta}'))
    valor_para_tabuada = valor_digitado
    multiplicador = 1

    if valor_para_tabuada < 0:
        break
    else:
        print('-'*45)
        while multiplicador <= 10:
            resultado = multiplicador * valor_para_tabuada            
            print(f"{valor_para_tabuada} X {multiplicador} = {resultado}")
            multiplicador += 1
        valor_para_tabuada = valor_digitado
    
    
