# Back-Monitoring-Test

API to generate an chart based on transactions given by the user, and alerting if something is not normal

# Install

you have to install it on an virtual ambient, so firts create an venv with:

```shell
python -m venv venv
```

then, access it with:

```shell
Powershell:
.\venv\Scripts\activate
```

```bash
GitBash:
source venv/Scripts/activate
```

After all that, just install the requirements with:

```shell
pip install -r requirements.txt
```

# Enviroment Variables

To proceed with the project, you will need to fill the Enviroment Variables on an .env arquive. So create an .env with this variables

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

Now all that is left is to run the migrations on your database, an then initiate the server

To run the migrations:

```shel
python manage.py migrate
```

And finally, to start the server:

```shel
python manage.py runserver
```
