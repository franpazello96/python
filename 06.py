""""
Solicitar ao usuario que digite 3 coordenadas x,y armazenando as em uma matriz bidimensional
"""
lista = []

for i in range(3):
    x = int(input("digite o valor de x"))
    y = int(input("digite o valor de y "))
    lista.append([x,y])
print(lista)