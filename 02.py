"""
elaborar um programa que solicita ao usuário cinco numeros e exibe duas
listas uma de numeros pares outra de numeros impares
"""
lista = []
impares = []
pares = []

for i in range(5):
    numero = int(input("Digite um valor"))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)