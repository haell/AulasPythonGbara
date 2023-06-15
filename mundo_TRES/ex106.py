# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
c = (
    '\033[m',         # 0 - sem cor.
    '\033[1;30;41m',  # 1 - vermelho
    '\033[1;30;42m',  # 2 - verde
    '\033[1;30;46m',  # 3 - Cian
    '\033[1;30;44m',  # 4 - verde
    '\033[7m'      # 5 - branco
)


def ajuda(comando):
    titulo(f"Acessando o manual do comando \'{comando}\'", 3)
    help(comando)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0])


# Programa Principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Bíblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)
