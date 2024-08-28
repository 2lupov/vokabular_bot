from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler

# Ваш токен
TOKEN = '7456144617:AAG7w0k2Dy6sZgPpUpqkmYZ50iRy8NTJ-4E'

def start(update, context):
    # Создание кнопки с Web App
    web_app = WebAppInfo(url="https://your-domain.com/mini-app")  # Укажите URL вашего мини-приложения
    button = InlineKeyboardButton(text="Изучать слова", web_app=web_app)
    
    keyboard = [[button]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Нажмите кнопку ниже, чтобы начать изучать слова:", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    # Команда /start
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
