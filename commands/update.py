import discord
from discord.ext import commands

class updatekomut(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = False)
    async def update(self, mesaj , value:str):
        dizin = "commands."

        try:
            self.bot.unload_extension(dizin + value)
            self.bot.load_extension((dizin + value))

            await mesaj.send("Güncellendi")
        except ImportError as e:
            print(e)

def setup(bot):
    bot.add_cog(updatekomut(bot))