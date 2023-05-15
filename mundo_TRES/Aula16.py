lanche = ("hamburguer", "suco", "pizza", "pudim")
print(lanche)
print(sorted(lanche))
for c in range(0, len(lanche)):
    print(f'Lanche {c} é {lanche[c]}')

for lnc in lanche:
    print(f"Lanche = {lnc}")

for posição, lanche in enumerate(lanche):
    print(f"Lanche {posição} é {lanche}")

a = (2, 5, 2, 4)
b = (5, 8, 1, 2)
c = a+b
print(c)
print(f"Posição do número {c[2]} {c.index(2)}")
print(c.count(2))

pessoa = ('Israel', 41, 'M', 72.55) # Del(pessoa) Apaga a tupla
print(pessoa)

