from random import randint
cont = 0
lista = []
total = 1
jogos = []
quantidade = int(input("quantos jogos deseja?"))

while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total +=1
print(lista)

