def lin():
    print("="*30)


def soma(a, b):
    s = a + b
    print(f"a soma A + B = {s}")


def contador(* num):
    tam = len(num)
    print(tam)
    for valor in num:
        print(valor, end='')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

#programa principal
lin()
soma(4, 5)
soma(5, 6)
soma(8, 8)
lin()
soma(a=4, b=5)
soma(b=8, a=9)

contador(8,2,5)
contador(8,2)
contador(1)
lin()

valores = [2, 5, 8, 8]
dobra(valores)
print(valores)
