import asyncio
import datetime as dt
import re
import discord
from discord.ext import commands
import requests
from discord.ext.commands import Bot, has_permissions, CheckFailure

green = 0x2ecc71
red = 0xe74c3c

import os


def setup(bot):
    bot.add_cog(Main(bot))


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


        
    @commands.command(name="create")
    @has_permissions(administrator=True)
    async def create_db(self, ctx, type=None):
        if type == None:
            
            newpath = r'databases\{}'.format(ctx.guild.id) 
            if not os.path.exists(newpath):
                os.makedirs(newpath)
                await ctx.send(embed=discord.Embed(color=green, description="Base Database Created! Do ?createdb <type> to create a certain database!"))
            else:
                await ctx.send(embed=discord.Embed(color=red, description="You have already created your base database! Do ?createdb <type> to create a certain database!"))
        else:

            if type.lower() == "nitro":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "nitro"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created nitro database! This database is setup to your Nitro command already!"))
            elif type.lower() == "minecraft" or type.lower() == "mc":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "minecraft"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created Minecraft database! This database is setup to your Minecraft command already!"))
            elif type.lower() == "vbucks" or type.lower() == "vbuck":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "vbucks"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created VBucks database! This database is setup to your VBucks command already!"))
            elif type.lower() == "amazon":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "amazon"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created Amazon database! This database is setup to your Amazon command already!"))
            elif type.lower() == "xbox":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "xbox"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created Xbox database! This database is setup to your Xbox command already!"))
            elif type.lower() == "ps" or type.lower() == "ps4" or type.lower() == "ps3" or type.lower() == "playstation":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "ps"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created PlayStation database! This database is setup to your PlayStation command already!"))
            elif type.lower() == "blizzard":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "blizzard"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created Blizzard database! This database is setup to your Blizzard command already!"))
            elif type.lower() == "all":
                newpath = r'databases\{}'.format(ctx.guild.id) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                open("databases/{}/{}.txt".format(ctx.guild.id, "minecraft"),"a")
                open("databases/{}/{}.txt".format(ctx.guild.id, "nitro"),"a")
                open("databases/{}/{}.txt".format(ctx.guild.id, "vbucks"),"a")
                open("databases/{}/{}.txt".format(ctx.guild.id, "xbox"),"a")
                open("databases/{}/{}.txt".format(ctx.guild.id, "ps"),"a")
                open("databases/{}/{}.txt".format(ctx.guild.id, "amazon"),"a")
                open("databases/{}/{}.txt".format(ctx.guild.id, "blizzard"),"a")
                await ctx.send(embed=discord.Embed(color=green, description=f"Created All databases! These databases are now all setup to your commands!"))
            else:
                    newpath = r'databases\{}'.format(ctx.guild.id) 
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    open("databases/{}/{}.txt".format(ctx.guild.id, "{}".format(type.lower())),"a")
                    await ctx.send(embed=discord.Embed(color=green, description="Created {} database! This database is setup to your {} command already!".format(type,type)))
    
    @commands.command(name="clear")
    @has_permissions(administrator=True)
    async def clear_db(self, ctx, type=None):
        if type == None:
            return await ctx.send(embed=discord.Embed(color=red, description="You need to specify the database!"))
        
        newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, type.lower()) 
        guild = f"databases/{ctx.guild.id}/{type.lower()}.txt"
        with open(f"{guild}", "a")as w:
            w.truncate(0)
        w.close()
        await ctx.send(embed=discord.Embed(color=green, description="Cleared database!"))

    @commands.command(name="add")
    @has_permissions(administrator=True)
    async def addcmd(self, ctx, type=None):
        

        if type == None:
            return await ctx.send(embed=discord.Embed(color=red, description="You need to specify the database!"))
        
        newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, type.lower())
        if not os.path.exists(newpath):
            return await ctx.send(embed=discord.Embed(color=red, description="There is no database for {}!".format(type)))
        try:
            url = ctx.message.attachments[0].url
            if ctx.message.attachments[0].url:
                r = requests.get(url, allow_redirects=True)
                file = f"databases/{ctx.guild.id}/{type}.txt"
                with open(file, "a+") as w:
                    f = w.read()
                    send = f + r.text.replace("\n","")
                    w.write(send)
                w.close()
            await ctx.send(embed=discord.Embed(color=green, description="I have added your file to the database!"))
        except:
            return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
    
    @commands.command(name="check")
    async def check_cmd(self, ctx, type=None):
        if type == None:
            return await ctx.send(embed=discord.Embed(color=red, description="You need to specify the database!"))
        
        newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, type.lower()) 

        file = f"databases/{ctx.guild.id}/{type}.txt"
        num_lines = sum(1 for line in open(file, "r"))
        await ctx.send(embed=discord.Embed(color=green, description=f"You have {num_lines} items in your database!"))

    @commands.command(name="delete")
    async def delete_cmd(self,ctx,type=None):
        if type == None:
            return await ctx.send(embed=discord.Embed(color=red, description="You need to specify the database! "))
        if type.lower() == "minecraft" or type.lower() == "mc":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "minecraft") 
            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
        elif type.lower() == "amazon":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "amazon") 

            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
        elif type.lower() == "blizzard":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "") 
            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
        elif type.lower() == "nitro":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "nitro") 
            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
        elif type.lower() == "ps" or type.lower() == "ps4" or type.lower() == "playstation" or type.lower() == "ps3":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "ps") 
            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
        elif type.lower() == "xbox":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "xbox") 
            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!"))
        elif type.lower() == "vbucks" or type.lower() == "vbuck":
            newpath = r'databases\{}\{}.txt'.format(ctx.guild.id, "vbucks")
        try:
            file = f"databases/{ctx.guild.id}/{type}.txt"
            os.remove(file)
        except:
            try:
                file = f"databases/{ctx.guild.id}/{type}.txt"
                os.remove(file)
                await ctx.send(embed=discord.Embed(color=green, description=f"Removed {type} from database"))
            except:
                return await ctx.send(embed=discord.Embed(color=red, description="An error has occurred!")) 