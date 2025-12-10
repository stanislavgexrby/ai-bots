# AI Bots Framework

Universal framework for developing AI bots and agents with different interaction interfaces.

## Concept

This repository provides a base structure for building AI bots with clear separation between processing logic and interaction interfaces. The main branch contains the common project structure, while separate branches can contain specific bot implementations with different architectures and interfaces.

## Architecture Principles

### Separation of Concerns

- **Core** - main AI processing logic, independent of the interface
- **Interfaces** - different ways to interact with users (Telegram, Web, CLI)
- **Database** - data layer, universal for all interfaces

### Modularity

Each repository branch can contain its own bot implementation with unique capabilities while using the common structure and configuration approaches.

## Project Structure

```
ai-bots/
├── core/                    # Main AI logic
│   ├── agents/             # AI agent implementations
│   └── processors/         # Request and response processors
│
├── interfaces/             # Interaction interfaces
│   ├── telegram/          # Telegram bot interface
│   ├── web/               # Web interface (REST API, WebSocket)
│   └── cli/               # Command-line interface
│
├── database/               # Database layer
│   ├── models/            # Data models
│   └── migrations/        # Database schema migrations
│
├── config/                 # Configuration files
│   ├── config.example.py  # Configuration example
│   └── README.md          # Configuration documentation
│
├── utils/                  # Helper functions and utilities
├── tests/                  # Tests
└── logs/                   # Application logs
```

## Quick Start

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-bots
```

### 2. Configuration setup

Choose one of the configuration methods:

**Option A: Using .env file**

```bash
cp .env.example .env
# Edit .env and add your API keys
```

**Option B: Using Python configuration**

```bash
cp config/config.example.py config/config.py
# Edit config/config.py according to your needs
```

## Configuration

### Supported AI Providers

- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude)
- Google AI
- Cohere
- HuggingFace

### Supported Databases

- PostgreSQL - for relational data
- MongoDB - for document-oriented storage
- Redis - for caching and session management

## Development

### Creating a new branch for a bot

1. Create a new branch from main:
   ```bash
   git switch -c <bot-name>
   ```

2. Implement the required logic in the appropriate directories

3. Maintain the base project structure, adding only necessary implementation files

### Structure Guidelines

- **core/agents/** - place AI agent classes here
- **core/processors/** - message processing logic
- **interfaces/<type>/** - interface-specific code
- **database/models/** - data models for ORM
- **utils/** - reusable functions
