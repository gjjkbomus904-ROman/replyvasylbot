from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TARGET_TAG = "@Grisha4000"  # тег, на который бот должен реагировать

async def mention_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if TARGET_TAG in update.message.text:
            await update.message.reply_text( 
                "Шановний сусіде!\n\n" "Ваше питання є дуже важливим для нас, ми обов'язково розглянемо його в порядку черги і надамо Вам відповідь!\n\n"
                "Просимо очікувати!\n\n" 
                "З повагою\n"
                "Правління" )

def main():
    print("Бот запущен...")

    app = ApplicationBuilder().token("8329325514:AAGXjiwujzE8FCfMQxPlFPFqd350keki03U").build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mention_handler))

    # ВАЖНО: запускаем без asyncio.run()
    app.run_polling()

if __name__ == "__main__":
    main()

