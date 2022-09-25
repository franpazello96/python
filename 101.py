def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: Nào vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos o voto é opcional'
    else:
        return f'com {idade} anos o voto obrigatorio'

nasc = int(input("que ano vc naceu?"))
print(voto(nasc))

