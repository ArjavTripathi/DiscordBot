import discord
from discord import app_commands
from discord.ext import commands
import config

class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="announce", description="Use this embed for announcements only")
    @app_commands.describe(msg="The text you want to announce")
    @app_commands.checks.has_role(config.ROLE)
    async def announce(self, interaction: discord.Interaction, msg: str):
        embed = discord.Embed(
        title="📢 Announcement",
        description=f"{msg} \n\n ||<@&1453086741794656387>||",
        color=0x5865F2,  
        timestamp=interaction.created_at
        )

        embed.set_author(
            name=interaction.user.display_name,
            icon_url=interaction.user.display_avatar.url
        )

        embed.set_thumbnail(url="https://i.imgur.com/MGSirwZ.png")

        embed.set_footer(
            text=f"{interaction.guild.name}",
            icon_url=interaction.guild.icon.url if interaction.guild.icon else None
        )

        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="miniannounce", description="Use this embed for small announcements only")
    @app_commands.describe(msg="The text you want to announce")
    @app_commands.checks.has_role(config.ROLE)
    async def miniannounce(self, interaction: discord.Interaction, msg:str):
        embed = discord.Embed(
            description=f"📢 **Announcement**\n\n{msg} \n\n ||<@&1453086741794656387>||",
            color=0x5865F2
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Embeds(bot))