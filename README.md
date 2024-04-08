# Hi ProninTeam
# Проект "group_fees"

Этот проект - это [Django](https://www.djangoproject.com/) приложение для управления групповыми расходами.<br/>
## Использованные пакеты

Для разработки этого проекта мы использовали следующие пакеты:

- [Django](https://www.djangoproject.com/): Фреймворк для веб-разработки на языке Python.
- [Django REST framework](https://www.django-rest-framework.org/): Мощный и гибкий инструмент для создания API на базе Django.
- [django-redis](https://django-redis.readthedocs.io/): Пакет для интеграции Redis с Django.
- [Pillow](https://python-pillow.org/): Библиотека для работы с изображениями в Python.
- [sqlparse](https://pypi.org/project/sqlparse/): Парсер SQL-запросов для Python.
- [typing-extensions](https://pypi.org/project/typing-extensions/): Поддержка типов для Python 3.7 и выше.
- [tzdata](https://pypi.org/project/tzdata/): Данные о временных зонах для Python.

## Запуск проекта через Docker
1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Склонируйте репозиторий:

    ```bash
    git clone <URL репозитория>
    ```

3. Перейдите в каталог проекта:

    ```bash
    cd group_fees
    ```
4. Запустите проект с помощью Docker Compose:

    ```bash
    docker-compose up
    ```

5. Ваше приложение будет доступно по адресу http://127.0.0.1:8000/.

***
Для создания моковых значений 
 - python manage.py populate_db
***
