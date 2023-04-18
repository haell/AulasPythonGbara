from math import hypot
co = float(input('Digite a altura do triangulo: '))
ca = float(input('Digite a base do triangulo: '))
print('=== Calculo da hipotenusa do triangulo ===')
print(' Altura -> A = {:.2f}\n  Base  -> B = {:.2f}'.format(co, ca))
print('           +\n           ++\n           +++\n           ++++\n        A  +++++\n           ++++++  H = {:.2f}\
       hipotenusa\n           +++++++\n           ++++++++\n           +++++++++\n               B '.format(hypot(co, ca)))

