# Exercício 1: Dada uma lista, descubra o menor elemento.
# Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.

lista = [5, 9, 3, 19, 70, 8, 100, 2, 35, 2]


def retornaMenor(lista: list):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor


print(retornaMenor(lista))

# Exercício 2: Faça um programa que, dado um valor n qualquer,
# tal que n > 1, imprima na tela um triângulo retângulo com n
# asteriscos de base. Por exemplo, para n = 5 o triângulo terá 5
# asteriscos na base:

n = 7
line = 1


for num in range(n):
    print(line * "*")
    line += 1


# Exercício 3: Crie uma função que receba um número inteiro N e
# retorne o somatório de todos os números de 1 até N. Por exemplo,
# para N = 5, o valor esperado será 15.

n = 5
total = 0

for num in range(1, n + 1):
    total += num

print(total)

# Exercício 4: Um posto está vendendo combustíveis com a
# seguinte tabela de descontos:

#  Álcool:
#    - Até 20 litros, desconto de 3% por litro;
#    - Acima de 20 litros, desconto de 5% por litro.
#  Gasolina:
#    - Até 20 litros, desconto de 4% por litro;
#    - Acima de 20 litros, desconto de 6% por litro.

# Escreva uma função que receba o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A - álcool,
# G - gasolina), e retorne o valor a ser pago pelo cliente,
# sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço
# do litro do álcool é R$ 1,90.

combustivel = "G"
consumo = 36


def calculoCombustivel(combustivel: str, consumo: float):
    if combustivel == "A":
        litroAlcool = 1.90
        if consumo <= 20:
            desconto = 1 - 0.03
        else:
            desconto = 1 - 0.05

        return (litroAlcool * desconto) * consumo

    if combustivel == "G":
        litroGasolina = 2.50
        if consumo <= 20:
            desconto = 1 - 0.04
        else:
            desconto = 1 - 0.06

        return (litroGasolina * desconto) * consumo


print(calculoCombustivel(combustivel, consumo))
