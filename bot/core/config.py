import discord
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv("DISCORD_TOKEN")
    PREFIX = "!"
    INTENTS = discord.Intents.default()
    INTENTS.messages = True
    INTENTS.message_content = True
    FEED_CHANNEL_ID = 1486455880219365446
