num = [[], [] ]
valor = 0
for c in range(1,8):
    valor = int(input(f"digite o {c} valor"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(num)

num[0].sort()
num[1].sort()

print(num[0])
print(num[1])

