import os
import sqlite3
import discord
from discord.ext import commands
import asyncio
import config
from discord import app_commands


class MyBot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        if self.shard_count >= 1:
            print(f'Running {self.shard_count} shard')
        else:
            print(f'Running {self.shard_count} shards')

intents = discord.Intents.all()
bot = MyBot(command_prefix="yan", intents=intents, status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name='Questionable Things'))

async def main():
    async with bot:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
            else:
                print(f'Unable to load {filename[:-3]}')
        await bot.load_extension('jishaku')
        await bot.start(config.token)


asyncio.run(main())