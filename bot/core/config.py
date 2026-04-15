import discord
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """The Config class stores the project's global variables."""
    TOKEN = os.getenv("DISCORD_TOKEN")
    PREFIX = "!"
    INTENTS = discord.Intents.default()
    INTENTS.messages = True
    INTENTS.message_content = True
    FEED_CHANNEL_ID = 1486455880219365446
    DEFAULT_TIME = 600

