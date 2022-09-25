num = []
maior = 0
menor = 0

for c in range(0, 5):
    num.append(int(input("digite os valores")))
    print(num[c])
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(maior)
for i, v in enumerate(num):
    if v == maior:
        print(f"{i}")

print(num)

print(menor)
for i, v in enumerate(num):
    if v == menor:
        print(f"{i}")
