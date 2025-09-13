# Pokédex Project - Django

Este é um projeto desenvolvido como parte do Workshop de Backend da Fábrica de Software. A aplicação é uma Pokédex interativa construída com Django, permitindo que usuários criem contas, busquem Pokémons em uma API externa e montem suas próprias equipes de até 6 pokémons.

## Tecnologias Utilizadas
* Python
* Django
* Django REST Framework (para o endpoint de registro)
* HTML, CSS, JavaScript

## Funcionalidades
* Criação de contas de usuário (Treinadores) e login seguro com o sistema de autenticação do Django.
* Busca de Pokémons por nome ou ID na PokéAPI, com cadastro automático no banco de dados local.
* Montagem de uma equipe de até 6 Pokémons para cada treinador.
* Possibilidade de dar apelidos e remover Pokémons da equipe.
* Interface visual com templates Django.
* Opção para apagar a própria conta.

---

## Como Rodar o Projeto

**Pré-requisitos:**
* [Git](https://git-scm.com/)
* [Python 3.12+](https://www.python.org/)

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/K1d4-K1d4/wsBackend-Fabrica25.2.git](https://github.com/K1d4-K1d4/wsBackend-Fabrica25.2.git)
    cd wsBackend-Fabrica25.2
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    # Cria a venv
    python -m venv venv

    # Ativa a venv (Windows)
    .\venv\Scripts\activate

    # Ativa a venv (Linux/Mac)
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as Migrações:**
    * Este comando criará o arquivo de banco de dados SQLite ou as tabelas no seu PostgreSQL.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um Superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o Servidor:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse a Aplicação:**
    * **Interface Web:** `http://localhost:8000/`