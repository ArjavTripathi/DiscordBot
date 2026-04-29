import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    # This is a slash command
    @app_commands.command(name="rules", description="Send the embed that contains rules")
    @app_commands.checks.has_role("Early Supporter")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! {latency}ms")

    @app_commands.command(name="embed_test", description="Show off a custom color embed")
    async def embed_test(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Custom Setup Active",
            description="Slash commands + Cogs are working!",
            color=0x2ECC71 # Emerald Green
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))