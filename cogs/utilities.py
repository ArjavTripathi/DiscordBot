import discord
from discord import app_commands
from discord.ext import commands
import config

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rules", description="Send the embed that contains rules")
    @app_commands.checks.has_role(config.ROLE)
    async def ping(self, interaction: discord.Interaction):

        rules = (
            "\n"
            "1. Jokes are fine as long as they aren't personal and the recipient is alright with the banter.\n\n"
            "2. Blatant homophobia, transphobia, racism, misogyny, sexual harassment, etc. towards another member are prohibited.\n\n"
            "3. Keep serious drama and or beef out of the server. If you have a problem with someone then either keep it in the DMs or message a moderator.\n\n"
            "4. NO NSFW AT ALL.\n\n"
            "5. Treat others how you want to be treated. This is a community, Please respect one another and be reasonable.\n\n"
            "6. No Self Promotion of any kind without permission.\n\n"
            ""
        )

        
        embed = discord.Embed(
            title="Faz League Rules",
            description=rules,
            color=0x232424
        )
        embed.set_image(url="https://i.imgur.com/pHarayJ.png")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))