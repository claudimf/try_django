# Try Django

👋 Olá, Seja Bem-vindo(a) ao 'Try Django'.

# Projeto 'Try Django' do curso ['Python Django Web Framework - Full Course for Beginners'](https://www.youtube.com/watch?v=F5mRW0jo-U4):

## Sobre o curso:

O curso tem um guia básico que cobre as principais funcionalidades do Django Framework que você poderá acompanhar na lista abaixo chamada ['aulas do curso'](https://github.com/claudimf/try_django#aulas-do-curso), porém há alguns pontos de atenção:

1. Para facilitar o desenvolvimento utilizaremos Docker na aplicação e caso haja dúvida de como foi feito isso você pode acessar nas referências o link ['1° Criar projeto Django com banco Postgres'](https://github.com/claudimf/django-docker).

2. O banco padrão do Django até a versão corrente do curso é o Sqlite3, porém utilizo o Postgres nesse artigo. Arquivos alterados para essa configuração:
    * [settings](https://github.com/claudimf/try_django/blob/main/try_django/settings.py)
    * [docker-compose.yml](https://github.com/claudimf/try_django/blob/main/docker-compose.yml)

3. Para acesso ao banco com ferramentas como o [DBeaver](https://dbeaver.com/docs/wiki/Connect-to-Database/) os dados necessários a conexão você encontrará no [docker-compose.yml](https://github.com/claudimf/try_django/blob/main/docker-compose.yml) e a porta 5433 foi externalizada que são:
    * Host: localhost
    * Port: 5433
    * Database: postgres
    * User: postgres

4. No [docker-compose.yml](https://github.com/claudimf/try_django/blob/main/docker-compose.yml) o volume do banco foi externalizado para se preservar os dados imputados caso seja derrubado o container.

5. No [docker-compose.yml](https://github.com/claudimf/try_django/blob/main/docker-compose.yml) o volume da aplicação foi mapeado para que as alterações sejam identificadas no momento em que se subir o projeto.

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

### Criar migrações no seu banco de dados:

```sh
docker-compose exec web python manage.py makemigrations
```

### Aplicar migrações no seu banco de dados:

```sh
docker-compose exec web python manage.py migrate
```

### Criar um 'Super User' para acessso no [admin 'http://localhost:8000/admin'](http://localhost:8000/admin):

```sh
docker-compose exec web python manage.py createsuperuser
```

### Utilizar o ['shell_plus'](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) ao invés do shell:
1. no arquivo [settings.py](https://github.com/claudimf/try_django/blob/main/try_django/settings.py) adicione o app 'django_extensions' no dicionário 'INSTALLED_APPS'.
2. no arquivo [Dockerfile](https://github.com/claudimf/try_django/blob/main/Dockerfile) adicione a seguite linha:

    ```sh
    RUN pip install django-extensions
    ```
3. Reconstrua sua aplicação:
    ```sh
    docker-compose build
    ```
4. Para acessar o terminal interativo basta acessar o a bash do seu contâiner:
     ```sh
    docker-compose run --rm web bash
    ```
5. Por fim acessar o terminal com a opção '--print-sql' para imprimir as queries solicitadas pelo usuário:
     ```sh
    python manage.py shell_plus --print-sql
    ```

## Notas sobre as aulas:

- [(0:33:57​) 8 - Your First App Component](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2037s)
    * Criar um app chamado 'Products', para isso entre na bash via o seu terminal:
    ```sh
    docker-compose run --rm web bash
    ```
    * Depois crie o app:
    ```sh
    python manage.py startapp products
    ```
    * Criar no arquivo ['.products/models.py'](https://github.com/claudimf/try_django/blob/main/products/models.py) a classe Product e os atributos.
    ```sh
    class Product(models.Model):
        title = models.TextField()
        description = models.TextField()
        price = models.TextField()
        summary = models.TextField(default='isto é bacana!')
    ```

    * Gerar e aplicar as migrações no seu terminal.
    ```sh
    docker-compose exec web python manage.py makemigrations
    ```
    ```sh
    docker-compose exec web python manage.py migrate
    ```

    * Reiniciar a aplicação web:

    ```sh
    docker-compose down && docker-compose up web
    ```

    * Acessar no seu browser a rota [http://localhost:8000/admin/products/](http://localhost:8000/admin/products/)

- [(0:42:34​) 9 - Create Product Objects in the Python Shell](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2554s)
    * Utilizar o shell_plus(console interativo) para utilizar o ORM do Django.
    * Cadastrar produtos:
    ```sh
    Product.objects.create(title='Novo produto 2', description='outro', price='1234', summary='qualquer coisa')
    ```
- [(0:46:18​) 10 - New Model Fields](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2778s) 
    * Dropar seu banco, vá em seu terminal:
    ```sh
    docker-compose up -d db
    ```
    * liste o container do banco que estará de pé:
    ```sh
    docker ps
    ```
    * Entre no contâiner:
    ```sh
    docker exec -it [nome do db] bash
    ```
    * [dentro do container] - Entrar no banco e derrube o banco:
    ```sh
    drop database postgres;
    ```
    * [dentro do container] - Crie um novo banco:
    ```sh
    create database postgres;
    ```
    * Na model Product atualize o conteúdo para:
    ```sh
    class Product(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField(blank=True, null=True)
        price = models.DecimalField(max_digits=1000, decimal_places=2)
        summary = models.TextField()
    ```
    * Delete as migrações existentes e o pycache dos produtos e crie novamente as migrações e aplique.
    * Você poderá criar os produtos novamentes via terminal como no exemplo abaixo:
    ```sh
    Product.objects.create(title='Novo produto 2',  price=1.99, summary='qualquer coisa')
    ```
- [(0:59:27​) 12 - Default Homepage to Custom Homepage](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=3567s)
    * Criar um app chamado 'pages':
    ```sh
    python manage.py startapp pages
    ```
    * Crie a views no arquivo [pages/views.py](https://github.com/claudimf/try_django/blob/main/pages/views.py) com o seguinte conteúdo:
    ```sh
    from django.http import HttpResponse
    from django.shortcuts import render


    # Create your views here.
    def home_view(*args, **kwargs):
        return HttpResponse("<h1>Hello World<h1>")
    ```
    * Adiciona essa rota no arquivo [settings.py](https://github.com/claudimf/try_django/blob/main/try_django/settings.py)

- [(1:10:23​) 14 - Django Templates](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=4223s)
    * Criando os templates no diretório [templates](https://github.com/claudimf/try_django/tree/main/templates)
    * Configura o path dos templates no arquivo [settings.py](https://github.com/claudimf/try_django/blob/main/try_django/settings.py):
    ```sh
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, "templates")],
    ```
- [(1:16:50​) 15 - Django Templating Engine Basics](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=4610s)
    * Criar um template [base](https://github.com/claudimf/try_django/blob/main/templates/base.html) para ser compartilhado com os demais.

- [(1:24:00​) 16 - Include Template Tag](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=5040s)
    * Incluir uma [navba](https://github.com/claudimf/try_django/blob/main/templates/navbar.html)

- [(1:42:17​) 20 - Template Tags and Filters](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=6137s)
    * Criar [template que traz os detalhes do produto](https://github.com/claudimf/try_django/blob/main/templates/products/detail.html)

- [(2:06:50​) 23 - Django Model Forms](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=7610s)
    * Criar [um formulário para cadastrar produtos](https://github.com/claudimf/try_django/blob/main/products/forms.py)

- [(3:07:35​) 36 - Class Based Views - ListView](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=11255s)
    * Crie o app 'Blog':
    ```sh
    python manage.py startapp blog
    ```
    * Adicione o app no arquivo [settings.py](https://github.com/claudimf/try_django/blob/main/try_django/settings.py) e no arquivo [try_django/urls.py](https://github.com/claudimf/try_django/blob/main/try_django/urls.py).

## Aulas do curso:

- [(0:00:00​) 1 - Welcome ](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=0s)
- [(0:01:14​) 2 - Installing to Get Started](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=74s)
- [(0:05:02​) 3 - Setup your Virtual Environment for Django](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=302s)
- [(0:14:39​) 4 - Create a Blank Django Project](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=879s)
- [(0:18:54​) 5 - Setup Your Code Text Editor](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=1134s)
- [(0:22:27​) 6 - Settings](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=1347s)
- [(0:29:58​) 7 - Built-In Components](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=1798s)
- [(0:33:57​) 8 - Your First App Component](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2037s)
- [(0:42:34​) 9 - Create Product Objects in the Python Shell](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2554s)
- [(0:46:18​) 10 - New Model Fields](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=2778s)
- [(0:52:52​) 11 - Change a Model](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=3172s)
- [(0:59:27​) 12 - Default Homepage to Custom Homepage](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=3567s)
- [(1:04:48​) 13 - URL Routing and Requests](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=3888s)
- [(1:10:23​) 14 - Django Templates](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=4223s)
- [(1:16:50​) 15 - Django Templating Engine Basics](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=4610s)
- [(1:24:00​) 16 - Include Template Tag](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=5040s)
- [(1:26:49​) 17 - Rendering Context in a Template](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=5209s)
- [(1:33:21​) 18 - For Loop in a Template](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=5601s)
- [(1:37:01​) 19 - Using Conditions in a Template](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=5821s)
- [(1:42:17​) 20 - Template Tags and Filters](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=6137s)
- [(1:48:59​) 21 - Render Data from the Database with a Model](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=6539s)
- [(1:59:55​) 22 - How Django Templates Load with Apps](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=7195s)
- [(2:06:50​) 23 - Django Model Forms](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=7610s)
- [(2:14:16​) 24 - Raw HTML Form](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=8056s)
- [(2:25:33​) 25 - Pure Django Form](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=8733s)
- [(2:35:30​) 26 - Form Widgets](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=9330s)
- [(2:41:29​) 27 - Form Validation Methods](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=9689s)
- [(2:48:59​) 28 - Initial Values for Forms](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10139shttps://www.youtube.com/watch?v=F5mRW0jo-U4&t=10139s)
- [(2:51:42​) 29 - Dynamic URL Routing](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10302s)
- [(2:54:26​) 30 - Handle DoesNotExist](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10466s)
- [(2:56:24​) 31 - Delete and Confirm](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10584s)
- [(2:58:24​) 32 - View of a List of Database Objects](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10704s)
- [(3:00:00​) 33 - Dynamic Linking of URLs](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10800s)
- [(3:01:17​) 34 - Django URLs Reverse](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10877s)
- [(3:03:10​) 35 - In App URLs and Namespacing](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=10990s)
- [(3:07:35​) 36 - Class Based Views - ListView](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=11255s)
- [(3:10:45​) 37 - Class Based Views - DetailView](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=11445s)
- [(3:15:38​) 38 - Class Based Views - CreateView and UpdateView](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=11738s)
- [(3:21:23​) 39 - Class Based Views - DeleteView](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12083s)
- [(3:24:02​) 40 - Function Based View to Class Based View](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12242s)
- [(3:27:15​) 41 - Raw Detail Class Based View](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12435s)
- [(3:30:31​) 42 - Raw List Class Based View](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12631s)
- [(3:33:32​) 43 - Raw Create Class Based View](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12812s)
- [(3:26:03​) 44 - Form Validation on a Post Method](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12363s)
- [(3:37:58​) 45 - Raw Update Class Based View](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=13078s)
- [(3:41:13​) 46 - Raw Delete Class Based View](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=13273s)
- [(3:42:17​) 47 - Custom Mixin for Class Based Views](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=13337s)

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

[1° Criar projeto Django com banco Postgres](https://github.com/claudimf/django-docker)

[2° 'Try Django' do curso 'Python Django Web Framework - Full Course for Beginners'](https://www.youtube.com/watch?v=F5mRW0jo-U4)

[3° 'Try Django' project sample - Full Course for Beginners'](https://github.com/codingforentrepreneurs/Try-Django)

[4° Django Models Fields types](https://docs.djangoproject.com/en/3.1/ref/models/fields/)

[5° Built-in template tags and filters](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)

[6° Form fields tyoe in Django](https://docs.djangoproject.com/en/3.1/ref/forms/fields/)

[7º 10 reasons to try django for client projects](https://www.freecodecamp.org/news/10-reasons-to-try-django-for-client-projects/)