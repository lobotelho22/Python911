import sys

# Exercicio 01: Faça um programa que solicite
# o nome de uma pessoa usuária e imprima-o na vertical.

nome = input("Digite seu nome: ")


for letter in nome:
    print(f"{letter}", sep=" ")


# Exercício 02: Escreva um programa que receba vários números naturais e
# calcule a soma desses valores. Caso algum valor da entrada seja inválido
# (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros no
# seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”.
# Ao final, você deve imprimir a soma dos valores válidos.

numbers = input("Digite alguns números, serparando por espaços: ")

numbersArr = numbers.split()
total: int = 0

for number in numbersArr:
    testNumber = number.isdigit()
    if testNumber:
        total += int(number)
    else:
        err_msg = f'{number} é inválido'
        print(f"Erro ao somar valores: {err_msg}", file=sys.stderr)

print(f"A soma dos números informados é {total}")
