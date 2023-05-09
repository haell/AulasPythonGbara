# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
""" 
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
 """

qtd_maior_18 = homens_cadastrados = mulheres_ate_19 = 0


while True:

    valida_idade = False
    while valida_idade == False:
        idade = input("Idade: ")
        if idade.isdigit() and int(idade) > 0:
            valida_idade = True
            if int(idade) >= 18:
                qtd_maior_18 += 1
        else:
            print('Idade inválida.')
            valida_idade = False

    valida_sexo = False
    while valida_sexo == False:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()
        if sexo != '' and sexo.isalpha():
            if sexo[0] == 'F':
                valida_sexo = True
                if int(idade) < 20:
                    mulheres_ate_19 += 1
            elif sexo[0] == 'M':
                valida_sexo = True
                homens_cadastrados += 1
            else:
                print('Valor inválido!')
                valida_idade = False
        else:
            print('Valor inválido!')
            valida_idade = False

    print(f"Elas: {mulheres_ate_19}")

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp != '' and resp.isalpha():
        if resp == 'N':
            break
    
print(f"\nTotal de pessoas com mais de 18 anos: {qtd_maior_18}")
print(f"Total de homens cadastrados: {homens_cadastrados}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_ate_19}")  
    
print('\nFim do programa!')
