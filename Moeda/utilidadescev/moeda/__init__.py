def metade(preço=0, show=False):
    resp = preço / 2
    return resp if show is False else moeda(resp)


def dobro(preço=0, show=False):
    resp = preço * 2
    return resp if show is False else moeda(resp)


def aumentar(preço=0, taxa=0, show=False):
    """
    -> Calcular o aumento de um determinado preço,
    retornando o resultado som ou sem formatação
    :param preço: o preço que que ser reajustar
    :param taxa: qual é a porcentagem do aumento
    :param show: quer mostrar a saida ou não
    :return: o valor reajustado, com ou sem formato
    """
    resp = preço + (preço * taxa / 100)
    return resp if not show else moeda(resp)


def diminuir(preço=0, taxa=0, show=False):
    resp = preço - (preço * taxa / 100)
    return resp if not show else moeda(resp)


def moeda(preço=0, m='R$'):
    return f'{m}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=13):
    print('-' * 30)
    print('Resumo Do Valor'.center(30))  # print(f'{'Resumo Do Valor':^25}')
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Metade do Preço: \t{metade(preço, True)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
