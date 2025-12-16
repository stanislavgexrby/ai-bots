# Core

This directory contains the main AI bot logic, independent of the interaction interface.

## Structure

### agents/

Contains AI agent implementations - classes that encapsulate work with various AI APIs.

**Usage examples:**
- Class for working with OpenAI API
- Class for working with Anthropic Claude API
- Base agent class with common interface
- Agents with specialized behavior (RAG, functions, memory)

**File structure example:**
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

Contains request processing and response formatting logic.

**Usage examples:**
- Processing incoming messages
- Formatting responses
- Managing conversation context
- Processing system prompts
- Logic for special commands

**File structure example:**
```python
class MessageProcessor:
    def process_message(self, message: str, user_context: dict) -> dict:
        pass

    def format_response(self, ai_response: str) -> str:
        pass

    def update_context(self, user_id: str, message: str, response: str):
        pass
```

## Principles

1. **Interface independence** - code should not depend on where the request came from (Telegram, Web, CLI)
2. **Reusability** - classes and functions should be universal
3. **Modularity** - clear separation of responsibilities between agents and processors
