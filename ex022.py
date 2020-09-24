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
print("""Seu nome com todas as letras em maiúsculo = {}
Seu nome com todas as letras em minúsculo = {}
Seu nome tem {} letras (contando os espaços em branco)
Seu nome tem {} letras (Sem os espaços em branco)
"Extra": Seu nome tem {} palavras
Seu primeiro nome tem {} letras"""
      .format(nome.upper(), nome.lower(), len(nome), len(''.join(nome.split())), len(nome.split()), len(nome.split()[0])))
