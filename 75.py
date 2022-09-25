num = (int(input("digite o primeiro valor")), int(input("digite o primeiro valor")),
       int(input("digite o primeiro valor")), int(input("digite o primeiro valor")),)

print(f"voce digitou os valor {num}")
print(f"quantas vezes apareceu o valor 9 = {num.count(9)} vezes")
if 3 in num:
    print(f"A Posicao que foi digitado o primeiro valor 3 = {num.index(3)+1}")
else:
    print(f"o valor 3 nao foi digitado em nenhuma posicao")

print(f"os valores pares digitados foram ", end="")
for n in num:
    if n % 2 == 0:
        print(n)

        