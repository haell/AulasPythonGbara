print('='*30)
titulo = '{:^30}'.format('10 TERMOS DE UMA PA')
print(titulo)
print('='*30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + 1, razao):
    print(c,'→ ', end='')
print(" Acabou!\n")