import calendar
import datetime
import traceback
import discord
from discord.ext import commands
from discord import app_commands    
from discord.app_commands import Choice

class Feedback(discord.ui.Modal, title='Feedback'):
    # Our modal classes MUST subclass `discord.ui.Modal`,
    # but the title can be whatever you want.

    # This will be a short input, where the user can enter their name
    # It will also have a placeholder, as denoted by the `placeholder` kwarg.
    # By default, it is required and is a short-style input which is exactly
    # what we want.
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Your name here...',
    )

    # This is a longer, paragraph style input, where user can submit feedback
    # Unlike the name, it is not required. If filled out, however, it will
    # only accept a maximum of 300 characters, as denoted by the
    # `max_length=300` kwarg.
    feedback = discord.ui.TextInput(
        label='What do you think of this new feature?',
        style=discord.TextStyle.long,
        placeholder='Type your feedback here...',
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(913562181474336839)
        await channel.send(f'Feedback recieved: {self.feedback.value}!')
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}', ephemeral=True)

    async def on_error(self, error: Exception, interaction: discord.Interaction) -> None:
        pass
class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        for item in self.children:
            item.disabled = True
        await interaction.response.send_modal(Feedback())
        Feedback().wait()
        await interaction.edit_original_message(view=self)
        
    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True

        # you also only disable this buttons by setting button.disabled
        await interaction.response.edit_message(view=self)



class testing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def testing1(self, ctx:commands.Context):
        await ctx.send('Do you want to continue?', view=Confirm())

async def setup(bot: commands.Bot):
    await bot.add_cog(testing(bot))