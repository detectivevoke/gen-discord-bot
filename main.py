import discord
from discord.ext import commands

from bot import GenBot

def main():
    bot = GenBot()
    
    bot.run()

if __name__ == "__main__":
    main()
