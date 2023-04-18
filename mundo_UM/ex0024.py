# Ler o nome da cidade e dizer se começa com 'SANTO'

nome = input('Digite o nome de uma cidade: ').lstrip().upper().find("SANTO", 0, 5)
if nome == -1:
    print('O nome da cidade não começa com SANTO')
else:
    print('O nome da cidade começa com SANTO')

