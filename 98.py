from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até o {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush= True)
            sleep(0.5)
            cont += p
        print("Fim")
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p


contador(1, 10, 1)
contador(10, 0, 2)
print('='*20)
print("Agora é a sua vez")
ini = int(input("Inicio"))
fim = int(input("Fim"))
pas = int(input("passo"))
contador(ini, fim, pas)
