import telebot
import os

8743014682:AAHh0HxMGBdJOVWKJIs1aCjCdooYhZ68CAE = os.environ.get('8743014682:AAHh0HxMGBdJOVWKJIs1aCjCdooYhZ68CAE')
bot = telebot.TeleBot(8743014682:AAHh0HxMGBdJOVWKJIs1aCjCdooYhZ68CAE)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "تم تشغيل البوت ياحب#⚡")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()