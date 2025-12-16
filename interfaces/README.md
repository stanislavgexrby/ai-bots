# Interfaces

This directory contains different interaction interfaces for the AI bot.

## Structure

### telegram/

Telegram bot implementation.

**Contains:**
- Command and message handlers
- Inline keyboards and callback handlers
- Webhook or polling logic
- Telegram-specific formatting (Markdown, HTML)

**Main components:**
- `bot.py` - main bot initialization file
- `handlers.py` - message and command handlers
- `keyboards.py` - keyboards and menus
- `middleware.py` - middleware handlers

### web/

Web interface for AI bot (REST API, WebSocket, web application).

**Contains:**
- REST API endpoints
- WebSocket connections for real-time communication
- Static files (if frontend exists)
- Middleware for authentication and authorization

**Main components:**
- `app.py` - main web application (FastAPI/Flask/Django)
- `routes.py` - route definitions
- `websocket.py` - WebSocket handlers
- `static/` - static files
- `templates/` - HTML templates

### cli/

Command-line interface for AI interaction.

**Contains:**
- Terminal command handlers
- REPL interface
- Console output formatting
- Command-line argument processing

**Main components:**
- `cli.py` - main CLI interface
- `commands.py` - command handlers
- `formatter.py` - output formatting

## Principles

1. **Thin layer** - interfaces should be as thin as possible, all logic stays in core/
2. **Specificity** - platform-specific code (Telegram API, FastAPI, etc.) is isolated here
3. **Unified contract** - all interfaces should use the same way of interacting with core/

## Interaction with core

All interfaces should use classes from `core/` for logic processing:

```python
from core.agents import OpenAIAgent
from core.processors import MessageProcessor

agent = OpenAIAgent(api_key="...")
processor = MessageProcessor(agent)

# In the interface handler
response = processor.process_message(user_message, user_context)
```
