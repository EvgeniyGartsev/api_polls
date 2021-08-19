# api_polls
## Описание

Проект **Polls** позволяет проводить опросы пользователей.
### Функционал для администратора системы:

- авторизация в системе
- добавление/изменение/удаление опросов.
- добавление/изменение/удаление вопросов в опросе.

### Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя
Для получения списка ответов для анонимного пользователя необходимо в HEADERS запроса указань id. Для получения id необходимо отправить GET запрос на эндпоинт api/v1/auth/get_id/.
Подробная документация доступна по адресу http://127.0.0.1:8000/redoc/ после запуска проекта. Процедура запуска проекта представлена ниже.

## Использованные технологии
- Django 2.2.10
- Django REST framework.

## Процедура запуска проекта

1. Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/EvgeniyGartsev/api_yamdb
cd api_yamdb

2. Cоздать и активировать виртуальное окружение:

python3 -m venv venv
source venv/Scripts/activate

3. Обновить pip и установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Выполнить миграции

python manage.py migrate

5. Запустить проект

python3 manage.py runserver
