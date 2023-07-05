# Cat Charity Fund
<details><summary>Russian language</summary>  
    
Благотворительный фонд поддержки котиков. Присутствует возможность формирования отчёта в гугл-таблице.
[Документация](https://127.0.0.1:8000/docs) доступна после запуска проекта

## Техно-стек
* python 3.7.9
* fastapi 0.78.0
* SQLAlchemy 1.4.36
* alembic 1.7.7
* pydantic 1.9.1
* aiogoogle 4.2.0
* uvicorn 0.17.6
* Google API 2.0

## Запуск проекта
1. Клонировать репозиторий
```
git clone git@github.com:avnosov3/QRkot.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd QRkot
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Активировать виртуальное окружение
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Установить зависимости из файла requirements.txt:
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Создать файл и заполнить файл .env
```
DATABASE_URL=sqlite+aiosqlite:///./<указать название БД>.db
SECRET=<указать секретное значение>
FIRST_SUPERUSER_EMAIL = <указать логин супер пользователя>
FIRST_SUPERUSER_PASSWORD = <указать пароль супер пользователя>

type=<указать данные из сервисного аккаунта Google Cloud>
project_id=<указать данные из сервисного аккаунта Google Cloud>
private_key_id=<указать данные из сервисного аккаунта Google Cloud>
private_key<указать данные из сервисного аккаунта Google Cloud>
client_email=<указать данные из сервисного аккаунта Google Cloud>
client_id=<указать данные из сервисного аккаунта Google Cloud>
auth_uri=<указать данные из сервисного аккаунта Google Cloud>
token_uri=<указать данные из сервисного аккаунта Google Cloud>
auth_provider_x509_cert_url=<указать данные из сервисного аккаунта Google Cloud>
client_x509_cert_url=<указать данные из сервисного аккаунта Google Cloud>

email=<указать потчу личного аккаунта Google>
```
6. Провести миграции
```
alembic upgrade head
```
7. Запустить проект
```
uvicorn app.main:app
```

## Автор
[Артём Носов](https://github.com/avnosov3)
</details>
<details><summary>English language</summary>  
  
Charitable foundation for the support of cats. There is the possibility of generating a report in a Google spreadsheet.
[Documentation](https://127.0.0.1:8000/docs) available after project launch

## Stack
* python 3.7.9
* fastapi 0.78.0
* SQLAlchemy 1.4.36
* alembic 1.7.7
* pydantic 1.9.1
* aiogoogle 4.2.0
* uvicorn 0.17.6
* Google API 2.0

## Launch of the project

1. Clone repository
```
git clone git@github.com:avnosov3/QRkot.git
```
2. Go to the project folder and create a virtual environment
```
cd QRkot
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Activate a virtual environment
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Install dependencies from requirements.txt
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Create a file and fill the .env file
```
DATABASE_URL=sqlite+aiosqlite:///./<specify the name of the database>.db
SECRET=<specify secret value>
FIRST_SUPERUSER_EMAIL = <specify super user login>
FIRST_SUPERUSER_PASSWORD = <specify super user password>

type=<specify data from the Google Cloud service account>
project_id=<specify data from the Google Cloud service account>
private_key_id=<specify data from the Google Cloud service account>
private_key<specify data from the Google Cloud service account>
client_email=<specify data from the Google Cloud service account>
client_id=<specify data from the Google Cloud service account>
auth_uri=<specify data from the Google Cloud service account>
token_uri=<specify data from the Google Cloud service account>
auth_provider_x509_cert_url=<specify data from the Google Cloud service account>
client_x509_cert_url=<specify data from the Google Cloud service account>

email=<specify the email of a personal Google account>
```
6. Conduct migrations
```
alembic upgrade head
```
7. Start project
```
uvicorn app.main:app
```

## Author
[Artem Nosov](https://github.com/avnosov3)

</details>
