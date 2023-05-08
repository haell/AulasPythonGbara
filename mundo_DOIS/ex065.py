# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
opcao = ''
lista_numeros_digitados = []
soma = 0
media = 0
maior_numero = 0
menor_numero = 0
inteiro = int(input("Digite um número: "))

while opcao.lower() != 'n':
    opcao = input("\033[32mDeseja continuar [S/N]:\033[m ")
    if opcao.lower() not in ['s', 'n']:
        print("Opção \033[31minválida\033[m. Digite S ou N.")
    elif opcao.lower() == 'n':
        lista_numeros_digitados.append(inteiro)
        soma += inteiro    
        media = soma / len(lista_numeros_digitados)
        maior_numero = max(lista_numeros_digitados)
        menor_numero = min(lista_numeros_digitados)
        break
    else:        
        lista_numeros_digitados.append(inteiro)
        soma += inteiro    
        media = soma / len(lista_numeros_digitados)
        maior_numero = max(lista_numeros_digitados)
        menor_numero = min(lista_numeros_digitados)
        inteiro = int(input("Digite um número: "))

print(f"Números digitados: {lista_numeros_digitados}")
print(f"Soma de todos: {soma}")
print(f"Média entre todos: {media}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")