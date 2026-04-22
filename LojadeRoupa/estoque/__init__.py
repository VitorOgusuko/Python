from time import sleep
from LojadeRoupa.interface import *
from LojadeRoupa.guardar import *

arquivo = 'Carrinho'

def rosa(c=5):
    return cores[c]

def tirarrosa(c=0):
    return cores[c]



#gerar estoque de calças
def calca():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = {'36':'(PP) Cintura fina', '39':'(P) Pequeno', '42':'(M) Médio', '44':'(G) Grande', '48':'(GG/XG) Extra Grande','52':'(EXG): Especial'}
    lista = {'1':'Calça Jeans', '2':'Calça Moletom', '3':'Calça Cargo', '4':'Calça Casual'}

    print('As opções de Calças são: ')

    print(rosa(), end='')
    for k, v in lista.items():
        print(f'[{k}] para {v}')
    print(tirarrosa(), end='')

    while True:
        n = leiastr('Qual a sua opção ? ')
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ? ')
            certo = leiastr('Confirme [S/N] ').upper().strip()
            if certo in 'Sn':
                break
            else:
                print(erro(), end='')
                print('Cancelado')
                print(pararerro(), end='')

    linhat(f'Tamanhos de {lista[n]} Disponíveis:')
    print(rosa(), end='')
    for k, v in ta.items():
        print(f'{k} {v}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 15)
        t = leiastr('Qual Tamanho ? ')
        if t in ta:
            print(f'Você escolheu \"{ta[t]}\" correto ? ')
            certo = leiastr('Confirme [S/N] ').upper().strip()
            if certo in 'Sn':
                break
            else:
                print(erro(), end='')
                print('Cancelado')
                print(pararerro(), end='')


    linhat('Cores Disponíveis:')
    print(rosa(), end='')
    for c in range(0, len(cor)):
        if c % 2 == 0:
            print(f'{cor[c]:<20}', end='')
        else:
            print(f'{cor[c]:>3}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor ? ').title().strip()
        if e in cor:
            break
        else:
            print(erro(), end='')
            print(f'Cor {e} fora de estoque')
            print(pararerro(), end='')

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print(f'Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)


#gerar estoque de camisas
def camisa():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = {'PP':'Extra Pequeno', 'P':'Pequeno', 'M':'Médio', 'G':'Grande', 'GG':' Extra Grande', 'EG':'Extra Extra Grande'}
    lista = {'1':'Camisa Regata', '2':'Camisa Manga Longa', '3':'Camisa Manga Curta', '4':'Camisa Justa', '5':'Camisa Formal'}

    print('Os tipos de camisas disponíveis são: ')

    print(rosa(), end='')
    for k, v in lista.items():
        print(f'[{k}] para {v}')
    print(tirarrosa(), end='')

    while True:
        n = leiastr('Sua escolha: ')
        if n in lista.keys():
            print(f'Você selecionou \"{lista[n]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print(erro(), end='')
                print('Cancelado')
                print(pararerro(), end='')



    linhat(f'Tamanhos de {lista[n]} disponíveis: ')
    print(rosa(), end='')
    for k, v in ta.items():
        print(f'[{k}] {v}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 15)
        t = leiastr('Qual Tamanho: ').upper().strip()
        if t in ta:
            print(f'Você selecionou \"{ta[t]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
        else:
            print(erro(), end='')
            print(f'Tamanho {t} fora de estoque')
            print(pararerro(), end='')


    linhat(f'Cores de {lista[n]} Disponíveis:')
    print(rosa(), end='')
    for c in range(0, len(cor)):
        if c % 2 == 0:
            print(f'{cor[c]:<20}', end='')
        else:
            print(f'{cor[c]:>3}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor: ').title().strip()
        if e in cor:
            break
        else:
            print(erro(), end='')
            print(f'Cor {e} fora de estoque')
            print(pararerro(), end='')

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print(f'Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)


#gerar estoque de blusas
def blusa():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = {'PP':'Extra Pequeno', 'P':' Pequeno', 'M':'Médio', 'G':'Grande:', 'GG':'Extra Grande', 'EG':'Extra Extra Grande'}
    lista = {'1':'Blusa Canguru', '2':'Blusa Careca', '3':'Blusa com Capuz', '4':'Blusa sem Capuz', '5':'Blusa Com Ziper'}

    print('As Blusas disponíveis são:')

    print(rosa(), end='')
    for k, v in lista.items():
        print(f'[{k}] para {v}')
    print(tirarrosa(), end='')

    while True:
        n = leiastr('Sua escolha: ')
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print(erro(), end='')
                print('Cancelado')
                print(pararerro(), end='')


    linhat(f'Tamanhos de {lista[n]} Disponíveis:')
    print(rosa(), end='')
    for k, v in ta.items():
        print(f'[{k}] {v}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 15)
        t = leiastr('Qual tamanho ? ').upper().strip()
        if t in ta:
            print(f'Você escolheu \"{ta[t]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
        else:
            print(erro(), end='')
            print(f'Tamanho {t} fora de estoque')
            print(pararerro(), end='')

    linhat(f'Cores de {lista[n]} Disponíveis:')
    print(rosa(), end='')
    for c in range(0, len(cor)):
        if c % 2 == 0:
            print(f'{cor[c]:<20}', end='')
        else:
            print(f'{cor[c]:>3}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor: ').title().strip()
        if e in cor:
            break
        else:
            print(erro(), end='')
            print(f'Cor {e} fora de Estoque')
            print(pararerro(), end='')

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print('Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)

#gerar estoque de Tênis
def tenis():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = (34, 35, 36, 37, 38, 39, 40, 41)
    lista = {'1':'Tênis Esportivo', '2':'Tênis Casual', '3':'Tênis Formal'}

    print('Os Tênis disponíveis são:')

    print(rosa(), end='')
    for k, v in lista.items():
        print(f'[{k}] para {v}')
    print(tirarrosa() ,end='')

    while True:
        n = leiastr('Sua Escolha: ').upper().strip()
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ?')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print(erro(), end='')
                print('Cancelado')
                print(pararerro(), end='')


    linhat(f'Os tamanhos de {lista[n]} Disponíveis:')
    print(rosa(), end='')
    for c in range(0, len(ta)):
        if c % 2 == 0:
            print(f'{ta[c]:<20}', end='')
        else:
            print(f'{ta[c]:>3}')
    print(tirarrosa(), end='')

    while True:
        print('-' *15)
        t = leiaint('Qual tamanho ? ')
        if t in ta:
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
        else:
            print(erro(), end='')
            print(f'Tamanho {t} fora de estoque')
            print(pararerro(), end='')

    linhat('Cores de {lista[n]} Disponíveis:')
    print(rosa(), end='')
    for c in range(0, len(cor)):
        if c % 2 == 0:
            print(f'{cor[c]:<20}', end='')
        else:
            print(f'{cor[c]:>3}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor: ').title().strip()
        if e in cor:
            break
        else:
            print(erro(), end='')
            print(f'Cor {e} fora de Estoque')
            print(pararerro(), end='')

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print('Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)


#gerar estoque de acessórios
def acessorio():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    lista = {'1':'Óculos', '2':'Brinco', '3':'Corrente', '4':'Bracelete', '5':'Pingente', '6':'Toca', '7':'Chapéu'}

    print('Os Acessórios disponíveis são:')

    print(rosa(), end='')
    for k, v in lista.items():
        print(f'[{k}] para {v}')
    print(tirarrosa(), end='')

    while True:
        n = leiastr('Sua Escolha: ').upper().strip()
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ?')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print(erro(), end='')
                print('Cancelado')
                print(pararerro(), end='')


    linhat(f'As cores de {lista[n]} Disponívei:')
    print(rosa(), end='')
    for c in range(0, len(cor)):
        if c % 2 == 0:
            print(f'{cor[c]:<20}', end='')
        else:
            print(f'{cor[c]:>3}')
    print(tirarrosa(), end='')

    while True:
        print('-' * 12)
        e = leiastr('Qual cor ? ').title().strip()
        if e in cor:
            break
        else:
            print(erro(), end='')
            print(f'Cor \"{e}\" fora de estoque')
            print(pararerro(), end='')

    linhat(f'Produto: {lista[n]}')
    print(f'Cor: {e}')
    print('Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, produto=lista[n], cor=e)


#sair do sistema
def sair():
    print(rosa(), end='')
    print('-' *17)
    print('Saindo do Sistema', end='')
    for c in range(3):
        print('.', end='')
        sleep(0.5)
    print()
    print('Até Logo')
    print(tirarrosa(), end='')


