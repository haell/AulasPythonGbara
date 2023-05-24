# Aprimore o desafio anterior, mostrando no final:
""" 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
 """

colunas = []
soma_pares = 0
soma_terciera_coluna = 0
maior_valor = 0
for c in range(3):
    linha = []
    for l in range(3):
        valor = input(f"Digite um valor para: [{len(colunas)}, {l}] ")
        linha.append(valor)
    colunas.append(linha)
for i in colunas[1]:
    if int(i) > maior_valor:
        maior_valor = int(i)
for linha in colunas:    
    for coluna in range(3):
        print(f"{linha[coluna]:<5}| ", end='')
        if int(linha[coluna]) % 2 == 0: 
            soma_pares += int(linha[coluna])
    soma_terciera_coluna += int(linha[coluna])    
    print('')
print(f"Soma dos números PARES digitados: {soma_pares}")
print(f"Soma dos valores da terceira coluna: {soma_terciera_coluna}")
print(f"O maior valor da segunda linha: {maior_valor}")


