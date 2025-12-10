# Database

Директория содержит код для работы с базами данных.

## Структура

### models/

Содержит модели данных для ORM (SQLAlchemy, Tortoise, MongoEngine и т.д.).

**Примеры моделей:**

**users.py** - модель пользователя:
```python
class User:
    - id
    - username
    - created_at
    - settings (JSON)
```

**messages.py** - модель сообщений:
```python
class Message:
    - id
    - user_id
    - content
    - role (user/assistant/system)
    - timestamp
    - conversation_id
```

**conversations.py** - модель беседы:
```python
class Conversation:
    - id
    - user_id
    - title
    - created_at
    - updated_at
    - metadata (JSON)
```

### migrations/

Содержит миграции схемы базы данных.

**Используемые инструменты:**
- Alembic (для SQLAlchemy)
- Django migrations
- Или кастомные скрипты миграций

## Подключения к БД

### PostgreSQL

Используется для:
- Хранение истории сообщений
- Пользовательские данные
- Метрики и аналитика

### MongoDB

Используется для:
- Документо-ориентированное хранение
- Гибкие схемы данных
- Большие объемы неструктурированных данных

### Redis

Используется для:
- Кэширование ответов
- Управление сессиями
- Rate limiting
- Временное хранение контекста

## Пример использования

```python
from database.models.users import User
from database.models.messages import Message

# Создание пользователя
user = User.create(username="john_doe")

# Сохранение сообщения
message = Message.create(
    user_id=user.id,
    content="Hello, AI!",
    role="user"
)

# Получение истории
history = Message.get_by_user(user.id, limit=10)
```

## Принципы

1. **Абстракция** - использование ORM для независимости от конкретной БД
2. **Миграции** - все изменения схемы через миграции
3. **Индексация** - правильные индексы для производительности
4. **Нормализация** - соблюдение принципов проектирования БД
