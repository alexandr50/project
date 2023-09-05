from django.core.management.base import BaseCommand

from project.settings import TOKEN_BOT
from telebot import TeleBot



bot = TeleBot(TOKEN_BOT, threaded=False)



class Command(BaseCommand):

    help = 'Some information'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()

