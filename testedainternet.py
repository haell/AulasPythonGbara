# -*- CODING MATK: 12 -*-
#
# SENO, COSSENO E TANGENTE EM PYTHON
#
# VICTOR HUGO
#
# EMAIL: VICTORHGDASILVA2017@OUTLOOK.COM
#
# ------------------------------------------------------

import time
import math

print("\t SENO, COSSENO E TANGENTE: \n")
a = input("SENO ----> \n'1'\n"
          "COSSENO ----> \n'2'\n"
          "TANGENTE ----> \n'3'\n"
          "SAIR ----> \n'n'\n")
if a == 'n':
    print("\t CARREGANDO....\n")
    loop = 0
    time.sleep(1.2)
    exit()

elif a == '1':
    print("\t CARREGANDO....\n")
    time.sleep(1.2)
    print("\t SENO \n")
    b = input("DIGITE O VALOR DO ÂNGULO: ")
    resp = math.sin(float(b))
    print("\t CALCULANDO....\n")
    loop = 0
    time.sleep(1.2)
    print("\t O VALOR DO SENO DO ÂNGULO {}° É: {:.2f} \n".format(b, resp))

elif a == '2':
    print("\t CARREGANDO....\n")
    loop = 0
    time.sleep(1.2)
    print("\t COSSENO \n")
    b = input("DIGITE O VALOR DO ÂNGULO: ")
    resp = math.cos(float(b))
    print("\t CALCULANDO....\n")
    time.sleep(1.2)
    print("\t O VALOR DO COSSENO DO ÂNGULO {}° É: {:.2f} \n".format(b, resp))

elif a == '3':
    print("\t CARREGANDO....\n")
    loop = 0
    time.sleep(1.2)
    print("\t TANGENTE \n")
    b = input("DIGITE O VALOR DO ÂNGULO: ")
    resp = math.tan(float(b))
    print("\t CALCULANDO....\n")
    time.sleep(1.2)
    print("\t O VALOR DA TANGENTE DO ÂNGULO {}° É: {:.2f} \n".format(b, resp))
