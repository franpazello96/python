pessoas = {'nome': 'fran', 'sexo': 'feminino', 'idade': 22 }
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-'*30)
for k in pessoas.keys():
    print(k)
print('-'*30)
for v in pessoas.values():
    print(v)
print('-'*30)
for k, v in pessoas.items():
    print(k, v)
print('-'*30)
del pessoas['sexo']
print(pessoas)
print('-'*30)
pessoas['nome'] = 'teste'
pessoas['peso'] = 98
print(pessoas)
print('-'*30)
estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'sao paulo', 'sigla': 'sp'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print('-'*30)
"""
dados = {"nome": "pedro", "idade": 25}
print(dados["nome"])
print(dados["idade"])
dados["sexo"] = "masculino"
print(dados)
del dados["idade"]
print(dados)
filme = {
    "titulo": "Star wars",
    "ano": 1977,
    "direto": "george lucas"
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(k, v)


    estado = {}
brasil = []

for c in range(0,3):
    estado ['ufc']  = str(input('unidade federativa'))
    estado['sigla'] = str(input("sigla do estado"))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print()
print(brasil)
"""

