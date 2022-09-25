""""
Elaborar um programa que solicita ao usuário cinco numeros, armazena-os em uma lista, exibindo como resultado 
os dados obtidos
"""""
lista = []

for i in range(5):
    lista.append(int(input("Digite um numero")))
print(lista)