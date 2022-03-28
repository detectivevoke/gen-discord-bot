import asyncio
import datetime as dt
import re
import discord
from discord.ext import commands
import requests

green = 0x2ecc71
red = 0xe74c3c

import os


def setup(bot):
    bot.add_cog(Error_Handler(bot))


class Error_Handler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, error, ctx):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(embed=discord.Embed(color=red, description="You dont have permission to do this!"))
            elif isinstance(error, commands.NoPrivateMessage):
                try:
                    await ctx.author.send(embed=discord.Embed(color=red, description=f'{ctx.command} can not be used in Private Messages.'))
                except discord.HTTPException:
                    pass
            elif isinstance(error, commands.MissingRequiredArgument):
                    await ctx.send(embed=discord.Embed(color=red, description="You need to add arguments!"))
            elif isinstance(error, commands.CommandNotFound):
                await ctx.send(embed=discord.Embed(color=red, description="That is not a command!"))
    
    @commands.Cog.listener()
    async def on_error(self , error, ctx):
        await ctx.send(embed=discord.Embed(color=red, description="An error has occured!"))