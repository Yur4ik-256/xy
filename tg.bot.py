import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

MY_BOT_TOKEN = '7055644784:AAEqfOkIcq3KI8bjpxggLoeW0aRkzjLtiIo'

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка сообщения при команде /start."""
    await update.message.reply_text("Привет! Я калькулятор. Напиши мне выражение для вычисления.")


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка арифметических выражений."""
    user_input = update.message.text

    try:
        # Вычисление результата
        result = eval(user_input)
        await update.message.reply_text(f"Результат: {result}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}. Пожалуйста, проверьте Ваше выражение.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка справочной информации при команде /help."""
    help_text = "правильное написание:\nумножение *\nделение /\nстепень **"
    await update.message.reply_text(help_text)

def main() -> None:
    """Запуск бота."""
    application = ApplicationBuilder().token(MY_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))  # Добавлено
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    application.run_polling()


if __name__ == "__main__":
    main()
