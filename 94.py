pessoa = {}
galera = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input("nome:"))
    while True:
        pessoa["sexo"] = str(input("sexo: M/F")).upper()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F")
    pessoa['idade'] = int(input("idade:"))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
         resp = str(input("quer continuar? s/n")).upper()[0]
         if resp in 'SN':
             break
         print("erro! Responda sim ou nao")
    if resp == "N":
        break
print(f"Ao todo temos {len(galera)} pessoas cadastradas")
media = soma / len(galera)
print(f"a media de idade é de {media:5.2f} anos")
print(f"as mulheres cadastradas foram ", end='')
for p in galera:
    if p['sexo'] in "Ff":
        print(f"{p['nome']}", end="")
print("lista das pessoas que estao acima da media")
for p in galera:
    if p['idade'] >= media:
        print()
        for k,v in p.items():
            print(f"{k} = {v}")
        print()
print("encerrado")