lanche = ("hamburgue", "suco", "pizza", "pudim ")
for contador in range(0, len(lanche)):
    print(lanche[contador], contador)

for pos, comida in enumerate(lanche):
    print(comida, pos)

print(sorted(lanche)) #colocar a tupla em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
