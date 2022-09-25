listaTemporaria = []
principal = []
maior = menor = 0

while True:
    listaTemporaria.append(str(input("Digite seu nome")))
    listaTemporaria.append(float(input("Digite seu peso")))
    if len(principal) == 0:
        maior = menor = listaTemporaria[1]
    else:
        if listaTemporaria[1] > maior:
            maior = listaTemporaria[1]
        if listaTemporaria[1] < menor:
            menor = listaTemporaria[1]
    principal.append(listaTemporaria[:])
    listaTemporaria.clear()

    resposta = str(input("Deseja continuar"))
    if resposta in "Nn":
        break

print(f"os dados foram{principal}")
print(f"ao todo voce cadastrou {len(principal)}")
for p in principal:
    if p[1] == maior:
        print(f"o peso de {p[0]} é o maior peso")
print(f"o maior peso foi {maior} e o menor foi {menor}")

