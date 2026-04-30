import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name="rules", description="Send the embed that contains rules")
    @app_commands.checks.has_role("Early Supporter")
    async def ping(self, interaction: discord.Interaction):

        rules = """Jokes are fine as long as they aren’t personal and the recipient is alright with the banter. \n Blatant homophobia, transphobia, racism, misogyny, sexual harassment, etc. towards another member are prohibited. \n 
            Keep serious drama and or beef out of the server. If you have a problem with someone then either keep it in the DMs or message a moderator. \n
            NO NSFW AT ALL. \n  Treat others how you want to be treated. This is a community, Please respect one another and be reasonable. \n
            No Self Promotion of any kind"""
        
        embed = discord.Embed(
            title="Faz League Rules",
            description=rules,
            color=0x232424
        )
        embed.set_image(url="https://i.imgur.com/pHarayJ.png")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="embed_test", description="Show off a custom color embed")
    async def embed_test(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Custom Setup Active",
            description="Slash commands + Cogs are working!",
            color=0x2ECC71 
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))