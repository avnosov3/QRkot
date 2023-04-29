# Cat Charity Fund

Благотворительный фонд поддержки котиков. Присутствует возможность формирования отчёта в гугл-таблице.


## Техно-стек
* python 3.7.9
* fastapi 0.78.0
* SQLAlchemy 1.4.36
* alembic 1.7.7
* pydantic 1.9.1
* aiogoogle 4.2.0
* uvicorn 0.17.6
* Google API 2.0


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
DATABASE_URL=sqlite+aiosqlite:///./charity_fund.db
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

email=<укажите потчу личного аккаунта Google>
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
