from rich import print
from rich.panel import Panel

def erro(msg):
    error = f'[red]{msg}[/]'
    return error


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO, tente novamente![/]')
            continue
        except KeyboardInterrupt:
            print('[red]Operação Interrompida[/]')
            break
        else:
            return valor

def leiastr(msg):
    while True:
        try:
            valor = str(input(msg))
        except (ValueError, TypeError):
            print('[red]ERRO, tente novamente![/]')
            continue
        except KeyboardInterrupt:
            print('[red]Operação Interrompida[/]')
            continue
        else:
            return valor


def linha(tam=40):
    return '-' * tam

def linhad(msg):
    print('-'*len(msg))
    print(msg.center(len(msg)))

def menu(txt, c=4):
    conteudo = '[blue][1] - Calça\t\t[2] - Camisa\n'
    conteudo += '[3] - Blusa\t\t[4] - Tênis\n'
    conteudo += '[5] - Acessórios\t[6] - Ver Carrinho\n'
    conteudo += '[7] - Sair[/]'

    print('\n')
    painel = Panel(conteudo, title='Loja de Roupa', width=50, style='yellow')
    print(painel)

    opc = leiaint('O que deseja: ')
    return opc
