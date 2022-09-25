num = []
pares = []
impares = []

while True:
    num.append(int(input("Digite um valor")))
    resposta = str(input("Quer continuar"))
    if resposta in "Nn":
        break

for posicao, numerodalista in enumerate(num):
    if numerodalista % 2 == 0:
        pares.append(numerodalista)
    elif numerodalista % 2 == 1:
        impares.append(numerodalista)

print(num)
print(pares)
print(impares)