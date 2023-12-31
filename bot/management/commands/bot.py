import asyncio

from django.core.management.base import BaseCommand

from bot.main_bot import bot


class Command(BaseCommand):
    help = 'Some information'

    def handle(self, *args, **kwargs):
        asyncio.run(bot.polling())
