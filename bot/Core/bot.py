from discord.ext import commands, tasks
import os

from .config import Config



class AnimeFeeds(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = Config.PREFIX,
            intents= Config.INTENTS,
            help_command = None,
        )


    async def on_ready(self):
        print(f"Bot Connected with {self.user} (ID: {self.user.id})")
