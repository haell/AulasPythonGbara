#   "Reproduza um arquivo de som em formato mp3"
#   A Biblioteca importada pelo professor é a pygame.
#   Deve instalar a biblioteca
#   O aquivo .mp3 deve estar na pasta do projeto
from pygame import mixer


mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.set_volume(0.8)
mixer.music.play()

while True:

    print('Digite P para pausar a música \
            Digite R para despausar a música \
            Digite E para parar a execução.')
    query = input(" ").upper()

    if query == 'P':
        mixer.music.pause()
    elif query == 'R':
        mixer.music.unpause()
    elif query == 'E':
        mixer.music.stop()
        break
    else:
        print("Opção inválida!")
