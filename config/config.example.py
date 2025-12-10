"""
Пример конфигурационного файла для AI ботов.
Скопируйте этот файл как config.py и заполните необходимые параметры.
"""

import os
from typing import Dict, Any


class BaseConfig:
    """Базовая конфигурация для всех ботов"""

    # Общие настройки
    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")


class AIConfig:
    """Конфигурация для AI провайдеров"""

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
    OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "2000"))
    OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

    # Anthropic Claude
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")

    # Google AI
    GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")

    # Другие провайдеры
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


class DatabaseConfig:
    """Конфигурация для баз данных"""

    # PostgreSQL
    POSTGRES_CONFIG = {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "port": int(os.getenv("POSTGRES_PORT", "5432")),
        "database": os.getenv("POSTGRES_DB", "ai_bots_db"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
    }

    # MongoDB
    MONGO_CONFIG = {
        "host": os.getenv("MONGO_HOST", "localhost"),
        "port": int(os.getenv("MONGO_PORT", "27017")),
        "database": os.getenv("MONGO_DB", "ai_bots_db"),
        "username": os.getenv("MONGO_USER"),
        "password": os.getenv("MONGO_PASSWORD"),
    }

    # Redis
    REDIS_CONFIG = {
        "host": os.getenv("REDIS_HOST", "localhost"),
        "port": int(os.getenv("REDIS_PORT", "6379")),
        "password": os.getenv("REDIS_PASSWORD"),
        "db": int(os.getenv("REDIS_DB", "0")),
    }


class TelegramConfig:
    """Конфигурация для Telegram бота"""

    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
    USE_WEBHOOK = bool(os.getenv("TELEGRAM_USE_WEBHOOK", False))


class WebConfig:
    """Конфигурация для веб-интерфейса"""

    HOST = os.getenv("WEB_HOST", "0.0.0.0")
    PORT = int(os.getenv("WEB_PORT", "8000"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",")


class Config(BaseConfig, AIConfig, DatabaseConfig, TelegramConfig, WebConfig):
    """Общая конфигурация приложения"""

    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """Возвращает словарь с конфигурацией"""
        return {
            key: getattr(cls, key)
            for key in dir(cls)
            if not key.startswith("_") and key.isupper()
        }

    @classmethod
    def validate(cls) -> bool:
        """Проверяет наличие обязательных параметров"""
        required_vars = []

        # Добавьте сюда обязательные переменные для вашего бота
        # Например:
        # if not cls.OPENAI_API_KEY:
        #     required_vars.append("OPENAI_API_KEY")

        if required_vars:
            raise ValueError(
                f"Отсутствуют обязательные переменные окружения: {', '.join(required_vars)}"
            )

        return True
