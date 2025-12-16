# AI Bots Framework

Universal framework for developing AI bots with modular architecture.

## Current Bot: Telegram Bot with Deepseek API

Simple Telegram bot that uses Deepseek API for generating responses. Maintains conversation context for each user.

**Features:**
- Conversation context management
- Basic commands (/start, /help, /clear)
- Docker deployment ready

**Setup:**
```bash
cp .env.example .env
# Add DEEPSEEK_API_KEY and TELEGRAM_BOT_TOKEN
docker-compose up -d
```

Full documentation: [BOT_README.md](BOT_README.md)

## Architecture

### Structure
```
core/
├── agents/             - AI agent implementations
│   └── deepseek_agent.py
└── processors/         - Message processing
    └── message_processor.py

interfaces/
└── telegram/          - Telegram bot interface
    └── bot.py

main.py                - Entry point
```

### Components
- **DeepseekAgent** - API client for Deepseek
- **MessageProcessor** - Context management
- **TelegramBot** - Telegram interface handlers

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
