import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Берем токен из переменной окружения Render
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот НАФАНЯ запущен и работает ✅")

def main():
    # Инициализация приложения
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Запуск бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
