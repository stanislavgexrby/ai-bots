# AI Bots Framework

Universal framework for developing AI bots with modular architecture.

## Current Bot: Telegram Bot with Deepseek API

Simple Telegram bot that uses Deepseek API for generating responses. Maintains conversation context for each user.

**Features:**
- Conversation context management
- Basic commands (/start, /help, /clear)
- Docker deployment ready

## Architecture

### Structure
```
core/
├── agents/
│   └── deepseek_agent.py       - Deepseek API client
└── processors/
    └── message_processor.py    - Context management

interfaces/
└── telegram/
    └── bot.py                  - Telegram bot handlers

main.py                         - Entry point
```

### Components
- **DeepseekAgent** - API client for Deepseek
- **MessageProcessor** - Context management
- **TelegramBot** - Telegram interface handlers

## Setup

1. Create `.env` file:
```bash
cp .env.example .env
```

2. Add your credentials to `.env`:
```env
DEEPSEEK_API_KEY=sk-your-deepseek-key
TELEGRAM_BOT_TOKEN=your-telegram-token
DEEPSEEK_MODEL=deepseek-chat
```

3. Start:
```bash
docker-compose up -d
```

## Usage

### Docker Commands
```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Logs
docker-compose logs -f

# Restart
docker-compose restart

# Rebuild
docker-compose up -d --build
```

### Helper Script
```bash
./run.sh start   # Start bot
./run.sh stop    # Stop bot
./run.sh logs    # View logs
./run.sh status  # Check status
```

### Bot Commands
- `/start` - Start bot
- `/help` - Show help
- `/clear` - Clear conversation history

## Configuration

**System prompt** (`interfaces/telegram/bot.py:51`):
```python
system_prompt="You are a helpful AI assistant."
```

**Context length** (`interfaces/telegram/bot.py:53`):
```python
max_context_messages=10
```

**AI parameters** (`core/agents/deepseek_agent.py:25-26`):
```python
max_tokens=2000
temperature=0.7
```

## Development

Local run without Docker:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Troubleshooting

**Bot doesn't start**: Check logs with `docker-compose logs -f`

**No response**: Verify API keys in `.env` and check Deepseek credits

**Reset**: `docker-compose down && docker-compose up -d`

## Supported Technologies

### AI Providers
- Deepseek (used in this bot)
- OpenAI
- Anthropic Claude
- Google AI
- Cohere
- HuggingFace

### Interfaces
- Telegram (used in this bot)
- Discord
- Web (REST API, WebSocket)
- CLI

### Databases
- PostgreSQL
- MongoDB
- Redis
