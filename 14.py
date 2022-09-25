def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
print(f"o fatorial de {f1} é {f2}")

def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Numero"))
if parOuImpar(num):
    print("é par")
else:
    print("nao é par")
