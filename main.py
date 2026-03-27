import asyncio
from bot.core.bot import AnimeFeeds
from bot.core.config import Config



async def main():
    bot = AnimeFeeds()
    await bot.start(token=Config.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
