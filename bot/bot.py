from pathlib import Path

import discord
from discord.ext import commands


class GenBot(commands.Bot):
    def __init__(self):
        
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix=self.prefix, case_insensitive=True)

    def setup(self):
        print("Running setup...")

        for cog in self._cogs:
            self.remove_command("help")
            self.load_extension(f"bot.cogs.{cog}")
            print(f" Loaded {cog}.")

        print("Setup complete.")

    def run(self):
        self.setup()

        with open("data/token.txt", "r", encoding="utf-8") as f:
            TOKEN = f.read()
        f.close()
        print("Running bot...")
        super().run(TOKEN, reconnect=True)

    async def shutdown(self):
        print("Closing connection to Discord...")
        await super().close()

    async def close(self):
        print("Closing on keyboard interrupt...")
        await self.shutdown()

    
    async def on_resumed(self):
        print("Bot resumed.")

    async def on_disconnect(self):
        print("Bot disconnected.")

    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or("?")(bot, msg)
        

    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)
        