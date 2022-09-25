def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/ len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = "boa"
        elif r['media'] >= 5:
            r['situacao'] = 'razoavel'
        else:
            r['situacao'] = 'ruim'
    return r



resposta = notas (5, 6, 8, 8, sit=True)
print(resposta)