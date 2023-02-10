import math

# Exercício 1: crie uma função que receba dois números e retorne o maior deles


def retornaMaior(x: int, y: int):
    """A funçaõ recebe dois números e retorna o maior deles"""
    if x > y:
        return print(f"{x} é o maior número")
    elif x < y:
        return print(f"{y} é o maior número")
    else:
        return print("os dois são iguais")


retornaMaior(9, 4)

# Exercício 2: crie um função que calcule a média aritmética dos
# números contidos em uma lista

lista_num = list(range(1, 652))


def calcula_media(lista: list):
    """A função calcula a média aritmética de números em uma lista"""
    total = 0
    lista_len = lista.__len__()

    for num in lista:
        total += num

    media = total / lista_len

    return print(f"A média dos números dessa lista é: {media}")


calcula_media(lista_num)

# Exercício 3: Faça um programa que, dado um valor n qualquer,
# tal que n > 1, imprima na tela um quadrado feito de asteriscos
# de lado de tamanho n.

n = 3


def returnSquare(n: int):
    for line in range(n):
        print(n * "*")


returnSquare(n)

# 🚀 Exercício 4: Crie uma função que receba uma lista de nomes
# e retorne o nome com a maior quantidade de caracteres.
# Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda",
# "Cairo", "Joana"], o retorno deve ser "Fernanda".

namelist = ["José", "Lucas", "Nádia", "Fernanda", "Pin", "Joana"]


def returnMaiorNome(nameList: list):
    maiorNome = ""
    for name in nameList:
        if len(name) > len(maiorNome):
            maiorNome = name
    return maiorNome


print(returnMaiorNome(namelist))


# Exercício 5: Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Crie uma função que retorne dois valores em uma tupla contendo
# a quantidade de latas de tinta a serem compradas e o preço
# total a partir do tamanho de uma parede (em m²).

area = 156.2


def calcularTinta(area: float):
    rendimento = 1 / 3
    litrosUtilizados = area * rendimento
    galaoVolume = 18.0
    galao_price = 80.0
    galoesTotais = math.ceil(litrosUtilizados / galaoVolume)
    valorTotal = galoesTotais * galao_price
    return tuple((galoesTotais, valorTotal))


print(calcularTinta(area))

# Exercício 6: Crie uma função que receba os três lado de um
# triângulo e informe qual o tipo de triângulo formado ou
# "não é triangulo", caso não seja possível formar um triângulo.

a = 3
b = 3
c = 5


def classificaTriangulo(a: float, b: float, c: float):
    isTriangle = a + b > c and a + c > b and b + c > a
    if isTriangle:
        if a == b == c:
            print("Triângulo equilátero")
        elif a == b or a == c or b == c:
            print("Triângulo isósceles")
        else:
            print("Triângulo escaleno")
    else:
        print("Não é triângulo")


classificaTriangulo(a, b, c)
