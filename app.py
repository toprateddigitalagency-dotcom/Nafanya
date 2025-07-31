import os
from telegram.ext import Application, CommandHandler
from commands.help import help_command
from commands.balance import balance_command
from commands.addorder import addorder_command
from commands.orders import orders_command
from commands.profit import profit_command

TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("balance", balance_command))
    app.add_handler(CommandHandler("addorder", addorder_command))
    app.add_handler(CommandHandler("orders", orders_command))
    app.add_handler(CommandHandler("profit", profit_command))

    print("НАФАНЯ запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
