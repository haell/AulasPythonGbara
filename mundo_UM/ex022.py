# Ler o nome completo
# Imprimir o nome com todas as letras maiúsculas
# Imprimir o nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome

# nome = str(input('Digite seu nome completo: '))
# print('Seu nome com todas as letras em maiúsculo = ', nome.upper())
# print('Seu nome com todas as letras em minúsculo = ', nome.lower())
# print('Seu nome tem {} letras (contando os espaços em branco)'.format(len(nome)))
# print('Seu nome tem {} letras (Sem os espaços em branco)'.format(len(''.join(nome.split()))))
# print('"Extra": Seu nome tem {} palavras'.format(len(nome.split())))

# Resolvendo o exercicio todo em duas linhas.
nome = str(input('Digite seu nome completo: '))

todas_letras_maiusculas = nome.upper()
todas_letras_minusculas = nome.lower()
qtd_letras_COM_espaço = len(nome)
qtd_letras_SEM_espaço = len(''.join(nome.split()))
qtd_palavras = len(nome.split())
qtd_letras_primeiro_nome = len(nome.split()[0])



print(f"""Seu nome com todas as letras em maiúsculo = {todas_letras_maiusculas}
Seu nome com todas as letras em minúsculo = {todas_letras_minusculas}
Seu nome tem {qtd_letras_COM_espaço} letras (contando os espaços em branco)
Seu nome tem {qtd_letras_SEM_espaço} letras (Sem os espaços em branco)
"Extra": Seu nome tem {qtd_palavras} palavras
Seu primeiro nome tem {qtd_letras_primeiro_nome} letras""")
