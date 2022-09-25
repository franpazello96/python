from math import factorial

n = int(input("Digite um numero para calcular seu fatoriall"))
f = factorial(n)
print("O fatorial de", n, "é0", f)

#--------------------------------------------

n = int(input("Digite um numero para calcular seu fatoriall"))
contador = n
f = 1
while contador > 0:
    print(contador, end='')
    print(" X " if contador > 1 else " = ", end="")
    contador -= 1
    f *= contador

