# Ler frase digitada e mostrar:
# Quantas vezes aparece a letra A;
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a ultima vez.

from unidecode import unidecode

frase = unidecode(str(input("Digite uma frase: "))).upper().lstrip()
print(f"A letra A aparece {frase.count('A')},"
      f" a primeira vez na posição {frase.find('A') + 1} "
      f"e a ultima vez na posição {frase.rfind('A') + 1}")
