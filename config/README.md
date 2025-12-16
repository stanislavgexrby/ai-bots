# Configuration

## Configuration Setup

### Option 1: Using .env file

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in the required parameters

3. Use `python-dotenv` library to load environment variables:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Option 2: Using Python configuration

1. Copy `config.example.py` to `config.py`:
   ```bash
   cp config/config.example.py config/config.py
   ```

2. Edit `config.py` according to your needs

3. Import configuration in your code:
   ```python
   from config.config import Config
   ```

## Configuration Structure

### AI API
- Support for various AI providers: OpenAI, Anthropic, Google AI, Cohere, HuggingFace
- Model settings, tokens, and generation parameters

### Databases
- **PostgreSQL** - for relational data
- **MongoDB** - for document-oriented storage
- **Redis** - for caching and sessions

### Interfaces
- **Telegram** - bot configuration (token, webhook)
- **Web** - web server settings (host, port, CORS)
