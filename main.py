import os
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get('TOKEN')

async def start(update, context):
    await update.message.reply_text('مرحباً! أنا تومي بوت جاهز للعمل!')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
