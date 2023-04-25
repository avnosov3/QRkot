# Cat Charity Fund

Благотворительный фонд поддержки котиков


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
git@github.com:avnosov3/QRkot_spreadsheets.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd QRkot_spreadsheets
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
5. Провести миграции
```
alembic upgrade head
```
6. Запустить проект
```
uvicorn app.main:app
```
## Автор
[Артём Носов](https://github.com/avnosov3)
