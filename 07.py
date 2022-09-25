"""
Solicitar ao usuário que entre com diversos nomes
informando de forma separada nome e ultimo sobrenome

ao final mostrar uma lista de nomes no formato
sobrenome,nome
para encerrar a entrada de dados basta o usuario inserir no nome
o texto sair
"""
lista = []

while True:
    nome = str(input("digite seu nome")).upper()
    if nome == "SAIR":
       break
    else:
        sobrenome = str(input("digite seu sobrenome"))
        lista.append([sobrenome, nome])
print(lista)