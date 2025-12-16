#!/bin/bash

# Simple script to manage the Telegram bot

case "$1" in
    start)
        echo "Starting Telegram bot..."
        docker-compose up -d
        echo "Bot started! Check logs with: ./run.sh logs"
        ;;
    stop)
        echo "Stopping Telegram bot..."
        docker-compose down
        echo "Bot stopped!"
        ;;
    restart)
        echo "Restarting Telegram bot..."
        docker-compose restart
        echo "Bot restarted!"
        ;;
    logs)
        docker-compose logs -f telegram-bot
        ;;
    build)
        echo "Rebuilding and starting bot..."
        docker-compose up -d --build
        echo "Bot rebuilt and started!"
        ;;
    status)
        docker-compose ps
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|logs|build|status}"
        echo ""
        echo "Commands:"
        echo "  start   - Start the bot"
        echo "  stop    - Stop the bot"
        echo "  restart - Restart the bot"
        echo "  logs    - Show bot logs (Ctrl+C to exit)"
        echo "  build   - Rebuild and start the bot"
        echo "  status  - Show bot status"
        exit 1
        ;;
esac
