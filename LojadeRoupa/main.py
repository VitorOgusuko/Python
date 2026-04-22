from LojadeRoupa.estoque import *
from LojadeRoupa.interface import *
from LojadeRoupa.guardar import *

arquivo = 'Carrinho'
arquivocriar(arquivo)

while True:
    resp = menu(['Calça', 'Camisa', 'Blusa', 'Tênis', 'Acessórios', 'Ver Carrinho', 'Sair'])
    if resp == 1:
        calca()
    elif resp == 2:
        camisa()
    elif resp == 3:
        blusa()
    elif resp == 4:
        tenis()
    elif resp == 5:
        acessorio()
    elif resp == 6:
        linhat('Itens do seu carrinho:')
        lerarquivo(arquivo)
    elif resp == 7:
        break
sair()

