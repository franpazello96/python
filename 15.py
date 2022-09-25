num = [2,5,9,1,2,2]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 5)
num.pop()
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print("nao achei o valor")
print(f"essa lista {num}tem {len(num)} elementos")

valores = []

for cont in range(0, 5):
    valores.append(int(input("digite um valor")))

for c, v in enumerate(valores):
    print(f"na aposicao {c} encntrei o valor {v}...",)



