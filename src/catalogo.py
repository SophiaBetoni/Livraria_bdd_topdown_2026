class Catalogo:

    def __init__(self, livros):
        self.livros = [livro.copy() for livro in livros]

    def pesquisar_por_titulo(self, titulo):
        termo = titulo.casefold()

        return [
            livro.copy()
            for livro in self.livros
            if termo in livro["titulo"].casefold()
        ]

    def encontrar_por_titulo(self, titulo):
        for livro in self.livros:
            if livro["titulo"].casefold() == titulo.casefold():
                return livro

        return None

    def definir_estoque(self, titulo, quantidade):
        livro = self.encontrar_por_titulo(titulo)

        if livro is None:
            raise ValueError("Livro não encontrado.")

        livro["estoque"] = quantidade

    def reduzir_estoque(self, titulo):
        livro = self.encontrar_por_titulo(titulo)

        if livro is None:
            raise ValueError("Livro não encontrado.")

        if livro["estoque"] <= 0:
            raise ValueError("Livro indisponível.")

        livro["estoque"] -= 1