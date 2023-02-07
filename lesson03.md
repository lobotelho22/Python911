# Tipos de Dados em Python

Veremos agora os tipos de dados inerentes (*buit-in*) da linguagem Python:

<br />

## Tipos Numéricos:

<br />

> Booleanos (*bool*)

Os valores `True` e `False` pertencem ao tipo `bool`. Podemos atribuir o valor a uma variável, exemplo: `real = True`.

<br />

> Números Inteiros (*int*)

São todos os valores numéricos que não possuem a parte decimal. `5` ou `7`, por exemplo. Atribuímos variáveis igualando a um valor: `x = 5`.

<br />

> Números Reais (*float*)

São todos os valores possíveis de serem representados por algarismos decimais. `5.0` ou `7.23`, por exemplo. Da mesma forma que os números `int`, podemos atribuir uma variável: `y = 3.14`.

<br />

> Números Complexos (*complex*)

Serve para representar números complexos, da forma `3+2j`, onde temos uma parte real e uma parte imaginária. Declaramos um número complexo utilizando o construtor `complex(Re, Im)`, tendo os argumentos `Re`(real) e `Im`(imaginário), ou uma string na forma `"3+5j"`. Exemplo: `a = complex("5+1j")`.

<br />

## Tipos de Lista

<br />

> Lista (*list*)

Listas são sequências mutáveis, utilizadas costumeiramente para armazenarmos itens homogêneos. Podemos declarar uma lista colocando seus itens entre colchetes: `listinha = [3, 5, 7, 11, 13]` ou pelo construtor `list()` colocando o valor da lista no interior dos parêntesis. Nossa `listinha` poderia ser declarada: `listinha = list((3, 5, 7, 11, 13))`.

<br />

> Tuplas (*tuples*)

São sequências imutáveis, normalmente utilizadas para armazenar dados heterogêneos, ou para armazenar sequências de dados homogêneos. Declaramos uma tupla colocando seus itens entre parêntesis: `vectorA = (a, b, c)` ou pelo construtor `tuple()`, da seguinte forma `vectorA = tuple('abc')`.

<br />

> Intervalo (*range*)

Representa uma sequência imutável de números. Utilizamos com frequência para percorrer um número determinado de vezes um laço `for`. Declaramos uma variável do tipo `range` através do construtor `range(início, fim, [salto -opcional])`. Vejamos os exemplos abaixo:

```
list(range(10)) # saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 5)) # saída: [1, 2, 3, 4]
list(range(0, 10, 3)) # saída: [0, 3, 6, 9]
```

<br />

## Tipo de Cadeia de Caracteres

<br />

> Strings (*str*)

São as cadeias de caracteres em texto. Declaramos uma variável deste tipo, colocando seu valor entre aspas: `nome = "Carlos"`. As aspas podem ser simples, duplas ou triplas.

<br />

## Tipos de Conjuntos

<br />

> Conjuntos (*set*)

É uma coleção de dados, mutável, sem repetições e não ordenada. Seus métodos implementam operações matemáticasentre conjuntos. É possível, por exemplo, verificar a igualdade entre conjuntos, diferença, interseção, entre outros.

Declaramos um conjunto igualando uma variável a uma coleção de itens entre chaves: `cariocas = {"Flamengo", "Botafogo", "Fluminense", "Vasco"}`. Alternativamente, podemos declarar pelo iniciador `set()`. Vejamos no exemplo:

```
cariocas = set(['Flamengo', 'Botafogo', 'Fluminense', 'Vasco'])
```

<br />

> Frozenset(*frozenset*)

São conjuntos que não podem ser modificados. São declarados através do construtor `frozenset()`:

```
cariocas = frozenset(['Flamengo', 'Botafogo', 'Fluminense', 'Vasco'])
```

<br />

## Tipos de Mapeamento

<br />

> Dicionários ou Objetos (*dict*)

São uma estrutura que funcionam da mesma forma que um objeto em JavaScript, pela associação de pares *chave-valor*.

Podemos declarar um `dict` utilizando pares chave-valor, entre chaves:

```
obj = { 'nome': 'João', 'role': 'filho' }
```

<br />

As chaves(`nome` e `role`) são informadas entre aspas para que o *runtime* do Python não interprete os nomes das chaves como variáveis e incorra em erro.

Podemos declarar através de uma sentença, por exemplo:

```
obj = { x: x ** 2 for x in range(1, 10, 3)}
# saída: {1: 1, 4: 16, 7: 49}
```

<br />

É possível também declarar utilizando o construtor `dict()`:

```
obj = dict([('x', 10), ('y', 20)])
```

<br />

## Tipos de Sequência Binária

<br />

> Bytes (*bytes*)
 
> ByteArray (*bytearray*)

> MemoryView (*memoryview*)