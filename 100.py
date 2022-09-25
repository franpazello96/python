from random import randint

def sorteio(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    print('PRONTO')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(f'somando os valores pares da {lista}, temos {soma}')


numeros = []
sorteio(numeros)
somaPar(numeros)