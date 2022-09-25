
def maior(* num):
    cont = maior = 0
    print('='*20)
    print("analisando os valores passados")
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram encontrados {cont} valores ao todo')
    print(f'o maior valor informado foi {maior}')
    print('='*20)


maior(2, 9, 5, 7, 2, 1)
maior(2, 5, 8, 5, )

