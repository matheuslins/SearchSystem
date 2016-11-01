# SearchSystem

<p>
**Linguagem Utilizada no Projeto:</b> Python 3.4. e Django 1.10.**
</p>

**Antes de começar o projeto instale:**
* Python 3.4
* Pip
* Virtualenv

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
pronto, agora é só usar o ```./manage.py runserver``` para rodar o projeto.

# 2 -  GERANDO OS DADOS

** No Terminal...

#### 1.1 No seu terminal, rode o ambiente shell do Python
```bash
./manage.py shell
```
#### 1.2 Importe o arquivo onde está a função que cria os objetos de acordo com a API
```bash
from core.tasks import baixar_dados_api
```
```bash
baixar_dados_api()
```
** Por uma tarefa assincrôna

#### 1.1 Rode o Celery

```bash
celery -A searchsystem worker -l info
```

#### 1.2 Rode o Redis

```bash
redis-server
```
***
# 2 - Links

Aplicação no Heroku:

API: http://uinames.com/api/?amount=25
