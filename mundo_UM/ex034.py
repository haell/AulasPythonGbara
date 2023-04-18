# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_original = float(input('Digite o salário: R$'))


if salario_original > 1250.00:
    acrescimo = 1.10    
if salario_original <= 1250.00:
    acrescimo = 1.15

print(f'Seu salario era RS{salario_original:.2f} e agora é R${salario_original*acrescimo:.2f}.')
