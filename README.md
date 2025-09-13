# Pokédex Project - Django

Este é um projeto desenvolvido como parte do Workshop de Backend da Fábrica de Software. A aplicação é uma Pokédex interativa construída com Django, permitindo que usuários criem contas, busquem Pokémons em uma API externa e montem suas próprias equipes de até 6 pokémons.

## Tecnologias Utilizadas
* Python
* Django
* Django REST Framework (para o endpoint de registro)
* PostgreSQL (com Docker) ou SQLite (para setup manual)
* Docker & Docker Compose
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

Existem duas formas de rodar este projeto: a forma **Recomendada (com Docker)** e a forma **Manual**.

### Método 1: Com Docker (Recomendado)

Esta é a forma mais simples e rápida, pois o Docker configura todo o ambiente (Python, PostgreSQL, etc.) para você.

**Pré-requisitos:**
* [Git](https://git-scm.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/K1d4-K1d4/wsBackend-Fabrica25.2.git](https://github.com/K1d4-K1d4/wsBackend-Fabrica25.2.git)
    cd wsBackend-Fabrica25.2
    ```

2.  **Configure as Variáveis de Ambiente:**
    * Crie uma cópia do arquivo de exemplo `.env.example` e renomeie-a para `.env`.
    * Abra o arquivo `.env` e defina uma senha segura em `POSTGRES_PASSWORD`.

3.  **Construa e Inicie os Containers:**
    ```bash
    docker-compose up --build
    ```
    *Aguarde o processo ser finalizado. O terminal ficará mostrando os logs da aplicação.*

4.  **Crie um Superusuário (Opcional, em outro terminal):**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5.  **Acesse a Aplicação:**
    * **Interface Web:** `http://localhost:8000/`

---

### Método 2: Manualmente (Sem Docker)

Esta forma requer que você tenha o Python e (opcionalmente) o PostgreSQL instalados na sua máquina.

**Pré-requisitos:**
* [Git](https://git-scm.com/)
* [Python 3.12+](https://www.python.org/)
* (Opcional) [PostgreSQL](https://www.postgresql.org/download/)

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

4.  **Configure o Banco de Dados:**
    * **Opção A (Mais Simples - SQLite):** Se você não quer instalar o PostgreSQL, vá até o arquivo `pokemonProject/settings.py`, comente as configurações do `DATABASES` para PostgreSQL e descomente as do SQLite. Ficará assim:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```
    * **Opção B (Avançado - PostgreSQL):** Se você instalou o PostgreSQL na sua máquina, crie um banco de dados e um usuário para o projeto. Depois, crie um arquivo `.env` na raiz do projeto com suas credenciais:
        ```
        DB_NAME=seu_banco
        DB_USER=seu_usuario
        DB_PASSWORD=sua_senha
        DB_HOST=localhost
        DB_PORT=5432
        ```

5.  **Aplique as Migrações:**
    * Este comando criará o arquivo de banco de dados SQLite ou as tabelas no seu PostgreSQL.
    ```bash
    python manage.py migrate
    ```

6.  **Crie um Superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o Servidor:**
    ```bash
    python manage.py runserver
    ```

8.  **Acesse a Aplicação:**
    * **Interface Web:** `http://localhost:8000/`