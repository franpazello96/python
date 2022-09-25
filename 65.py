continuar = "S"
contador = 0
num = 0
media = num
maior = menor = num

while continuar == "S":
    num = int(input("Digite um valor"))
    continuar = str(input("Deseja continuar S/N")).upper()
    contador += 1
    media = media + num
    if contador == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if continuar == "N":
      media = media/ contador

print(media, maior, menor)