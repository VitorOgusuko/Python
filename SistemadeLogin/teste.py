from SistemadeLogin.arquivo import *
from SistemadeLogin.interface import *
import time

arquivo = 'armazem'

if not arquivoexiste(arquivo):
    arquivocriar(arquivo)


while True:
    resp = menu(['Adicionar Nova Pessoa', 'Ver Pessoas Cadastradas', 'Sair'])
    if resp == 1:
        p = leiastr('Informe seu Nome: ')
        i = leiaint('Informe sua Idade: ')
        cadastrar(arquivo, p, i)
    elif resp == 2:
        lerarquivo(arquivo)
    elif resp == 3:
        print('Saindo do Sistema', end='')
        for p in range(3):
            print('.', end='')
            time.sleep(0.5)
        print()
        print('Até Logo')
        break
    else:
        print('Por Favor, informe uma valor válido')
