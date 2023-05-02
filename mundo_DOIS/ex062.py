# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar termos_adicionais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
def cabecalho():
    print('='*30)
    titulo = '{:^30}'.format('10 TERMOS DE UMA PA')
    print(titulo)
    print('='*30)

cabecalho()

termo = int(input("PRIMEIRO Termo: "))
razao = int(input("Razão: "))
termo_final = termo + (10 - 1) * razao # Termo final, inicialmente configurado para ser 10
primeiro_termo = termo
termos_adicionais = 1
contador_de_termos = 10

while termos_adicionais > 0:
    while primeiro_termo <= termo_final:
        print(f"{primeiro_termo} -> ", end='')
        primeiro_termo += razao
    print("\033[1;32mPAUSE\033[m")
    termos_adicionais = int(input("\nQuantos termos quer adicionar? "))
    termo_final += termos_adicionais * razao
    contador_de_termos += termos_adicionais

print(f'Foram {contador_de_termos} termos.')    
print("\033[1;32mFIM\033[m")