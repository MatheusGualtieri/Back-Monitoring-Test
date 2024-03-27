# Back-Monitoring-Test

API para gerar gráficos baseados em dados(neste caso, transações) fornecidas pelo usuário, e alertando se algo estiver fora do normal

# Instalação

Deve-se instala-lo em um ambiente virtual, então primeiramente, crie um venv com:

```shell
python -m venv venv
```

Depois, acesse com:

```shell
Powershell:
.\venv\Scripts\activate
```

```bash
GitBash:
source venv/Scripts/activate
```

Emfim, instale as depenências com:

```shell
pip install -r requirements.txt
```

# Variáveis de ambiente

Para prosseguir com o projeto, você precisará preencher as Variáveis ​​de Ambiente em um arquivo .env. Então crie um .env com essas variáveis

```env
SECRET_KEY = yourSecretKey
POSTGRES_DB = yourDB
POSTGRES_USER = yourPSQLUser
POSTGRES_PASSWORD =yourPSQLPassword
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=yourMail
EMAIL_HOST_PASSWORD=pass
```

# Migrations

Agora só falta executar as migrações no seu banco de dados e então iniciar o servidor

Para rodar as migrações:

```shel
python manage.py migrate
```

Finalmente, para iniciar o servidor:

```shel
python manage.py runserver
```
