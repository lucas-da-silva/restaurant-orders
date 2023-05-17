<h1 align="center">Pedidos de restaurantes</h1>

## Sobre o projeto

Aplicação que gera cardápios a partir de arquivos `.csv`, que contém receitas e ingredientes.
Os cardápios podem ser gerados considerandos possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. E a cada pedido realizado, os ingredientes são consumidos.

Também é disponibilizada uma API para consulta dos cardápios e realização de pedidos.

## Tecnologias utilizadas

-   [Python](https://www.python.org/) - Linguagem de programação interpretada de alto nível.
-   [Pytest](https://docs.pytest.org/en/7.2.x/) - Framework de testes em Python.
-   [pandas](https://pandas.pydata.org/) - Biblioteca de software escrita para a linguagem de programação Python para manipulação e análise de dados.
-   [FastAPI](https://fastapi.tiangolo.com/) - Framework para construção de APIs com Python.

## Funcionalidades

-   Ler arquivos `.csv` de receitas e ingredientes.
-   Listar receitas com seus preços de venda e ingredientes.
-   Listar ingredientes com suas restrições.
-   Consumir ingredientes de uma receita.

## Instalação

```bash
# Clonar Projeto
$ git clone git@github.com:lucas-da-silva/restaurant-orders.git

# Entrar no diretório
$ cd restaurant-orders

# Criar ambiente virtual e ativá-lo
$ python3 -m venv .venv && source .venv/bin/activate

# Instalar dependências
$ python3 -m pip install -r dev-requirements.txt

# Subir a API
$ uvicorn app:app
# Acesse a rota /docs para ver a documentação gerada pelo FastAPI

# Executar testes
$ python3 -m pytest
```

## Estrutura do projeto

```
$PROJECT_ROOT
|   # Arquivos estáticos de receitas e ingredientes
├── data
|   # Arquivos Python da aplicação
├── src
|   |   # Classes de modelo para representação de dados
│   ├── models
|   |   # Classes de serviço para manipulação de dados
│   └── services
|   # Arquivos de testes
└── tests
    |   # Testes da classe Dish
    ├── dish
    |   # Testes da classe Ingredient
    └── ingredient
```

## Autor

-   [@lucas-da-silva](https://github.com/lucas-da-silva)
