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

### Gerando os dados

#### 1.1 No seu terminal, rode o ambiente shell do Python
```bash
./manage.py shell
```
#### 1.2 Importe o arquivo onde está a função que cria os objetos de acordo com a API
```bash
from core.views import baixar_dados_api
```
```bash
baixar_dados_api()
```

***
# 2 - Liks

Aplicação no Heroku: http://searchsystem.herokuapp.com

API: http://uinames.com/api/?amount=25
