from behave import given, when, then


@given("que o cliente ainda não possui cadastro")
def step_cliente_sem_cadastro(context):
    assert not context.app.cliente_existe("ana@email.com")


@when('o cliente informar o nome "{nome}" e o e-mail "{email}"')
def step_cadastrar_cliente(context, nome, email):
    context.cliente = context.app.cadastrar_cliente(nome, email)


@then("o cadastro deve ser realizado com sucesso")
def step_verificar_cadastro(context):
    assert context.app.cliente_existe(context.cliente["email"])


@given("que existem livros cadastrados no catálogo")
def step_catalogo_com_livros(context):
    assert len(context.app.catalogo.livros) > 0


@when('o cliente pesquisar pelo título "{titulo}"')
def step_pesquisar_livro(context, titulo):
    context.resultado = context.app.pesquisar_livros(titulo)


@then('o sistema deve retornar o livro "{titulo}"')
def step_verificar_livro_encontrado(context, titulo):
    titulos = [livro["titulo"] for livro in context.resultado]

    assert titulo in titulos


@then("deve apresentar o preço, a edição e o estoque")
def step_verificar_detalhes(context):
    assert context.resultado

    livro = context.resultado[0]

    assert "preco" in livro
    assert "edicao" in livro
    assert "estoque" in livro


@given('que o cliente de e-mail "{email}" está cadastrado')
def step_cliente_cadastrado(context, email):
    if not context.app.cliente_existe(email):
        context.app.cadastrar_cliente("Ana", email)

    context.email_cliente = email


@given('que o livro "{titulo}" possui estoque disponível')
def step_livro_disponivel(context, titulo):
    livro = context.app.catalogo.encontrar_por_titulo(titulo)

    assert livro is not None
    assert livro["estoque"] > 0


@when(
    'o cliente comprar o livro "{titulo}" via Pix '
    'para retirar na loja "{loja}"'
)
def step_comprar_livro(context, titulo, loja):
    context.pedido = context.app.comprar_para_retirada(
        context.email_cliente,
        titulo,
        loja,
    )


@then("o pedido deve ser confirmado")
def step_verificar_pedido(context):
    assert context.pedido["status"] == "confirmado"


@then("o pagamento deve estar aprovado")
def step_verificar_pagamento(context):
    assert context.pedido["pagamento"]["status"] == "aprovado"
    assert context.pedido["pagamento"]["forma"] == "Pix"


@then('a loja de retirada deve ser "{loja}"')
def step_verificar_loja(context, loja):
    assert context.pedido["loja_retirada"] == loja


@given('que o livro "{titulo}" está sem estoque')
def step_livro_sem_estoque(context, titulo):
    context.app.catalogo.definir_estoque(titulo, 0)


@when('o cliente tentar comprar o livro "{titulo}" via Pix')
def step_tentar_comprar(context, titulo):
    try:
        context.app.comprar_para_retirada(
            context.email_cliente,
            titulo,
            "Centro",
        )
        context.erro = None
    except ValueError as erro:
        context.erro = str(erro)


@then("o sistema deve informar que o livro está indisponível")
def step_verificar_indisponibilidade(context):
    assert context.erro == "Livro indisponível."