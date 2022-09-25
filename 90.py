situacao = {}

situacao["nome"] = str(input("Digite o nome do aluno"))
situacao["nota"] = float(input("Digite a nota do aluno"))

if situacao["nota"] >= 70:
    situacao["situacao"] = "aprovado"
else:
    situacao["situacao"] = "reprovado"

for k, v in situacao.items():
    print(f"o {k} é igual a {v} ")

