palavras = ("aprender", "programar", "linguagem", "python", "futuro")

for p in palavras:
    print(p)
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra)
        