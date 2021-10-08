import discord
from discord.ext import commands

token = "your discord token"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!d",pm_help = None ,description= "")

        self.load_extension("commands.update")
        self.load_extension("commands.member")
        #self.load_extension("commands.ap")
    async def on_ready(self):
        print("Bot çalışıyor..")

    async  def on_command_error(self, context, exception):
         if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
             await context.send("Böyle bir komut bulunamadı.")
bot = Bot()
bot.run(token)