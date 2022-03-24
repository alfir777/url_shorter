# URL shorter

Создание коротких ссылок с помощью Django и GraphQL

## Запуск
1. Клонировать репозиторий или форк
```
git clone https://github.com/alfir777/url_shorter.git
```
2. Выполнить копирование файла .env_template на .env и выставить свои параметры
```
cd jatu_ru/
cp .env_template .env
```
3. В Dockerfile заменить app на Вашего пользователя и его UID/GID
4. Создать acme.json для traefik и дать права
```
touch acme.json
chmod 600 acme.json
```
5. Развернуть контейнеры с помощью в docker-compose
```
docker-compose -f docker-compose.yml up -d
```
6. Выполнить миграции/сбор статики
```
 docker exec -it web python3 manage.py makemigrations
 docker exec -it web python3 manage.py migrate
 docker exec -it web python3 manage.py collectstatic
```
7. Создать суперпользователя
```
 docker exec -it web python3 manage.py createsuperuser
```
Возможны проблемы с правами на папки, созданными docker/django
- Изменить права доступа для директорий на 755 (drwxr-xr-x)
```
find /path/to/target/dir -type d -exec chmod 755 {} \;
```
- Изменить права доступа для файлов на 644 (-rw-r--r--)
```
find /path/to/target/dir -type f -exec chmod 644 {} \;
```
- Не всегда выполняются все миграции, принудительно:
```
 docker exec -it web python3 manage.py migrate --run-syncdb
```

## Запросы в GraphQL
#### Получить все записи
```GraphQL
query {
  urls {
    id
    fullUrl
    shortUrl
    clicks
    createdAt
  }
}
```

#### Фильтр записей со строкой "google"
```GraphQL
query {
  urls(url:"google") {
    id
    fullUrl
    shortUrl
    clicks
    createdAt
  }

```

#### Пагинация (получить первые 'first' URL-адресов, но пропустив 'skip' значении)
```GraphQL
query {
  urls(first: 15, skip: 3) {
    id
    fullUrl
    shortUrl
    clicks
    createdAt
  }
}
```

#### Создание записи
```
mutation {
  createUrl(fullUrl:"https://google.com") {
    url {
      id
      fullUrl
      shortUrl
      clicks
      createdAt
    }
  }
}
```