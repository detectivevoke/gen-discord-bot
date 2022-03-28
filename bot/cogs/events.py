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
    bot.add_cog(Events(bot))


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command("help")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot ready.")
    @commands.Cog.listener()
    async def on_connect(self):
        print(f" Connected to Discord.")



        