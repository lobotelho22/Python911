# Entrada e Saída de Dados

## Objetivos

- Preparar um ambiente de projeto em Python, definindo sua estrutura de objetos e criando ambientes isolados;
- Instalar bibliotecas de terceiros em um projeto Python;
- Entender como lidar com exceções em Python;
- Receber dados de pessoas usuárias, assim como enviá-los de volta;
- Ler e escrever arquivos no formato tabular `CSV`;
- Serializar e desserializar dados no formato `JSON`.

<br />

## Módulo

<br />

Um módulo é um arquivoque contém definições e instruções em Python. Esses arquivos tem exenção `.py`. De modo geral, qualquer arquivo Python é em si um módulo e pode ser importado por ouro arquivo Python. De forma que estarão disponíveis para utilização suas classes, funções, variáveis, etc.

<br />

## Pacotes

Pacotes são um conjunto de módulos e/ou pacotes, normalmente selecionados para a execução de tarefas similares. *Grosso modo* é uma pasta de arquivos e diretórios que pode conter vários módulos e pacotes.

Utilizamos o comando `import` para importar o pacote como um módulo, ou importar um módulo, constante ou função de um pacote:

```
$ import http # aqui importamos o pacote como um módulo
$from http import client # aqui importamos um módulo de dentro do pacote http
$ from http.client import HTTP_PORT # aqui importamos a variável HTTP_PORT dentro do módulo client que pertence ao módulo http
```

<br />

## Ambiente Virtual

<br />

- `venv`: é um gerenciador de projetos do Python, que permite a utilização simultânea de versões diferentes de um mesmo projeto, em uma mesma máquina. A ideia é que esta ferramente cria ambientes virtuais de produção de projetos;
> Executamos o `venv` através do comando: `python3 -m venv .venv`. Neste caso `.venv` será o nome do ambiente virtual criado.
> Para ativarmos um ambiente vitual para o desenvolvimento de um projeto, devemos repetir esse passo:
>
>> `$source .venv/bin/activate`
>
> Podemos conferir se tudo deu certo, digitando o comando:
>
> >`$ which python3`
>
> O resultado será o caminho da aplicação, acrescido de `.venv/bin/python3`
> 

<br />

## Entrada de Dados: `input()`

<br />

A função `input()` recebe dados de entrada do usuário, por padrão, através do prompt. O valor recebido nessa entrada é do tipo *string*(`str`).

<br />

## Entrada de Dados: módulo `sys`

<br />

Com esse módulo, escrevemos um script para receber dados que ficarão disponíveis no módulo `sys.argv`. O script é conforme o que segue:

<br />

```
import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received ->", argument)
```

<br />

Se chamarmos no prompt a execução: `python3 arquivo.py 2 4 "teste"`, teremos a seguinte saída:


