from telebot.async_telebot import AsyncTeleBot

from django.conf import settings

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, 'Пользовательское соглашение')



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


