"""
dada a lista nums = [17,33,23,11,8,15,9] correr a lista e identificar qual o
maior e menos número da mesma
"""

nums = [17,33,23,11,8,15,9]
contador = 0

maior = nums[0]
menor = nums [0]

for num in nums:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(menor, maior)