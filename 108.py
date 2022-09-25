num = int(input("Calcule o fatorial"))
primeiroTermo = int(input("Primeiro termo"))
razao = int(input("Razao"))

def fat(n):
    if n == 0:
        return 1
    else:
        return  n * fat(n-1)

print(fat(5))

def pa(a, r , n):
    if n ==1:
        return a
    an = a + r
    if n == 2:
        return an
    else:
        return pa(an, r, n-1)

print(pa, 3, 3, 7)