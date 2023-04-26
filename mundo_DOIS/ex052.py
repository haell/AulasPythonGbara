# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Digite um número: "))
cont = 0
for i in range(1, numero + 1):
        if numero % i == 0:
            print("\033[36m", end=" ")
            cont += 1
        else:
            print("\033[31m",end=" ")
        print(f"{i}", end=" ")
print(f"\n\n\033[1;36m{numero}\033[m é divisivel pelos números da cor \033[1;36m▓▓▓\033[m")
print(f"\033[m\nO número \033[1;36m{numero}\033[m foi divisivel \033[1;32m{cont}\033[m vezes!")
if cont <= 2:
     print(f"E por isso \033[1;36m{numero}\033[m \033[4;32mÉ PRIMO\033[m\n")
else:
     print(f"E por isso \033[1;36m{numero}\033[m \33[4;31mNÃO É PRIMO\033[m\n")
