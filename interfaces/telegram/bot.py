"""
Telegram Bot

Simple Telegram bot that uses Deepseek API for generating responses.
"""

import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from core.agents import DeepseekAgent
from core.processors import MessageProcessor


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class TelegramBot:
    """
    Telegram bot with Deepseek AI integration.
    """

    def __init__(self, telegram_token: str, deepseek_api_key: str, deepseek_model: str = "deepseek-chat"):
        """
        Initialize Telegram bot.

        Args:
            telegram_token: Telegram bot token
            deepseek_api_key: Deepseek API key
            deepseek_model: Deepseek model name
        """
        self.telegram_token = telegram_token

        # Initialize AI agent
        self.agent = DeepseekAgent(
            api_key=deepseek_api_key,
            model=deepseek_model
        )

        # Initialize message processor
        self.processor = MessageProcessor(
            agent=self.agent,
            system_prompt="You are a helpful AI assistant in Telegram. Be concise and friendly."
        )

        logger.info("Telegram bot initialized")

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handle /start command.
        """
        user = update.effective_user
        await update.message.reply_text(
            f"Hi {user.first_name}! 👋\n\n"
            f"I'm an AI assistant powered by Deepseek. Ask me anything!\n\n"
            f"Commands:\n"
            f"/start - Start the bot\n"
            f"/clear - Clear conversation history\n"
            f"/help - Show this message"
        )
        logger.info(f"User {user.id} started the bot")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handle /help command.
        """
        await update.message.reply_text(
            "🤖 AI Assistant Help\n\n"
            "Just send me any message and I'll respond!\n\n"
            "Commands:\n"
            "/start - Start the bot\n"
            "/clear - Clear conversation history\n"
            "/help - Show this message\n\n"
            "Powered by Deepseek API"
        )

    async def clear_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handle /clear command - clears conversation history.
        """
        user_id = str(update.effective_user.id)
        self.processor.clear_context(user_id)
        await update.message.reply_text("✅ Conversation history cleared!")
        logger.info(f"User {user_id} cleared conversation history")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handle user messages.
        """
        user = update.effective_user
        user_id = str(user.id)
        message_text = update.message.text

        logger.info(f"Received message from user {user_id}: {message_text[:50]}...")

        # Show typing indicator
        await update.message.chat.send_action(action="typing")

        try:
            # Process message and get response
            response = self.processor.process_message(user_id, message_text)

            # Send response
            await update.message.reply_text(response)
            logger.info(f"Sent response to user {user_id}")

        except Exception as e:
            logger.error(f"Error handling message: {e}")
            await update.message.reply_text(
                "Sorry, I encountered an error. Please try again later."
            )

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Handle errors.
        """
        logger.error(f"Update {update} caused error: {context.error}")

    def run(self):
        """
        Start the bot.
        """
        logger.info("Starting Telegram bot...")

        # Create application
        application = Application.builder().token(self.telegram_token).build()

        # Add handlers
        application.add_handler(CommandHandler("start", self.start_command))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("clear", self.clear_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Add error handler
        application.add_error_handler(self.error_handler)

        # Start bot
        logger.info("Bot is running...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)


def start_bot():
    """
    Initialize and start the Telegram bot.
    """
    # Get configuration from environment variables
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    deepseek_model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    if not telegram_token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

    if not deepseek_api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")

    # Create and run bot
    bot = TelegramBot(
        telegram_token=telegram_token,
        deepseek_api_key=deepseek_api_key,
        deepseek_model=deepseek_model
    )

    bot.run()
