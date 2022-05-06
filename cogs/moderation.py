import calendar
import datetime
import discord
from discord.ext import commands
from discord import app_commands    
from discord.app_commands import Choice


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Ban specified user")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        if member == self.bot:
            return await interaction.response.send_message("You cannot ban me!", ephemeral=True)
        if member == interaction.user:
            await interaction.response.send_message('``You Cannot Ban Yourself!``')
        else:
            if interaction.user.top_role >= member.top_role:
                return
            else:
                try:
                    user = await commands.converter.UserConverter().convert(interaction, user)
                except:
                    await interaction.response.send_message("Error: user could not be found!")
                    return  


                date = datetime.datetime.utcnow()
                utc_time = calendar.timegm(date.utctimetuple()) 

                embed = discord.Embed(title=f"*{member} was banned!*", description=f"Reason: {reason} \n Member banned at <t:{utc_time}:F>")

                await member.send(f'``You Have Been Banned From {interaction.guild.name} for \n {reason}``')
                await member.ban(reason=reason)
                await interaction.response.send_message(embed=embed) 

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))