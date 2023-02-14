# O Terminal Python (REPL)

### Objetivos:

- Apresentar o terminal interativo do Python;
- Apresentar a sintaxe de declaração de variáveis, operadores matemáticos, de comparação e lógicos

<br />

Normalmente, distribuições Linux e Mac já possuem uma versão do Python instalada. Isso acontece porque esses sistemas já utilizam a linguagem em diversos programas essenciais.

Para verificar se o Python já está instalado em sua máquina, basta abrir uma instância do terminal e digitar `python3`. Devemos ter uma saída parecida com a seguinte:

>>> COLOCAR IMAGEM DE RETORNO DO TERMINAL

Esse é o comando que acessa o terminal de leitura-avaliação-impressão da linguagem (**REPL**: *Read-Eval-Print Loop*). Ele cumpre a função de receber uma entrada, avaliar sua execução e imprimir na tela o resultado.

É nesse ambiente que, normalmente, digitamos o "Olá, mundo"(*hello, world*) de uma linguagem de programação. No entanto, em Python isso é um passo tão simples, que podemos deixar de lado.

Comecemos com o seguinte comando:

```
$ import antigravity
```

Ao prosseguirmos com o `enter` seremos transportados a uma tirinha da **xkcd** sobre o Python.

Podemos, também, aproveitarmos e executar o comando abaixo, para acessarmos os princípios básicos da linguagem:

```
$ import this
```

Uma outra coisa que podemos fazer, para tomarmos intimidade com os princípios do Python é ler o documento PEP 8 - Style For Python Code, que pretende-se uma convenção da comunidade, para melhorar a legibilidade do código.

<br />

## Operadores Matemáticos e Lógicos, Declaração de Variáveis

Estes são os operadores matemáticos básicos, na linguagem Python:

```
$ 3 + 1 # soma, saída: 4
$ 3 - 1 # subtração, saída: 2
$ 3 * 2 # multiplicação, saída: 6
$ 3 / 2 # divisão, saída: 1.5
```

> O caractere hashtag(#) indica que é um comentário, na linha de código. Nos nossos exemplos, os comentários normalmente trarão o resultado(saída) do código.

<br />

Na atribuição de variáveis, em Python, não utilizamos nenhuma palavra reservada. Se em JavaScript precisávamos declarar utilizando `let`, `const` ou `var`, aqui apenas denominaremos a variável e igualaremos ao seu valor:

```
$ counter = 0
```

Como em JavaScript, podemos fazer incremento ou decréscimo da variável, mas não podemos utilizar as sintaxes `++` ou `--`. De modo, que faremos da seguinte forma:

```
$ counter += 1 # aqui fazemos o incremento de 1
$ counter -= 15 # aqui fazemos o decréscimo de 15
```

<br />

Outros operadores matemáticos como potenciação, radiciação, quociente e módulo, também podem ser representados em Python:

```
$ 2 ** 3 # potenciação, saída: 8
$ 9 ** (1/2) # utilizamos a radiciação como um operador da potenciação, saída: 3
$ 3 // 2 # quociente, saída: 1
$ 9 % 7 # módulo ou resto, saída: 2
```

<br />

Os operadores de comparação também podem ser representados em Python:

```
$ 3 > 2 # maior que, saída: True
$ 3 < 2 # menor que, saída: False
$ 3 == 2 # igual a, saída: False
$ 3 != 2 # diferente de, saída: True
$ 3 >= 3 # maior ou igual a, saída: True
$ 3 <= 3 # menor ou igual a, saída: True
```

<br />

Os operadores lógicos "e" e "ou" são declarados como `and` e `or`:

```
$ True and False # comparação lógica E, saída: False
$ True or False # comparação lógica OU, saída: True
```

<br />

Finalmente, vamos chegar ao nosso "hello world". É muito simples, basta digitar o seguinte em nosso terminal:

```
print("hello, world!")
```

Well done! Rs