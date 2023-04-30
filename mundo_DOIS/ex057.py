# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Digite o sexo [M/F]: ").strip().upper()[0]
m_ou_f = ''
while sexo not in ('MmFf'):
    nova_opção = input("Dados inválidos. Por favor, informe o sexo: ")
    sexo = nova_opção
if sexo in ('Mm'):
    m_ou_f = 'Masculino'
elif sexo in ('Ff'):
    m_ou_f = 'Feminino'
    
print(f'Sexo {m_ou_f} registrado com sucesso!\n')
