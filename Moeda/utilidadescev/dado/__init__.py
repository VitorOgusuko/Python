def leiadinheiro(prec, ok=False):
    ok = False
    while not ok:
        p = str(input(prec)).replace(',', '.').strip()
        if p .isalpha() or p == '':
            print(f'\033[31mERRO: \'{p}\' é um preço inválido\033[m')
        else:
            ok = True
            return float(p)
