""""
Dada a matriz m= [[1,2,3], [4,5,6],[7,8,9]]
efetuar a soma de todos os seus elementos e exibir o resultado
"""

m = [[1,2,3], [4,5,6],[7,8,9]]
soma = 0

for i in range(3):
    for j in range(3):
        soma += m[i][j]
print(soma)