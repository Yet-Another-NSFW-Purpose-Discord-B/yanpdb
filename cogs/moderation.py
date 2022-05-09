import calendar
import datetime
from discord import app_commands
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Bans a specified user")
    @app_commands.checks.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, interaction: discord.Interaction, member: discord.Member = None, *, reason: str = None):
        if member == None:
            await interaction.response.send_message("``Who Are You Banning?``")
        else:
            if member == self.bot.user:
                await interaction.response.send_message("``You Cannot Ban Me!``")
            else:
                if member == interaction.user:
                    await interaction.response.send_message("``You Cannot Ban Yourself!``")
                else:

                    if reason == None:
                        reason = "No Reason Specified"

                    date = datetime.datetime.utcnow()
                    utc_time = calendar.timegm(date.utctimetuple())

                    embed = discord.Embed(
                        title=f"*{member} was banned!*", description=f"Reason: {reason} \n Member banned at <t:{utc_time}:F>"
                    )

                    await member.send(f"``You Have Been Banned From {interaction.guild.name} for \n {reason}``")
                    await member.ban(reason=reason)
                    await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Unbans a user")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, *, user: str=None):
        if user == None:
            await interaction.response.send_message("``Who Are You Banning?``")
        else:
            try:
                user = await commands.converter.UserConverter().convert(interaction, user)
            except:
                await interaction.response.send_message("Error: user could not be found!")
                return

            print(user)

            try:
                try:
                    await interaction.guild.unban(user, reason="Responsible moderator: " + str(interaction.user))

                    embed = discord.Embed(title="Successfully unbanned", description=f"{user.mention}")
                    await interaction.response.send_message(embed=embed)
                    return
                except discord.errors.NotFound:
                    return

            except discord.Forbidden:
                await interaction.response.send_message("I do not have permission to unban!")
                return

            except:
                return await interaction.response.send_message("Unbanning failed!")

    @app_commands.command(description="Kicks a user")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member = None, *, reason: str=None):
        if member == None:
            await interaction.response.send_message("Who are you kicking?")
        else:
            if member == interaction.user:
                await interaction.response.send_message("``You Cannot kick Yourself!``")
            if reason == None:
                reason = "No Reason Specified"

            embed = discord.Embed(
                title=f"Successfully kicked {member}",
                description=f"Reason: {reason}",
                timestamp=datetime.datetime.utcnow(),
                color=0xFF0000,
            )
            embed.set_footer(text=member, icon_url=member.display_avatar.url)
            await member.send(f"``You Have Been Kicked From {interaction.guild.name} for\n``{reason}``")
            await member.kick(reason=reason)
            await interaction.response.send_message(embed=embed)


    @app_commands.command(description="Bans a user using the method 'hackban'")
    @app_commands.checks.has_permissions(ban_members=True)
    async def hackban(self, interaction: discord.Interaction, user: str=None, *, reason: str=None):
        guild = interaction.guild
        if user == None:
            return await interaction.response.send_message("You need to specify a user!")
        if reason == None:
            reason = "No Reason Specified"

        date = datetime.datetime.utcnow()
        utc_time = calendar.timegm(date.utctimetuple())
        user = await commands.converter.UserConverter().convert(interaction, user)
        embed = discord.Embed(
            title=f"*{user} was hack-banned!*", description=f"Reason: {reason} \n Member banned at <t:{utc_time}:F>"
        )

        await guild.ban(discord.Object(id=user.id))
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))