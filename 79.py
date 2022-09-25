numeros = []

while True:
    n = int(input("Digite um valor"))
    if n not in numeros:
        numeros.append(n)
        print("valor adicionado com sucesso")
    else:
        print("Valor duplicado, não vou adicionar")
    r =  str(input("Quer continuar"))
    if r in "Nn":
        break
numeros.sort()
print(numeros)