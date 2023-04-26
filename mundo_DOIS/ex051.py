print('='*30)
titulo = '{:^30}'.format('10 TERMOS DE UMA PA')
print(titulo)
print('='*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(primeiro_termo, 21, razao):
    print(c,'→ ', end='')
print(" Acabou!\n")