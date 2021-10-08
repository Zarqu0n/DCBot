import discord
from discord.ext import commands
from  openpyxl import *

dosya = load_workbook("Dictator-GS.xlsx")
dosya.get_sheet_by_name("Sayfa1")
sheet = dosya.active

class updateap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = False)
    async def ap(self, mesaj , value:str):
        display_name = mesaj.author.display_name
        print()
        fname = ""
        for i in display_name:
            if i == "/":
                break
            else:
                fname += i

        for i in range(2, 15):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["C" + str(i)].value = int(value)

        for i in range(2, 15):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                member_class = sheet["B" + str(i)].value
                member_AP = sheet["C" + str(i)].value
                member_AP1 = sheet["D" + str(i)].value
                member_DP = sheet["E" + str(i)].value
                member_GS = str(int(member_AP) + int(member_DP))

        try:
            emb = discord.Embed(color=0xff0080)
            emb.add_field(name="Aile adı", value=fname)
            emb.add_field(name="Sınıfı", value=member_class)
            emb.add_field(name="GS", value=member_GS)
            emb.add_field(name="AP", value=member_AP)
            emb.add_field(name="Uyanış AP", value=member_AP1)
            emb.add_field(name="DP", value=member_DP)

            dosya.save("Dictator-GS.xlsx")
            dosya.close()
            self.bot.unload_extension("commands.member")
            self.bot.load_extension(("commands.member"))
            await mesaj.send("Güncellendi")
            await mesaj.send(embed=emb)
        except ImportError as e:
            print(e)

    @commands.command(hidden=False)
    async def aap(self, mesaj, value: str):
        display_name = mesaj.author.display_name
        print()
        fname = ""

        for i in display_name:
            if i == "/":
                break
            else:
                fname += i

        for i in range(2, 15):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["D" + str(i)].value = int(value)

        try:
            dosya.save("Dictator-GS.xlsx")
            dosya.close()
            self.bot.unload_extension("commands.member")
            self.bot.load_extension(("commands.member"))
            await mesaj.send("Güncellendi")
        except ImportError as e:
            print(e)

    @commands.command(hidden=False)
    async def dp(self, mesaj, value: str):
        display_name = mesaj.author.display_name
        print()
        fname = ""
        for i in display_name:
            if i == "/":
                break
            else:
                fname += i

        for i in range(2, 15):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["E" + str(i)].value = int(value)

        try:
            dosya.save("Dictator-GS.xlsx")
            dosya.close()
            self.bot.unload_extension("commands.member")
            self.bot.load_extension(("commands.member"))
            await mesaj.send("Güncellendi")
        except ImportError as e:
            print(e)

def setup(bot):
    bot.add_cog(updateap(bot))