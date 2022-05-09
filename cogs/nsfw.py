import datetime
import aiohttp
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import os
import random
import pathlib
from typing import Optional



class nsfw(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    async def is_nsfw(interaction: discord.Interaction) -> bool:
        if interaction.channel.is_nsfw():
            return True
        await interaction.response.send_message("🔞 You cannot use this command outside a nsfw channel!", ephemeral=True)
        return False
    
    
    @app_commands.command(description="Show NSFW neko pics! ")
    @app_commands.check(is_nsfw)
    @app_commands.choices(feature=[
        Choice(name="neko", value="neko"),
        Choice(name="waifu", value="waifu"),
        Choice(name="trap", value="trap"),
        Choice(name="blowjob", value="blowjob")
    ])
    async def neko(self, interaction: discord.Interaction, feature:Choice[str]):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.waifu.pics/nsfw/{feature.name}") as request:
                print(request.url)

                data = await request.json()
                print(data['url'])
                embed = discord.Embed(description=f"**[Image Link]({data['url']})**", color=0xc98cbf)
                embed.set_image(url=data['url'])       
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
                embed.set_footer(text="Powered by waifu.pics")
                print(interaction.user.display_avatar.url)
                return await interaction.response.send_message(embed=embed)   

    
    @neko.error
    async def nsfwerror(self,interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.CheckFailure):
            pass

    @app_commands.command(description="Get Some Helltaker Porn")
    @app_commands.check(is_nsfw)
    async def helltaker(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://thino.pics/api/v1/helltaker") as request:
                data = await request.json()
                print(data['url'])
                embed = discord.Embed(description=f"**[Raw Image Link]({data['url']})**", color=0xc98cbf )
                embed.set_image(url=data['url'])
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
                embed.set_footer(text="Powered by thino.pics!")
                await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Sends femboy porn")
    @app_commands.check(is_nsfw)
    async def femboy(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://thino.pics/api/v1/femboy") as request:
                data = await request.json()
                print(data['url'])
                embed = discord.Embed(description=f"**[Raw Image Link]({data['url']})**", color=0xc98cbf )
                embed.set_image(url=data['url'])
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
                embed.set_footer(text="Powered by thino.pics!")
                await interaction.response.send_message(embed=embed)
        
    @app_commands.command(description="Shows hentai")
    @app_commands.check(is_nsfw)
    async def hentai(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://thino.pics/api/v1/hentai") as request:
                data = await request.json()
                print(data['url'])
                embed = discord.Embed(description=f"**[Raw Image Link]({data['url']})**", color=0xc98cbf )
                embed.set_image(url=data['url'])
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
                embed.set_footer(text="Powered by thino.pics!")
                await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Shows hot af tomboy porn")
    @app_commands.check(is_nsfw)
    async def tomboy(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://thino.pics/api/v1/tomboy") as request:
                data = await request.json()
                print(data['url'])
            
                embed = discord.Embed(description=f"Found File: [{data['filename']}]({data['url']}) on endpoint: [tomboy](https://thino.pics/api/v1/tomboy)", color=0xc98cbf )
                embed.set_image(url=data['url'])
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
                embed.set_footer(text="Powered by thino.pics!")
                await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Shows hot af thighs porn")
    @app_commands.check(is_nsfw)
    async def thighs(self, interaction: discord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://thino.pics/api/v1/thighs") as request:
                data = await request.json()
                print(data['url'])
            
                embed = discord.Embed(description=f"Found File: [{data['filename']}]({data['url']}) on endpoint: [thighs](https://thino.pics/api/v1/thighs)", color=0xc98cbf )
                embed.set_image(url=data['url'])
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
                embed.set_footer(text="Powered by thino.pics!")
                await interaction.response.send_message(embed=embed)

    @app_commands.command(description=f"Search for an image from the thino.pics API")
    @app_commands.check(is_nsfw)
    async def search(self, interaction:discord.Interaction, image: str):
        dir = "/root/yanpdb/nsfw_cdn/"
        p = pathlib.Path(dir)
        
        for f in p.rglob(image):
            print(str(f.parent))

        finished_url = f"https://i.thino.pics/{str(image)}"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://i.thino.pics/search/{image}") as request:
                data = await request.json()
                url = data['url']
                
                if url == "https://thino.pics/api/v1/hentai":
                    url_endpoint = "hentai"
                
                if url == "https://thino.pics/api/v1/helltaker":
                    url_endpoint = "Helltaker"

                if url == "https://thino.pics/api/v1/neko":
                    url_endpoint = "neko"

                if url == "https://thino.pics/api/v1/tomboy":
                    url_endpoint = "tomboy"
                
                if url == "https://thino.pics/api/v1/femboy":
                    url_endpoint = "femboy"
        
        print(url_endpoint)
        print(url)
        print(finished_url)
        embed = discord.Embed(description=f"Found the file name: [{image}]({finished_url}) at the endpoint: [{url_endpoint}]({url})", timestamp=datetime.datetime.utcnow())
        embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
        embed.set_image(url=finished_url)
        embed.set_footer(text="Powered by thino.pics!")

        await interaction.response.send_message(embed=embed)



async def setup(bot: commands.Bot):
    await bot.add_cog(nsfw(bot))