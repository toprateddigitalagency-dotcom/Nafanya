import os
from telegram.ext import Application, CommandHandler
from commands.help import help_command
from commands.balance import balance_command

TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("balance", balance_command))

    print("НАФАНЯ запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
