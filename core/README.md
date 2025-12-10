# Core

Директория содержит основную логику работы AI-ботов, независимую от интерфейса взаимодействия.

## Структура

### agents/

Содержит реализации AI агентов - классов, которые инкапсулируют работу с различными AI API.

**Примеры использования:**
- Класс для работы с OpenAI API
- Класс для работы с Anthropic Claude API
- Базовый класс агента с общим интерфейсом
- Агенты со специализированным поведением (RAG, функции, memory)

**Пример структуры файла:**
```python
class BaseAgent:
    def __init__(self, api_key: str, model: str):
        pass

    def generate_response(self, prompt: str, context: dict = None) -> str:
        pass

    def stream_response(self, prompt: str, context: dict = None):
        pass
```

### processors/

Содержит логику обработки запросов и формирования ответов.

**Примеры использования:**
- Обработка входящих сообщений
- Форматирование ответов
- Управление контекстом беседы
- Обработка системных промптов
- Логика для специальных команд

**Пример структуры файла:**
```python
class MessageProcessor:
    def process_message(self, message: str, user_context: dict) -> dict:
        pass

    def format_response(self, ai_response: str) -> str:
        pass

    def update_context(self, user_id: str, message: str, response: str):
        pass
```

## Принципы

1. **Независимость от интерфейса** - код не должен зависеть от того, откуда пришел запрос (Telegram, Web, CLI)
2. **Переиспользуемость** - классы и функции должны быть универсальными
3. **Модульность** - четкое разделение ответственности между агентами и процессорами
