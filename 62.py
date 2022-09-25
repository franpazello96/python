"""
sequencia de fibonatti
"""
n = int(input("Digite quantas vezes voce deseja mostrar"))
t1 = 0
t2 = 1
contador = 3
print("> {} > {}".format(t1, t2))
while contador <= n:
    t3 = t1 + t2
    print(" > {}".format(t3))
    t1 = t2
    t2 = t3
    contador += 1
print("Fim")