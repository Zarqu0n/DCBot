import discord
from discord.ext import commands

token = "NzY0ODIxMzkxMzIwNjc4NDMw.X4L1bQ.xUuWtbXB335uMzo64M2_70fF8xo"

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