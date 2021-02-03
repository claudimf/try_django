# 'Try Django'

👋 Olá, Seja Bem-vindo(a) ao 'Try Django'.

# Como criar o projeto:

- 1° Criar arquivo Dockerfile com o seguinte conteúdo:
    ```sh
    FROM python:3
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    ADD requirements.txt /code/
    RUN pip install -r requirements.txt
    ADD . /code/
    ```
- 2° Criar o arquivo docker-compose.yml com o conteúdo abaixo:
    ```sh
    version: "3.3"
   
    services:
    db:
        image: postgres
        environment:
        - POSTGRES_DB=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
    web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
        - .:/code
        ports:
        - "8000:8000"
        depends_on:
        - db
    ```
- 3° Depois de criado os arquivos, construa sua aplicação com o Docker com o seguinte comando no terminal:
    ```sh
    sudo docker-compose run web django-admin.py startproject test .
    ```
- 4° Usando o Linux o projeto construido via Docker fica atrelado ao usuário raiz, para mudar o usuário execute o seguinte comando no terminal:
    ```sh
    sudo chown -R $USER:$USER .
    ```
- 5° Para conectar a database substitua o trecho "DATABASES = ..." do arquivo "test/settings.py" para:
    ```sh
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
    ```
- 6° Construa a aplicação:
    ```sh
    docker-compose build
    ```
- 7° Suba a aplicação:
    ```sh
    docker-compose up
    ```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm web bash
```

Para acessar a instância do banco de dados, execute:

```sh
docker exec-it [nome do db] bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

🚀 :clap: Para visualizar o sistema basta acessar no navegador no endereço: [localhost:8000](localhost:8000)

# Referências utilizadas

[1° Criar docker-compose para Django com banco Postgres](https://docs.docker.com/compose/django/#define-the-project-components/)  