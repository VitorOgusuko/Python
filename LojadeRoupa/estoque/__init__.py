from time import sleep
from LojadeRoupa.interface import *
from LojadeRoupa.guardar import *
from rich import print
import os

arquivo = 'Carrinho'


#gerar estoque de calças
def calca():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = {'36':'(PP) Cintura fina', '39':'(P) Pequeno', '42':'(M) Médio', '44':'(G) Grande', '48':'(GG/XG) Extra Grande','52':'(EXG): Especial'}
    lista = {'1':'Calça Jeans', '2':'Calça Moletom', '3':'Calça Cargo', '4':'Calça Casual'}

    conteudo = '[yellow]As Opções de Calças são:\n'
    conteudo += '[1] para Calça Jeans\t[2] para Calça Moletom\n'
    conteudo += '[3] para Calça Cargo\t[4] para Calça Casual[/]'

    painel = Panel(conteudo, title='Calças', width=60, style='green')
    print(painel)

    while True:
        n = leiastr('Qual a sua opção ? ')
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ? ')
            certo = leiastr('Confirme [S/N] ').upper().strip()
            if certo in 'Sn':
                break
            else:
                print('[red]Cancelado[/]')
    os.system('cls')

    linha()
    conteudo = f'[yellow]Tamanhos de \"{lista[n]}\" Disponíveis:\n'
    conteudo +='36 (PP) Cintura fina\t  39 (P) Pequeno\n'
    conteudo += '42 (M) Médio\t\t  44 (G) Grande\n'
    conteudo += '48 (GG/XG) Extra Grande\t  52 (EXG): Especial[/]'

    painel = Panel(conteudo, title='Tamanhos de Calça', width=60, style='green')
    print(painel)


    while True:
        print('-' * 15)
        t = leiastr('Qual Tamanho ? ')
        if t in ta:
            print(f'Você escolheu \"{ta[t]}\" correto ? ')
            certo = leiastr('Confirme [S/N] ').upper().strip()
            if certo in 'Sn':
                break
            else:
                print('[red]Cancelado[/]')
    os.system('cls')


    linha()
    conteudo = f'[yellow]Cores de \"{lista[n]}\" Disponíveis\n'
    conteudo += 'Branco\t\tPreto\n'
    conteudo += 'Vermelho\tVerde\n'
    conteudo += 'Amarelo\t\tAzul\n'
    conteudo += 'Rosa\t\tCinza\n'
    conteudo += 'Roxo\t\tLaranja[/]'

    painel = Panel(conteudo, title='Cores de Calça', width=40, style='green')
    print(painel)

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor ? ').title().strip()
        if e in cor:
            break
        else:
            print(f'[red]Cor {e} fora de estoque[/]')
            

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print(f'Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)
     os.system('cls')
    

#gerar estoque de camisas
def camisa():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = {'PP':'Extra Pequeno', 'P':'Pequeno', 'M':'Médio', 'G':'Grande', 'GG':' Extra Grande', 'EG':'Extra Extra Grande'}
    lista = {'1':'Camisa Regata', '2':'Camisa Manga Longa', '3':'Camisa Manga Curta', '4':'Camisa Justa', '5':'Camisa Formal'}

    conteudo = '[yellow]Os Tipos de Camisa disponíveis são:\n'
    conteudo += '[1] - Camisa Regata\t\t[2] - Camisa Manga Longa\n'
    conteudo += '[3] - Camisa Manga Curta\t[4] - Camisa Justa\n'
    conteudo += '[5] - Camisa Formal[/]'

    painel = Panel(conteudo, title='Camisas', width=70, style='green')
    print(painel)

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
    os.system('cls')


    conteudo = f'[yellow]Tamanhos de \"{lista[n]}\" disponíveis:\n'
    conteudo += '[PP] - Extra Pequeno\t [P] - Pequeno\n'
    conteudo += '[M] - Médio\t\t [G] - Grande\n'
    conteudo += '[GG] - Extra Grande\t [EG] - Extra Extra Grande[/]'

    painel = Panel(conteudo, title='Tamanhos de Camisas', width=60, style='green')
    print(painel)

    while True:
        print('-' * 15)
        t = leiastr('Qual Tamanho: ').upper().strip()
        if t in ta:
            print(f'Você selecionou \"{ta[t]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
        else:
            print(f'[red]Tamanho {t} fora de estoque[/]')
     os.system('cls')

    conteudo = f'[yellow]Cores de \"{lista[n]}\" Disponíveis:\n'
    conteudo += 'Branco\t\tPreto\n'
    conteudo += 'Vermelho\tVerde\n'
    conteudo += 'Amarelo\t\tAzul\n'
    conteudo += 'Rosa\t\tCinza\n'
    conteudo += 'Roxo\t\tLaranja[/]'

    painel = Panel(conteudo, title='Cores de Camisas', width=60, style='green')
    print(painel)

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor: ').title().strip()
        if e in cor:
            break
        else:
            print(f'[red]Cor {e} fora de estoque[/]')
            

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print(f'Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)
    os.system('cls')


#gerar estoque de blusas
def blusa():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = {'PP':'Extra Pequeno', 'P':' Pequeno', 'M':'Médio', 'G':'Grande:', 'GG':'Extra Grande', 'EG':'Extra Extra Grande'}
    lista = {'1':'Blusa Canguru', '2':'Blusa Careca', '3':'Blusa com Capuz', '4':'Blusa sem Capuz', '5':'Blusa Com Ziper'}

    conteudo = '[yellow]Os Tipos de Blusas disponíveis são:\n'
    conteudo += '[1] - Blusa Canguru\t\t[2] - Blusa Careca\n'
    conteudo += '[3] - Blusa com Capuz\t\t[4] - Blusa sem Capuz\n'
    conteudo += '[5] - Blusa Com Ziperl[/]'

    painel = Panel(conteudo, title='Blusas', width=70, style='green')
    print(painel)

    while True:
        n = leiastr('Sua escolha: ')
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print('[red]Cancelado[/]')
    os.system('cls')

    conteudo = f'[yellow]Tamanhos de \"{lista[n]}\" disponíveis:\n'
    conteudo += '[PP] - Extra Pequeno\t [P] - Pequeno\n'
    conteudo += '[M] - Médio\t\t [G] - Grande\n'
    conteudo += '[GG] - Extra Grande\t [EG] - Extra Extra Grande[/]'

    painel = Panel(conteudo, title='Tamanhos de Blusa', width=60, style='green')
    print(painel)

    while True:
        print('-' * 15)
        t = leiastr('Qual tamanho ? ').upper().strip()
        if t in ta:
            print(f'Você escolheu \"{ta[t]}\" correto ? ')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
        else:
            print(f'[red]Tamanho {t} fora de estoque[/]')
          

    os.system('cls')

    conteudo = f'[yellow]Cores de \"{lista[n]}\" Disponíveis:\n'
    conteudo += 'Branco\t\tPreto\n'
    conteudo += 'Vermelho\tVerde\n'
    conteudo += 'Amarelo\t\tAzul\n'
    conteudo += 'Rosa\t\tCinza\n'
    conteudo += 'Roxo\t\tLaranja[/]'

    painel = Panel(conteudo, title='Cores de Blusa', width=50, style='green')
    print(painel)

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor: ').title().strip()
        if e in cor:
            break
        else:
            print(f'[red]Cor {e} fora de Estoque[/]')
           

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print('Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)
    os.system('cls')


#gerar estoque de Tênis
def tenis():
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    ta = (34, 35, 36, 37, 38, 39, 40, 41)
    lista = {'1':'Tênis Esportivo', '2':'Tênis Casual', '3':'Tênis Formal'}

    conteudo = '[yellow]Os Tipos de Tênis disponíveis são:\n'
    conteudo += '[1] - Tênis Esportivo\n'
    conteudo += '[2] - Tênis Casual\n'
    conteudo += '[3] - Tênis Formal[/]'

    painel = Panel(conteudo, title='Tênis', width=40, style='green')
    print(painel)

    while True:
        n = leiastr('Sua Escolha: ').upper().strip()
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ?')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print('[red]Cancelado[/]')
    os.system('cls')
    

    conteudo = f'[yellow]Tamanhos de \"{lista[n]}\" disponíveis:\n'
    conteudo += '34 \t\t35\n'
    conteudo += '36 \t\t37\n'
    conteudo += '38 \t\t39\n'
    conteudo += '40 \t\t41\n'

    painel = Panel(conteudo, title='Tamanhos de Tênis', width=40, style='green')
    print(painel)

    while True:
        print('-' *15)
        t = leiaint('Qual tamanho ? ')
        if t in ta:
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
        else:
            print(f'[red]Tamanho {t} fora de estoque[/]')
    os.system('cls')

    conteudo = f'[yellow]Cores de \"{lista[n]}\" Disponíveis:\n'
    conteudo += 'Branco\t\tPreto\n'
    conteudo += 'Vermelho\tVerde\n'
    conteudo += 'Amarelo\t\tAzul\n'
    conteudo += 'Rosa\t\tCinza\n'
    conteudo += 'Roxo\t\tLaranja[/]'

    painel = Panel(conteudo, title='Cores de Tênis', width=50, style='green')
    print(painel)

    while True:
        print('-' * 12)
        e = leiastr('Qual Cor: ').title().strip()
        if e in cor:
            break
        else:
            print(f'[red]Cor {e} fora de Estoque[/]')
            

    linhat(f'Produto: {lista[n]}')
    print(f'Tamanho: {t}')
    print(f'Cor: {e}')
    print('Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, lista[n], t, e)
    os.system('cls')


#gerar estoque de acessórios
def acessorio():
    print(linhad())
    cor = ('Branco', 'Preto', 'Vermelho', 'Verde', 'Amarelo', 'Azul', 'Rosa', 'Cinza', 'Roxo', 'Laranja')
    lista = {'1':'Óculos', '2':'Brinco', '3':'Corrente', '4':'Bracelete', '5':'Pingente', '6':'Toca', '7':'Chapéu'}

    conteudo = '[yellow]Os Acessórios Disponíveis são:\n'
    conteudo += '[1] - Óculos\t[2] - Brinco\n'
    conteudo += '[3] - Corrente\t[4] - Bracelete\n'
    conteudo += '[5] - Pingente\t[6] - Brinco\n'
    conteudo += '[7] - Chápeu\n'

    painel = Panel(conteudo, title='Acessórios', width=40, style='green')
    print(painel)

    while True:
        n = leiastr('Sua Escolha: ').upper().strip()
        if n in lista.keys():
            print(f'Você escolheu \"{lista[n]}\" correto ?')
            certo = leiastr('Confirmar [S/N] ').upper().strip()
            if certo in 'Ss':
                break
            else:
                print('[red]Cancelado[/]')
    os.system('cls')

    conteudo = f'[yellow]Cores de \"{lista[n]}\" Disponíveis:\n'
    conteudo += 'Branco\t\tPreto\n'
    conteudo += 'Vermelho\tVerde\n'
    conteudo += 'Amarelo\t\tAzul\n'
    conteudo += 'Rosa\t\tCinza\n'
    conteudo += 'Roxo\t\tLaranja[/]'

    painel = Panel(conteudo, title=f'{lista[n]}', width=50, style='green')
    print(painel)

    while True:
        print('-' * 12)
        e = leiastr('Qual cor ? ').title().strip()
        if e in cor:
            break
        else:
            print(f'[red]Cor \"{e}\" fora de estoque[/]')
          

    linhat(f'Produto: {lista[n]}')
    print(f'Cor: {e}')
    print('Carrinho Atualizado')
    print(linhad())

    cadastrar(arquivo, produto=lista[n], cor=e)
    os.system('cls')


#sair do sistema
def sair():
    print('[yellow]-' *17)
    print('Saindo do Sistema', end='')
    for c in range(3):
        print('.', end='')
        sleep(0.5)
    print()
    print('Até Logo')
    


