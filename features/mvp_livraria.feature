# language: pt

Funcionalidade: MVP do aplicativo da livraria
  Como cliente da livraria
  Quero pesquisar e comprar livros pelo aplicativo
  Para retirar minha compra na loja

  Cenário: Cadastrar um novo cliente
    Dado que o cliente ainda não possui cadastro
    Quando o cliente informar o nome "Ana" e o e-mail "ana@email.com"
    Então o cadastro deve ser realizado com sucesso

  Cenário: Pesquisar um livro pelo título
    Dado que existem livros cadastrados no catálogo
    Quando o cliente pesquisar pelo título "O Hobbit"
    Então o sistema deve retornar o livro "O Hobbit"
    E deve apresentar o preço, a edição e o estoque

  Cenário: Comprar um livro disponível para retirada
    Dado que o cliente de e-mail "ana@email.com" está cadastrado
    E que o livro "O Hobbit" possui estoque disponível
    Quando o cliente comprar o livro "O Hobbit" via Pix para retirar na loja "Centro"
    Então o pedido deve ser confirmado
    E o pagamento deve estar aprovado
    E a loja de retirada deve ser "Centro"

  Cenário: Tentar comprar um livro indisponível
    Dado que o cliente de e-mail "ana@email.com" está cadastrado
    E que o livro "Clean Code" está sem estoque
    Quando o cliente tentar comprar o livro "Clean Code" via Pix
    Então o sistema deve informar que o livro está indisponível