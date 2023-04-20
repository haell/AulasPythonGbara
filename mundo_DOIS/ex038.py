# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais
numero_um = 3
numero_dois = 3

def separa_maior_numero(numero_um, numero_dois):
    return f"O primeiro valor é maior: {numero_um}" if numero_dois < numero_um else f"O segundo valor é maior: {numero_dois}"

print(f"Não existe valor maior, os dois são iguais: {numero_um} == {numero_dois}" if numero_um == numero_dois else separa_maior_numero(numero_um, numero_dois))
