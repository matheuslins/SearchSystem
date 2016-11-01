# SearchSystem

<p>
**Linguagem Utilizada no Projeto:</b> Python 3.4. e Django 1.10.**
</p>

**Antes de começar o projeto instale:**
* Python 3.4
* Pip
* Virtualenv
* Redis
* Celery

***

# 1 - COMEÇANDO O PROJETO

## Clone o projeto

**SSH

```bash
git@github.com:matheuslins/SearchSystem.git
```
OU

**HTTPS

```bash
https://github.com/matheuslins/SearchSystem.git
```

## Instalando as dependencias

Em seguida, vá para a pasta clonada do projeto e o comando:
```bash
pip install -r requirements.txt
```

### Gere as Tabelas
no terminal (na raiz do projeto), rode o comando:
```bash
./manage.py migrate
```
rode o projeto na porta 7000

 ```bash
 ./manage.py runserver 7000
 ``` 

# 2 -  GERANDO OS DADOS

** Sincronamente...

#### 1.1 No seu terminal, rode o ambiente shell do Python
```bash
./manage.py shell
```
#### 1.2 Importe o arquivo onde está a função que cria os objetos de acordo com a API
```bash
from core.tasks import baixar_dados_api
```
Em seguida:
```bash
baixar_dados_api()
```
** Assincrônamente...

#### 1.1 Rode o Celery

```bash
celery -A searchsystem worker -l info
```
Em seguida:
```bash
baixar_dados_api.delay()
```

#### 1.2 Rode o Redis

```bash
redis-server
```
***
# 2 - Links

Aplicação no Heroku:

Instalando o Redis: http://redis.io/topics/quickstart

API: http://uinames.com/api/?amount=25
