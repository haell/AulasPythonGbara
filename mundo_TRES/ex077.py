# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("comboio", "estranho", "pudim", "igreja", "milho", "computador", "melancia", 
            "maravilha", "problema", "chocolate", "violino", "eletrico", "historia", 
            "gramatica", "esportivo", "fantastico", "telefone", "inteligente", "piano",
            "paralelepipedo", "circunferencia", "arqueologo", "insuficiente", "helicopetro", 
            "desorganizado", "hexagono", "juridico", "propaganda")

for palavra in palavras:
    texto = '{:.<43}'.format(f"Na palavra \033[36m{palavra.upper()}\033[m temos")
    print(texto, end='')
    for letra in palavra:
        if letra in "aeiou":            
            vogais = '{:>8}'.format(f" \033[32m{letra}\033[m")
            print(vogais, end='')
    print('')
    