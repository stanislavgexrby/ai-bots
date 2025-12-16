"""
Main entry point for the Telegram bot.
"""

import os
from dotenv import load_dotenv
from interfaces.telegram import start_bot


def main():
    """
    Load environment variables and start the bot.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Start the Telegram bot
    start_bot()


if __name__ == "__main__":
    main()
