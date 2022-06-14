# warpoint
1. Собрать образы

```docker-compose -f ./docker-compose.yaml up --build```

2. Использовать сервис

```http://0.0.0.0:8000/docs```

3. Обратиться к URL для получения статических данных (лимит обращений < 60 или вернет код 429)

```curl -X 'GET' 'http://0.0.0.0:8000/' -H 'accept: text/html'```
  
5. Создать пользователя

```curl -X 'POST' 'http://0.0.0.0:8000/user/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email": "user@example.com","password": "password123","password2": "password123"}'```

6. Авторизироваться чтобы получить токен (извлечь токен из response)

```curl -X 'POST' 'http://0.0.0.0:8000/auth/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email": "user@example.com","password": "password123"}'```

7. Продолжить запрос к http://0.0.0.0:8000/ без ограничений

```curl -X 'GET' 'http://0.0.0.0:8000/' -H 'accept: text/html' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIiwiZXhwIjoxNjU1MjM3MDI1fQ.W5ARON4Bo8QeTU1xKmdBZZ3hLGyFHlgpmIzXkEIJ_J0'```

В качестве хранилища используется Redis. Время жизни токена по умолчанию 2 минуты, чтобы изменить это обратитесь к `ACCESS_TOKEN_EXPIRE_MINUTES`
