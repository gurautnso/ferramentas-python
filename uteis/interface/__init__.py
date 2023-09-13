from uteis.numeros import *
from uteis.strings import *


def menu(prompt, *opcs):
    titulo(prompt)
    c = 1
    for item in opcs:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    lin()
    while True:
        opc = leiaint(f'\033[32mescolha uma opção:\033[m ')
        if opc in range(1, c):
            return opc
        else:
            print(f'\033[31;40mERRO! Digite um número válido.\033[m')
