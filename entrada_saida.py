import random
import sys

random_number = random.randint(1, 10)

guess = ""

print("O Acerte o palpite utiliza a função input()")

while guess != random_number:
    guess = int(input("Qual é o seu palpite? "))

print(f"Parabéns, o número era {random_number}")

print(
    "O módulo sys imprime os argumentos " +
    "recebidos na linha de execução do arquivo"
)


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)


print("Podemos fazer atribuição de variáveis por desempacotamento de valores.")

print("Por exemplo: a, *b = 'cde', verifique a saída:")

a, *b = "cde"

print(f'a = {a}')
print(f'b = {b}')
