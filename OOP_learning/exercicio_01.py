# Como lição de casa, tente criar uma classe
# com base em um livro que você leria.
# Pense em como você escreveria a classe
# e quais propriedades ela deveria ter.


class Book:
    def __init__(self, title, author, editor, year, gender, isbn):
        self.title = title
        self.author = author
        self.editor = editor
        self.year = year
        self.gender = gender
        self.isbn = isbn


book = Book(
    "Verão da Corrupção",
    "King, Stephen",
    "Francisco Alves",
    1988,
    "Contos estadunidenses",
    8526501496,
)

print(book.isbn)
