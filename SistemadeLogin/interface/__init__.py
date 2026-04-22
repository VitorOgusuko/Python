#lista de cores
cores = ('\033[m', #0, cor branca
     '\033[31m', #1, cor vermelha
     '\033[32m', #2, cor verde
     '\033[33m', #3, cor amarela
     '\033[34m', #4, cor azul
     '\033[35m', #5, cor rosa
     '\033[36m', #6, cor ciano
     '\033[37m', #7, cor cinza
    )


#verificar se é INTEIRO
def leiaint(txt):
    while True:
        try:
            valor = int(input(txt))
        except ValueError, TypeError:
            print('ERRO, Tente Novamente')
            continue
        except KeyboardInterrupt:
            print('Nenhum valor foi informado')
            continue
        else:
            return valor


#verificar se é STRING
def leiastr(txt):
    while True:
        try:
            valor = str(input(txt))
        except ValueError, TypeError:
            print('ERRO, Tente Novamente')
            continue
        except KeyboardInterrupt:
            print('Nenhum valor foi informado')
            continue
        else:
            return valor


#gerar pequena linha
def linha(tam=40):
    return '-' * tam


def cabeçalho(msg, cor=4):
    print(cores[cor], end='')
    print(linha())
    print(msg.center(40))
    print(linha())
    print(cores[0])


#menu principal
def menu(msg):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in msg:
        print(f'\033[33m{[c]} {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc