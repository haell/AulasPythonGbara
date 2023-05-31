# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
 
nome = input('Noma: ')
media = float(input('Média: '))
situacao = str

if media < 5:
    situacao = 'Reprovado'
elif 5 < media or media < 7:# Explicação: "se 5 é menor que meia E media menor que 7(5 < media <7) <<== isso aqui é um 'E' " é diferente de "se 5 é menor que média OU media menor que 7(5 < media or media < 7)"
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'


dados_aluno = {
    'nome': nome,
    'media': media,
    'situacao': situacao
}


print('-'*50)
print(f"- Nome: {dados_aluno['nome']}\n- Média: {dados_aluno['media']}\n- Situação: {situacao}\n")