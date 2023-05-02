# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
def cabecalho():
    print('='*30)
    titulo = '{:^30}'.format('10 TERMOS DE UMA PA')
    print(titulo)
    print('='*30)

""" 
cabecalho()
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + 1, razao):
    print(c,'→ ', end='')
print(" Acabou!\n")
 """
cabecalho()
termo = int(input("PRIMEIRO Termo: "))
razao = int(input("Razão: "))
decimo_termo = termo + (10 - 1) * razao
c = termo

while c < decimo_termo + 1:
    print(f"{c} -> ", end='')
    c += razao
print("\033[1;36mFIM\033[m")