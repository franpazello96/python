"""
leia o primeiro termo de uma progressao aritmetica
"""
print("GERADOR DE PA")
print("-"*10)
primeiro = int(input("Primeiro termo"))
razao = int(input("Razao"))

termo = primeiro
contador= 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos quer mostrar"))
print("FIM")

