from telebot.async_telebot import AsyncTeleBot, types

from django.conf import settings

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
    stop = types.KeyboardButton(text='отмена')
    agree = types.KeyboardButton(text='принять')
    keyboard.add(stop)
    keyboard.add(agree)
    await bot.send_message(message.chat.id, 'Пользовательское соглашение', reply_markup=keyboard)



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


