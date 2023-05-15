# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ("Arroz", 22.75, "Feijão", 21.50, "Ovo", 12.00, "Leite", 4.99, "Açúcar", 3.89,
            "Farinha", 3.50, "Café", 7.25, "Manteiga", 8.99, "Refrigerante", 5.49, "Pão", 6.75,
            "Bolacha", 2.99, "Queijo", 12.50, "Sabão em pó", 9.99, "Shampoo", 11.50, "Condicionador", 12.00,
            "Creme dental", 3.25, "Escova de dente", 4.50)

linha = '-'*50
titulo = '{:^50}'.format("LISTAGEM DE PREÇOS")
print(linha)
print(titulo)
print(linha)
padrão = '¨.'
for i in range(0, len(produtos), 2):
    produto = '{:.<40}'.format(f"{produtos[i]} ")
    preço = '{:>6}'.format(f"{produtos[i+1]}")
    print(produto,"R$",preço)
print(linha)