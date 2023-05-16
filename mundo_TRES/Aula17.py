# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
num = [2, 5, 9, 1]
print(f"num = {num}")

num[2] = 3
rashTag = "num[2] = 3  Altera o elemento na posição '2' de 9 para 3"
print(f"{rashTag}\n{num}\n")

num.append(36)
rashTag = "num.append(36) Adiciona 36 como último elemento da lista"
print(f"{rashTag}\n{num}\n")

num.sort(reverse=True)
rashTag = "num.sort(reverse=True) Ordena lista inversamente"
print(f"{rashTag}\n{num}\n")

num.insert(2, 0)
rashTag = "num.insert(2, 0) Insere na posição 2 o número 0"
print(f"{rashTag}\n{num}\n")

num.pop()
rashTag = "num.pop() Elimina o último elemento da lista"
print(f"{rashTag}\n{num}\n")

num.pop(2)
rashTag = "num.pop(2) Elimina o elemento na posição 2 da lista"
print(f"{rashTag}\n{num}\n")

num.remove(5)
rashTag = "num.remove(5) Remove a primeira ocorrência do n° 5 na lista"
print(f"{rashTag}\n{num}\n")

print(f"len(num) Mostra o n° de elementos na lista = {len(num)} elementos.\n")
