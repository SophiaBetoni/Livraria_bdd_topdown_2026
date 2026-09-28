from src.app import LivrariaApp


def before_scenario(context, scenario):
    livros = [
        {
            "titulo": "O Hobbit",
            "autor": "J. R. R. Tolkien",
            "preco": 59.90,
            "edicao": "Capa dura",
            "estoque": 3,
        },
        {
            "titulo": "Clean Code",
            "autor": "Robert Martin",
            "preco": 120.00,
            "edicao": "2ª edição",
            "estoque": 0,
        },
    ]

    context.app = LivrariaApp(livros)