# Formatação para colorir o texto:   \033[ 'estilo' ; 'texto' ; 'fundo' m

# Método para colorir o texto:
def style_text_background_msg(st='none', txt='white', bckgd='black', msg=''):
    # Define styles:
    styles = {'none': 0, 'negative': 0, 'bold': 1, 'underline': 4}
    style = styles.get(st, 0)

    # Define text colors:
    text_colors = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
                   'blue': 34, 'purple': 35, 'cian': 36, 'grey': 37}
    text = text_colors.get(txt.lower(), 37)

    # Define background colors:
    bg_colors = {'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
                 'blue': 44, 'purple': 45, 'cian': 46, 'grey': 47}
    background = bg_colors.get(bckgd.lower(), 40)

    # Mount frase:
    config = f'\033[{style};{text};{background}m{msg}\033[m'
    print(config)

# Agora é só chamar a função passando os parametros como String e na ordem, 1-estilo; 2-cor do texto; 3-cor do fundo; 4-texto
style_text_background_msg('bold', 'red', 'green', ' TESTE ')
