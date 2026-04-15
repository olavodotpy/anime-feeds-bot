from discord.ext import commands, tasks
import os

from ..core.config import Config



class BotFeeds(commands.Bot):
    """The BotFeeds class initializes the bot and loads the cogs."""
    def __init__(self):
        super().__init__(
            command_prefix = Config.PREFIX,
            intents= Config.INTENTS,
            help_command = None,
        )


    async def setup_hook(self):
        """The setup_hook method searches for .py files in the ./cogs directory."""
        for filename in os.listdir("./cogs"):

            if filename.endswith(".py") and not filename.startswith("__"):
                cog_name = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(cog_name)
                    print(f"Cog loaded: {filename}")
                except Exception as e:
                    print(f"Cog failure {filename}: {type(e).__name__} - {e}")


    async def on_ready(self):
        print(f"Bot Connected with {self.user} (ID: {self.user.id})")
