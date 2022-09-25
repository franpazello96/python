tupla = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
         "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

valor = int(input("digite um valor"))

while True:
    if valor > 20 or valor < 0:
        print("valor invalido, tente novamente")
        valor = int(input("digite um valor"))
    else:
        break
print(tupla[valor])

