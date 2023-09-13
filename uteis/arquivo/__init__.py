from uteis.strings import *


def arqexiste(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileExistsError:
        return False
    finally:
        return True


def arqcriar(name):
    try:
        a = open(name, 'wt+')
        a.close()
    finally:
        pass


def arqler(name):
    try:
        a = open(name, 'rt')
        titulo('Opção 1')
        for c in a:
            dado = c.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]: <21}{dado[1]: >21}')
            a.close()
    finally:
        pass


def cadastrar(arq, name, age):
    try:
        a = open(arq, 'at')
        a.write(f'{name};{age}\n')
    except:
        a.write(f'desconhecido;0\n')
    else:
        print(f'{name} adicionado com sucesso!')
        a.close()
