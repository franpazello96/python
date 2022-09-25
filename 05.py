import math


def area_circulo(raio):
    return math.pi * raio ** 2


def comprimento_base_circulo(raio):
    return 2 * math.pi = raio

def area_cilindro(altura, raio):
    base = 2 * area_circulo(raio)
    corpo = altura + comprimento_base_circulo(raio)
    return base + corpo

h = float(input("Digite a altura do cilindro"))
r = float(input("Digite o raio da base"))
area = (area_cilindro(h, r))
