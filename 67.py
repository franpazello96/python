valor = 1
mult = 1

while True:
    valor = int(input("quer ver a tabuada de qual valor?"))
    if valor < 0:
        break
    for c in range(1, 11):
        mult = valor * c
        print(f"{valor} X {c} = {mult}")
print("Acabou")
