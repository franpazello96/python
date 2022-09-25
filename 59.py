from time import sleep
num1 = int(input("Digite um numero "))
num2 = int(input("Digite um numero"))
while True:
    acao = int(input(""" O que deseja fazer:[1]somar [2] multiplicar [3]maior  [4]novos numero [5]sair do programa """))
    sleep(5)
    if acao == 1:
        print(num1 +  num2)
    elif acao == 2:
        print(num1 * num2)
    elif acao == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    elif acao == 4:
        num1 = int(input("Digite um novo valor"))
        num2 = int(input("Digite um novo valor"))
    elif acao == 5:
        print("Voce saiu")
        break