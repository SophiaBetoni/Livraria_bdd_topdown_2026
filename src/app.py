from src.catalogo import Catalogo
from src.pagamento import PagamentoPix


class LivrariaApp:

    def __init__(self, livros):
        self.catalogo = Catalogo(livros)
        self.pagamento = PagamentoPix()
        self.clientes = {}
        self.pedidos = []

    def cadastrar_cliente(self, nome, email):
        email_normalizado = email.casefold()

        if email_normalizado in self.clientes:
            raise ValueError("Cliente já cadastrado.")

        cliente = {
            "nome": nome,
            "email": email,
        }

        self.clientes[email_normalizado] = cliente
        return cliente

    def cliente_existe(self, email):
        return email.casefold() in self.clientes

    def pesquisar_livros(self, titulo):
        return self.catalogo.pesquisar_por_titulo(titulo)

    def comprar_para_retirada(self, email, titulo, loja):
        if not self.cliente_existe(email):
            raise ValueError("Cliente não cadastrado.")

        livro = self.catalogo.encontrar_por_titulo(titulo)

        if livro is None:
            raise ValueError("Livro não encontrado.")

        if livro["estoque"] <= 0:
            raise ValueError("Livro indisponível.")

        pagamento = self.pagamento.processar(livro["preco"])
        self.catalogo.reduzir_estoque(titulo)

        pedido = {
            "id": len(self.pedidos) + 1,
            "cliente": email,
            "livro": livro["titulo"],
            "loja_retirada": loja,
            "status": "confirmado",
            "pagamento": pagamento,
        }

        self.pedidos.append(pedido)
        return pedido