### Описание проекта:

Благотворительный фонд поддержки котиков

### Автор: [Артём Носов](https://github.com/avnosov3)

### Техно-стек:
* python 3.7.9
* fastapi 0.78.0
* SQLAlchemy 1.4.36

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:avnosov3/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Провести миграции

```
alembic upgrade head
```

Запустить проект

```
uvicorn app.main:app
```
