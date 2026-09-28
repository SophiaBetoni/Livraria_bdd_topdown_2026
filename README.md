# Livraria BDD e Top-Down 2026

MVP de um aplicativo de livraria desenvolvido com BDD e desenvolvimento
Top-Down.

## Objetivo

Permitir que o cliente se cadastre, pesquise livros, consulte informações
e compre um livro via Pix para retirada na loja.

## Funcionalidades do MVP

- Cadastro de clientes;
- Pesquisa de livros pelo título;
- Visualização de preço, edição e estoque;
- Pagamento via Pix;
- Compra para retirada na loja;
- Confirmação do pedido;
- Impedimento da compra de livros sem estoque.

## BDD

Os comportamentos do sistema foram definidos antes da implementação por
meio de cenários escritos no formato:

- Dado;
- Quando;
- Então.

Os cenários estão no arquivo:

```text
features/mvp_livraria.feature
```

Os passos Python correspondentes estão em:

```text
features/steps/mvp_steps.py
```

## Desenvolvimento Top-Down

O desenvolvimento começou pelo fluxo principal representado pela classe
`LivrariaApp`.

A classe principal delega responsabilidades para componentes menores:

- `LivrariaApp`: coordena o fluxo da aplicação;
- `Catalogo`: pesquisa livros e controla o estoque;
- `PagamentoPix`: processa o pagamento.

Assim, o sistema foi construído do comportamento mais geral para os
componentes internos.

## Estrutura

```text
Livraria_bdd_topdown_2026/
├── features/
│   ├── steps/
│   │   └── mvp_steps.py
│   ├── environment.py
│   └── mvp_livraria.feature
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── catalogo.py
│   └── pagamento.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalação

Crie e ative um ambiente virtual:

```bash
py -m venv .venv
```

No Windows:

```bash
.\.venv\Scripts\activate
```

Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

## Executar os testes BDD

```bash
behave
```

Resultado esperado:

```text
1 feature passed
4 scenarios passed
17 steps passed
```

## Tecnologias

- Python;
- Behave;
- Gherkin;
- Git;
- GitHub;
- Visual Studio Code.