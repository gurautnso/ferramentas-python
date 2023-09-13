def titulo(prompt, tam=42):
    if tam == 0:
        tam = len(prompt) + 4
    print(f'{"="*tam}\n{prompt: ^{tam}}\n{"="*tam}')


def lin(tam=42):
    print('='*tam)
