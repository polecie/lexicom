[Текст задания](https://github.com/polecie/lexicom/blob/main/src/task.md)

Суть: Разработать рестфул сервис + написать запросы к таблицам

## Настройка окружения
Создайте файл .env в папке .docker по образцу .env.example

## Запуск
_Для задания 1_

Склонируйте репозиторий и в папке с проектом выполните команду `docker-compose -f .docker/docker-compose.yaml up -d --build`, после этого проект доступен на http://0.0.0.0:8080

_Для задания 2_

После того как контейнеры поднимутся в папке с проектом выполните команду `docker compose -f .docker/docker-compose.yaml exec -it postgres psql -U (POSTGRES_USER из .env) -d (POSTGRES_DB из .env) -f /dumps/db.out`

[Запросы для задания 2 находятся тут](https://github.com/polecie/lexicom/blob/main/src/sql)
