
НАСТРОЙКА TELEGRAM-БОТА НА RENDER

1. Зарегистрируйся на https://render.com/
2. Создай новый Web Service → подключи папку с app.py (или загрузи ZIP).
3. В Settings → добавь переменные окружения:
   BOT_TOKEN = твой токен бота
   (chat_id уже встроен в код, если один пользователь)
4. Укажи:
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py
5. После деплоя получи URL вида https://имя.onrender.com
6. Установи webhook:
   https://api.telegram.org/bot<ТОКЕН>/setWebhook?url=<URL>/webhook

После этого бот начнет принимать команды напрямую в Telegram.
