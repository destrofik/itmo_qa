from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import config
import handlers

def main():
    app = ApplicationBuilder().token(config.TOKEN).build()

    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("help", handlers.help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message))

    print("Бот запущен")
    app.run_polling()

if __name__ == '__main__':
    main()
