import discord
from discord.ext import commands
from  openpyxl import *

dosya = load_workbook("Dictator-GS.xlsx")
dosya.get_sheet_by_name("Sayfa1")
sheet = dosya.active
guild_members = 16

class member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = False)
    async def showagree(self ,mesaj):

        emb = discord.Embed(color = 0xff0080)

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            member_SD = sheet["F" + str(i)].value
            if str(member_SD) == "1":
                emb.add_field(name=dosya_aile_adi, value="",inline=False)
            else:
                pass
        await mesaj.send(embed = emb)

    @commands.command(hidden = False)
    async def sayi(self ,mesaj):
        kisi_sayisi = 0

        for i in range(2, guild_members):
            if sheet["F" + str(i)].value == 1:
                kisi_sayisi += 1
        await mesaj.send( "Savaşa "+ str(kisi_sayisi)+ " kişi katılacak." )

    @commands.command(hidden = False)
    async def katil(self ,mesaj):
        display_name = mesaj.author.display_name
        fname = ""
        for i in display_name:
            if i == "/":
                break
            else:
                fname += i

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["F" + str(i)].value = 1

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                member_class = sheet["B" + str(i)].value
                member_AP = sheet["C" + str(i)].value
                member_AP1 = sheet["D" + str(i)].value
                member_DP = sheet["E" + str(i)].value
                member_GS = str(int((int(member_AP) + int(member_AP1)) / 2) + int(member_DP))
                member_SD = sheet["F" + str(i)].value

        if str(member_SD) == "0":
            durum = "Katılmıyor"
        elif str(member_SD) == "1":
            durum = "Katılıyor"
        try:
            emb = discord.Embed(color=0xff0080)
            emb.add_field(name="Aile adı", value=fname)
            emb.add_field(name="Sınıfı", value=member_class)
            emb.add_field(name="GS", value=member_GS)
            emb.add_field(name="AP", value=member_AP)
            emb.add_field(name="Uyanış AP", value=member_AP1)
            emb.add_field(name="DP", value=member_DP)
            emb.add_field(name="Savaş Durumu", value=durum)
            dosya.save("Dictator-GS.xlsx")
            dosya.close()

        except ImportError as e:
            print(e)

        self.bot.unload_extension("commands.member")
        self.bot.load_extension(("commands.member"))
        await mesaj.send("Güncellendi")
        await mesaj.send(embed=emb)

    @commands.command(hidden = False)
    async def showall(self ,mesaj):

        emb = discord.Embed(color = 0xff0080)

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            member_class = sheet["B" + str(i)].value
            member_AP = sheet["C" + str(i)].value
            member_AP1 = sheet["D" + str(i)].value
            member_DP = sheet["E" + str(i)].value
            member_GS = str(int(member_AP) + int(member_DP))
            member_SD = sheet["F" + str(i)].value
            if str(member_SD) == "1":
                emb.add_field(name=dosya_aile_adi, value=(str(member_class)  + "\n" +
                                                          str(member_AP) + "|" +
                                                          str(member_AP1) + "|" +
                                                          str(member_DP)), inline=False)
            else:
                pass
        await mesaj.send(embed = emb)

    @commands.command(hidden = False)
    async def show(self, mesaj , member:discord.Member):
        display_name = member.display_name
        fname = ""
        for i in display_name:
            if i == "/":
                break
            else:
                fname += i
        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                member_class = sheet["B" + str(i)].value
                member_AP = sheet["C" + str(i)].value
                member_AP1 = sheet["D" + str(i)].value
                member_DP = sheet["E" + str(i)].value
                member_GS = str(int((int(member_AP) + int(member_AP1)) / 2) + int(member_DP))
                member_SD = sheet["F" + str(i)].value

        if str(member_SD) == "0":
            durum = "Katılmıyor"
        elif str(member_SD) == "1":
            durum = "Katılıyor"
        try:
            emb = discord.Embed(color=0xff0080)
            emb.add_field(name="Aile adı", value=fname)
            emb.add_field(name="Sınıfı", value=member_class)
            emb.add_field(name="GS", value=member_GS)
            emb.add_field(name="AP", value=member_AP)
            emb.add_field(name="Uyanış AP", value=member_AP1)
            emb.add_field(name="DP", value=member_DP)
            emb.add_field(name="Savaş Durumu", value=durum)
            dosya.save("Dictator-GS.xlsx")
            dosya.close()

        except ImportError as e:
            print(e)

        await mesaj.send(embed = emb)

    @commands.command(hidden=False)
    async def ap(self, mesaj, value: str):
        display_name = mesaj.author.display_name
        fname = ""
        for i in display_name:
            if i == "/":
                break
            else:
                fname += i

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["C" + str(i)].value = int(value)

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                member_class = sheet["B" + str(i)].value
                member_AP = sheet["C" + str(i)].value
                member_AP1 = sheet["D" + str(i)].value
                member_DP = sheet["E" + str(i)].value
                member_GS = str(int((int(member_AP) + int(member_AP1)) / 2) + int(member_DP))
                member_SD = sheet["F" + str(i)].value

        if str(member_SD) == "0":
            durum = "Katılmıyor"
        elif str(member_SD) == "1":
            durum = "Katılıyor"
        try:
            emb = discord.Embed(color=0xff0080)
            emb.add_field(name="Aile adı", value=fname)
            emb.add_field(name="Sınıfı", value=member_class)
            emb.add_field(name="GS", value=member_GS)
            emb.add_field(name="AP", value=member_AP)
            emb.add_field(name="Uyanış AP", value=member_AP1)
            emb.add_field(name="DP", value=member_DP)
            emb.add_field(name="Savaş Durumu", value=durum)
            dosya.save("Dictator-GS.xlsx")
            dosya.close()

        except ImportError as e:
            print(e)

        self.bot.unload_extension("commands.member")
        self.bot.load_extension(("commands.member"))
        await mesaj.send("Güncellendi")
        await mesaj.send(embed=emb)


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

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["D" + str(i)].value = int(value)

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                member_class = sheet["B" + str(i)].value
                member_AP = sheet["C" + str(i)].value
                member_AP1 = sheet["D" + str(i)].value
                member_DP = sheet["E" + str(i)].value
                member_GS = str(int((int(member_AP) + int(member_AP1)) / 2) + int(member_DP))
                member_SD = sheet["F" + str(i)].value

        if str(member_SD) == "0":
            durum = "Katılmıyor"
        elif str(member_SD) == "1":
            durum = "Katılıyor"
        try:
            emb = discord.Embed(color=0xff0080)
            emb.add_field(name="Aile adı", value=fname)
            emb.add_field(name="Sınıfı", value=member_class)
            emb.add_field(name="GS", value=member_GS)
            emb.add_field(name="AP", value=member_AP)
            emb.add_field(name="Uyanış AP", value=member_AP1)
            emb.add_field(name="DP", value=member_DP)
            emb.add_field(name="Savaş Durumu", value=durum)
            dosya.save("Dictator-GS.xlsx")
            dosya.close()

        except ImportError as e:
            print(e)

        self.bot.unload_extension("commands.member")
        self.bot.load_extension(("commands.member"))
        await mesaj.send("Güncellendi")
        await mesaj.send(embed=emb)

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

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                sheet["E" + str(i)].value = int(value)

        for i in range(2, guild_members):
            dosya_aile_adi = sheet["A" + str(i)].value
            if dosya_aile_adi == fname:
                member_class = sheet["B" + str(i)].value
                member_AP = sheet["C" + str(i)].value
                member_AP1 = sheet["D" + str(i)].value
                member_DP = sheet["E" + str(i)].value
                member_GS = str(int((int(member_AP) + int(member_AP1)) / 2) + int(member_DP))
                member_SD = sheet["F" + str(i)].value

        if str(member_SD) == "0":
            durum = "Katılmıyor"
        elif str(member_SD) == "1":
            durum = "Katılıyor"
        try:
            emb = discord.Embed(color=0xff0080)
            emb.add_field(name="Aile adı", value=fname)
            emb.add_field(name="Sınıfı", value=member_class)
            emb.add_field(name="GS", value=member_GS)
            emb.add_field(name="AP", value=member_AP)
            emb.add_field(name="Uyanış AP", value=member_AP1)
            emb.add_field(name="DP", value=member_DP)
            emb.add_field(name="Savaş Durumu", value=durum)
            dosya.save("Dictator-GS.xlsx")
            dosya.close()

        except ImportError as e:
            print(e)

        self.bot.unload_extension("commands.member")
        self.bot.load_extension(("commands.member"))
        await mesaj.send("Güncellendi")
        await mesaj.send(embed=emb)
def setup(bot):
    bot.add_cog(member(bot))