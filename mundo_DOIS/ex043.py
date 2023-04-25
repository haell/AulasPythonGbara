# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
""" 
 IMC abaixo de 18,5: Abaixo do Peso

 Entre 18,5 e 25: Peso Ideal

 25 até 30: Sobrepeso

 30 até 40: Obesidade

 Acima de 40: Obesidade Mórbida
 """
altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

def calcula_imc(altura, peso):
    imc = peso / (altura**2)
    return imc

imc = calcula_imc(altura, peso)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}', end=' ')
    print(f'Você está \033[1;31;40mAbaixo do Peso\033[m!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.2f}', end=' ')
    print(f'Você está no \033[1;32;40mPeso Ideal\033[m!')
elif imc >= 25 and imc <= 30:
    print(f'Seu IMC é {imc:.2f}', end=' ')
    print(f'Você está com \033[1;31;40mSobrepeso\033[m!')
elif imc > 30 and imc <= 40 :
    print(f'Seu IMC é {imc:.2f}', end=' ')
    print(f'Você está com \033[1;31;40mObesidade\033[m!')
else:
    print(f'Seu IMC é {imc:.2f}', end=' ')
    print(f'Você está com \033[1;31;40mObesidade Mórbida\033[m!')
    