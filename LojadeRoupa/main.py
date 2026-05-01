from LojadeRoupa.estoque import *
from LojadeRoupa.interface import *
from LojadeRoupa.guardar import *

arquivo = 'Carrinho'
arquivocriar(arquivo)

while True:
    resp = menu()
    os.system('cls')
    if resp == 1:
        calca()
        os.system('cls')
    elif resp == 2:
        camisa()
        os.system('cls')
    elif resp == 3:
        blusa()
        os.system('cls')
    elif resp == 4:
        tenis()
        os.system('cls')
    elif resp == 5:
        acessorio()
        os.system('cls')
    elif resp == 6:
        linhad('Itens do seu carrinho:')
        lerarquivo(arquivo)
    elif resp == 7:
        break
sair()

