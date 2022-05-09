import os
import random
import sqlite3
import discord
from discord.ext import commands, tasks
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
            for extension in bot.cogs:
                print(f"Loaded cogs.{extension.lower()}")
        else:
            print(f'Running {self.shard_count} shards')
            for extension in self.cogs:
                print(f"Loaded cogs.{extension.lower()}")

    async def setup_hook(self):
        self.loop.create_task(ch_pr())

intents = discord.Intents.all()
bot = MyBot(command_prefix="yan ", intents=intents)

@tasks.loop(seconds=30)
async def ch_pr():
    await bot.wait_until_ready()

    statuses = ['Questionable Things', f'{len(bot.guilds)} servers!', 'thino.pics', 'hentai', 'porn']

    while not bot.is_closed():

        status = random.choice(statuses)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching   , name=status))

        await asyncio.sleep(30)

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