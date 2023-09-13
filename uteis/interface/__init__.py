from uteis.numeros import *


def menu(prompt, *opcs):
    titulo(prompt)
    c = 1
    for item in opcs:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    lin()
    opc = leiaint(f'\033[32mescolha uma opção:\033[m ')
    return opc
