from LojadeRoupa.interface import *


#criar o arquivo se não existe
def arquivocriar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Nao foi possivel criar o arquivo')
    else:
        print(f'Arquivo \"{nome}\" criado')


#ler o arquivo criado
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Não foi possivel ler o arquivo {nome}')
    else:
        for l in a:
            dado = l.split(';')
            print(f'{dado[0]:<20}{dado[1]:>4}{dado[2]:>10}')
    finally:
        a.close()


#cadastrar no arquivo criado
def cadastrar(nome, produto='', tamanho='', cor=''):
    try:
        a = open(nome, 'at')
    except:
        print('Erro ao cadastrar')
    else:
        try:
            a.write(f'{produto};{tamanho};{cor}\n')
        except:
            print('Não foi possivel cadastrar')
        else:
            a.close()