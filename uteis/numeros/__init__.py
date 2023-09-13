def leiaint(prompt='', style='0', color='31', back='40'):
    """
    -> função para analisar uma variavel é numerica de forma que não de syntaxerror
    :param prompt: pede um numero
    :param style: define o estilo da mensagem de erro no padrão ANSI
    :param color: define a cor da mensagem de erro no padrão ANSI
    :param back: define a cor da mensagem de erro no padrão ANSI
    :return: se for o prompt for numerico vai retormar o prompt em int senão vai ficar perguntando até ser um numero
    """
    while True:
        try:
            num = int(input(prompt).strip())
            return num
        except (TypeError, ValueError):
            print(f'\033[{style};{color};{back}mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[{style};{color};{back}mUsuario preferiu não digitar esse número.\033[m')
            return 0


def leiafloat(prompt='', style='0', color='31', back='40'):
    while True:
        try:
            num = float(input(prompt).replace(',', '.').strip())
            return num
        except (TypeError, ValueError):
            print(f'\033[{style};{color};{back}mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[{style};{color};{back}mUsuario preferiu não digitar esse número.\033[m')
            return 0


def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f
