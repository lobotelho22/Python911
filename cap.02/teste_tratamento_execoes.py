# No exemplo abaixo testamos como funciona uma instrução try / except,
# que lançará o erro sempre que receber um dado inválido
# (uma letra, por exemplo) retornando ao bloco try

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Ooops! That was no valid number. Try Again...")


# exemplo de try com finally ou else. O finally implementa ações de limpezas
# o else acontece sempre que todo o bloco try for bem sucedido

try:
    arquivo = open("arquivo02.txt", "r")
except OSError:
    # caso haja um erro de exceção
    print("arquivo não existe...")
else:
    # correndo tudo bem no try...
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # independente de erro, sempre será executado...
    print("Tentando abrir o arquivo...")
