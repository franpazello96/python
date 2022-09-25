
contador = 0
n = 0
soma = n
while True:
    n = int(input("Digite um valor"))
    if n == 999:
        break
    contador +=1
    soma += n
print(f"A soma foi {soma} seu programa rodou {contador}")
