# Receber nome completo e mostrar o primeiro e ultimo.

nome = input("Qual seu nome completo: ").strip().split()
print("Olá, Sr(a). {} {}!".format(nome[0], nome[len(nome)-1]))
