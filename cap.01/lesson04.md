# Os Comandos Help e Type

Esses comandos são duas importantes ferramentas, simples e elegantes, que podem ajudar na compreensão dos mais diversos códigos.

O comando `help()` serve para trazer informações acerca de um determinado comando passado por parâmetro. Entre as informações estão os métodos inerentes ao comando-parâmetro, bem como uma descrição básica do papel que ele exerce. Por exemplo:

```
$ help("def")
```

O comando acima irá trazer todas as informações sobre o comando `def`, como seu caráter definidor de funções, seus usos principais, os parâmetros aceitos e referências de documentos que possam trazer informações além do `help`.

O comando `type()`, por sua vez, identifica a que tipo pertence um objeto, variável, ou função. Sua sintaxe é simpeles: passamos como parâmetro o nome do objeto testado.

Por exemplo, imaginemos a variável `nomes`, que é uma lista de nomes próprios e foi definida por:

```
$ nomes = list(('Regina', 'Alberto', 'Renato'))
```

Podemos verificar o tipo dessa variável da seguinte forma:

```
$ type(nomes)

# teremos a saída: <class 'list'>
```