cores = ('\033[m', #0, cor branca
     '\033[31m', #1, cor vermelha
     '\033[32m', #2, cor verde
     '\033[33m', #3, cor amarela
     '\033[34m', #4, cor azul
     '\033[35m', #5, cor rosa
     '\033[36m', #6, cor ciano
     '\033[37m', #7, cor cinza
    )

def erro(c=1):
    return cores[c]

def pararerro(c=0):
    return cores[0]

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(erro(), end='')
            print('ERRO, tente novamente!')
            print(pararerro(), end='')
            continue
        except KeyboardInterrupt:
            print(erro(), end='')
            print('Operação Interrompida')
            print(pararerro(), end='')
            break
        else:
            return valor

def leiastr(msg):
    while True:
        try:
            valor = str(input(msg))
        except (ValueError, TypeError):
            print(erro(), end='')
            print('ERRO, tente novamente!')
            print(pararerro(), end='')
            continue
        except KeyboardInterrupt:
            print(erro(), end='')
            print('Operação Interrompida')
            print(pararerro(), end='')
            continue
        else:
            return valor


def linha(tam=40):
    return '-' * tam

def linhad(tam=40):
    return '=' * tam

def linhat(msg):
    print('-'*len(msg))
    print(msg.center(len(msg)))


def cabeçalho(txt, c=3):
    print(cores[c], end='')
    print(linha())
    print(txt.center(40))
    print(linha())
    print(cores[0], end='')

def menu(txt, c=4):
    cabeçalho('LOJA DE ROUPA')
    print(cores[c], end='')
    c = 1
    for item in txt:
        print(f'[{c}] para {item}')
        c += 1
    print(linha())
    print(cores[0], end='')
    opc = leiaint('O que deseja: ')
    return opc
