import discord
from discord.ext import commands, tasks
from bot.services.feed_service import Fetch
from bot.core.config import Config
from logging import error, log



class EmbedNews(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.service = Fetch()
        self.send_embed.start()


    @tasks.loop(seconds=30)
    async def send_embed(self):        
        try:
            channel = await self.bot.fetch_channel(Config.FEED_CHANNEL_ID)

            for source in ["myanimelist","crunchyroll"]:
                url = f"http://127.0.0.1:8000/api/last/{source}"
                response = await self.service.__smart_polling__(url)

                if channel:

                    for post in response:
                        color = post.get("mal_color")

                        if source == "crunchyroll":
                                color = post.get("cr_color")

                        embed = discord.Embed(title=post.get("title"), color=color)

                        if post.get("author") != "desconhecido":
                            embed.set_author(
                                name=post.get("author")
                            )
                        
                        embed.set_image(
                            url=post.get("image")
                        )

                        embed.add_field(
                            name=post.get("source"),
                            value=f"Fonte: {post.get("link")}",
                        )

                        await channel.send(embed=embed)

        except Exception as e:
                error(f"Erro in send_embed: {e}")


    @send_embed.before_loop
    async def before_send_embed(self):
        await self.bot.wait_until_ready()
        
        print("Task started!!")


async def setup(bot):
    await bot.add_cog(EmbedNews(bot))
