import asyncio
import datetime as dt
import re
import discord
from discord.ext import commands
import requests
from pathlib import Path
import random
import os

green = 0x2ecc71
red = 0xe74c3c


def setup(bot):
    bot.add_cog(Gen(bot))

class Gen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name = "gen")
    async def gen_command(self, ctx, type=None):
        if type == None:
            await ctx.send(embed=discord.Embed(color=red, description="You need to specify a type!"))
            return
        if type.lower() == "nitro" or type.lower() == "ntro":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "nitro")
            Ooo = random.choice(open(file, "r").readlines())
            print(Ooo)
            w = open(file,"r").read()
            wasd= w.replace("{}".format(Ooo), "")
            open(file, "w").close()
            f = open(file, "a").write(wasd)
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        elif type.lower() == "xbox":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "xbox")
            Ooo = random.choice(open(file, "r").readlines())
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        elif type.lower() == "ps4" or type.lower() == "playstation" or type.lower() == "ps3" or type.lower() == "ps":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "ps")
            Ooo = random.choice(open(file, "r").readlines())
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        elif type.lower() == "amazon":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "amazon")
            Ooo = random.choice(open(file, "r").readlines())
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        elif type.lower() == "mc" or type.lower() == "minecraft":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "minecraft")
            Ooo = random.choice(open(file, "r").readlines())
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        elif type.lower() == "vbuck" or type.lower() == "vbucks":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "vbucks")
            Ooo = random.choice(open(file, "r").readlines())
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        elif type.lower() == "blizzard":
            file = "databases/{}/{}.txt".format(ctx.guild.id, "blizzard")
            Ooo = random.choice(open(file, "r").readlines())
            print(Ooo)
            await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
            msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
            await asyncio.sleep(10)
            await msg.delete()
        else:
            try:
                file = "databases/{}/{}.txt".format(ctx.guild.id, "{}".format(type.lower()))
                Ooo = random.choice(open(file, "r").readlines())
                print(Ooo)
                await ctx.send(embed=discord.Embed(color=green, description="Sent! Check DMS!"))
                msg = await ctx.author.send(embed=discord.Embed(color=green, description=f"```{Ooo}```\n\n This message self destructs in 10 seconds!"))
                await asyncio.sleep(10)
                await msg.delete()
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="Please pick a valid option!"))

    @commands.command(name="stock")
    async def stock_command(self, ctx):
        folder = "databases/{}/".format(ctx.guild.id)
        embed= discord.Embed(color=green)
        for files in os.walk(folder):
            for file in files[2]:
                num_lines = sum(1 for line in open(folder+file, "r"))
                embed.add_field(name=file.replace(".txt","").capitalize(), value=f"{num_lines} items in stock!")
        await ctx.send(embed=embed)
    
    @commands.command(name="help")
    async def help_command(self, ctx, arg=None):
        if arg == None:
            embed= discord.Embed(color=green,title="Commands - Invite me (!invite)",)
            embed.add_field(name="?help database", value="Help setup databases.")
            embed.add_field(name="?create <type", value="Creates a database for that type.")
            embed.add_field(name="?add <type>", value="Puts the file into the database. **Requires an attachment** ")
            embed.add_field(name="?stock", value="Shows how much stock there is.")
            embed.add_field(name="?delete <type>", value="Deletes the database.")
            embed.add_field(name="?gen <type>", value="Generates something from the database.")
            embed.add_field(name="?clear <type>", value="Clears the database for the specific type.")
            await ctx.send(embed=embed)
        elif arg == "database":
            embed = discord.Embed(color=green, title="Database Help - Invite me (!invite)")
            embed.add_field(name="Getting Started", value="Firstly, run ?create all. This will create all templated databases. Run ?stock to see what has been created. Using ?delete <type> will remove the database, and ?add <type> will create the certain type of database.")
            embed.add_field(name="Setup", value="Run ?create <type>. This creates a database for that specific type. Once done, run ?add <type> and attach a file. This will then go into the database. ?gen <type> will then pick one line from the database, and send it to you. ")
            embed.add_field(name="Clearing Databases", value="Run ?clear <type>, this removes all lines in the database.")
            embed.add_field(name="Deleting Databases", value="Running ?delete <type> will fully delete the database. This will not show in ?stock command.")
            embed.add_field(name="Generating", value="With generating, the bot uses the name of the database to get the information, as an example, if you were to create a database called 'fortnite-vbucks', the command would be '?gen fortnite-vbucks'.")
            await ctx.send(embed=embed)
    @commands.command(name="invite")
    async def invite_command(self, ctx):
        embed=discord.Embed(color=green, title="Invite me: https://discord.com/oauth2/authorize?client_id=923530282915745792&permissions=8&scope=bot")
        await ctx.send(embed=embed)

    