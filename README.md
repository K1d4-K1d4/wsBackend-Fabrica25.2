# wsBackend-Fabrica25.2
# Pokédex Project - Django

Este é um projeto desenvolvido como parte do Workshop de Backend da Fábrica de Software. A aplicação é uma Pokédex interativa construída com Django e Django REST Framework, permitindo que usuários criem contas, busquem Pokémons em uma API externa e montem suas próprias equipes.

## Tecnologias Utilizadas
* Python
* Django & Django REST Framework
* PostgreSQL
* Docker & Docker Compose
* HTML, CSS & JavaScript

## Funcionalidades
* Criação de contas de usuário (Treinadores).
* Sistema de Login e Logout baseado em sessões.
* Busca de Pokémons por nome ou ID na PokéAPI, com cadastro automático no banco de dados local.
* Montagem de uma equipe de até 6 Pokémons para cada treinador.
* Possibilidade de dar apelidos e remover Pokémons da equipe.
* Interface visual com templates Django.
* API REST para funcionalidades de registro.

## Como Rodar o Projeto com Docker

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/K1d4-K1d4/wsBackend-Fabrica25.2]
    cd pokemonProject
    ```

2.  **Configure a Senha:**
    * No arquivo `docker-compose.yml`, altere o valor de `POSTGRES_PASSWORD` e `DB_PASSWORD` para uma senha segura de sua escolha.

3.  **Construa e Inicie os Containers:**
    ```bash
    docker-compose up --build
    ```

4.  **Crie um Superusuário (Opcional, em outro terminal):**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5.  **Acesse a Aplicação:**
    * A interface web estará disponível em: `http://localhost:8000`
    * A API do DRF estará disponível em: `http://localhost:8000/api/`
    * O painel de administração estará em: `http://localhost:8000/admin/`