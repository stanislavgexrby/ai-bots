# Utils

Директория содержит вспомогательные функции и утилиты, используемые во всем проекте.

## Примеры утилит

### logging.py
Настройка логирования для проекта.

```python
def setup_logger(name: str, log_file: str, level: str):
    """Настройка логгера с ротацией файлов"""
    pass

def log_api_call(provider: str, tokens: int, cost: float):
    """Логирование вызовов AI API"""
    pass
```

### validators.py
Валидация входных данных.

```python
def validate_api_key(key: str) -> bool:
    """Проверка формата API ключа"""
    pass

def sanitize_user_input(text: str) -> str:
    """Очистка пользовательского ввода"""
    pass
```

### formatters.py
Форматирование текста и данных.

```python
def format_code_block(code: str, language: str) -> str:
    """Форматирование блока кода для отображения"""
    pass

def truncate_text(text: str, max_length: int) -> str:
    """Обрезка текста с сохранением смысла"""
    pass
```

### rate_limiter.py
Управление частотой запросов.

```python
class RateLimiter:
    def check_rate_limit(self, user_id: str) -> bool:
        """Проверка лимита запросов"""
        pass

    def increment_usage(self, user_id: str):
        """Увеличение счетчика использования"""
        pass
```

### context_manager.py
Управление контекстом беседы.

```python
def build_context(messages: list, max_tokens: int) -> str:
    """Формирование контекста из истории сообщений"""
    pass

def summarize_context(messages: list) -> str:
    """Суммаризация длинного контекста"""
    pass
```

### crypto.py
Криптографические функции.

```python
def hash_password(password: str) -> str:
    """Хеширование пароля"""
    pass

def encrypt_sensitive_data(data: str) -> str:
    """Шифрование чувствительных данных"""
    pass
```

## Принципы

1. **DRY** - избегайте дублирования кода
2. **Простота** - функции должны делать одно дело хорошо
3. **Переиспользуемость** - утилиты должны быть универсальными
4. **Документация** - каждая функция должна иметь docstring
