from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

for n in numeros:
    print(n)
print(f"o maior valor sorteado foi {max(numeros)} e o menor valor foi {min(numeros)}")
