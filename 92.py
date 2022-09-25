"""
Crie um programa que leia nome, amo de nascimento, e carteira de trabalho
e cadastre com a idade se por acoso a CTPS for diferente de zero
o dicionario recebera tambem o ano de contratacao e o salario
calcule e acrescente alem da idade com quantos anos a pessoa vai se aposentar
"""
from datetime import datetime
dados = {}

dados["nome"] = str(input("Digite seu nome: "))
nascimento = int(input("ano de nascimento"))
dados["idade"] = datetime.now().year - nascimento
dados["ctps"] = int(input("Carteira de trabalho (0 nao tem) "))

if dados["ctps"] != 0:
    dados["contratacao"] = int(input("ano de contratacao "))
    dados["salario"] = float(input("salario"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f"{k} tem o valor {v}")
