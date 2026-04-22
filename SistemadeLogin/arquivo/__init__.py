#verificar se o arquivo existe
def arquivoexiste(nome):
    try:
        a =  open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


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
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>4}')
    finally:
        a.close()


#cadastrar no arquivo criado
def cadastrar(nome, pessoa='<desconhecido>', idade=0):
    try:
        a = open(nome, 'at')
    except:
        print('Erro ao cadastrar')
    else:
        try:
            a.write(f'{pessoa};{idade}\n')
        except:
            print('Não foi possivel cadastrar')
        else:
            print(f'Pessoa \"{pessoa}\" cadastrada')
            a.close()