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
