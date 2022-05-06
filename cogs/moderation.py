import calendar
import datetime
import discord
from discord.ext import commands
from discord import app_commands    
from discord.app_commands import Choice


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot



async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))