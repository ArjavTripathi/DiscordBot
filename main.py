import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv('guild')))

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.presences = True
        intents.members = True
        
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded: {filename}')

        synced = await self.tree.sync(guild=GUILD_ID)
        print(f"Synced {len(synced)} commands")
        print()
        print("Commands synced:")
        for i in synced:
            print(i)
        print()

    async def on_ready(self):
        activity = discord.Activity(
            type=discord.ActivityType.playing, 
            name="Faz League", 
            state="Locked In"
        )
        await self.change_presence(activity=activity, status=discord.Status.online)
        print(f'Logged in as {self.user}')

    async def on_member_join(self, member):
        channel = self.get_channel(1498809319368691885)
        if channel:
            embed = discord.Embed(
                title="New Member!",
                description=f"{member.mention} has joined the server!",
                color=0x232424
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_image(url="https://i.imgur.com/pHarayJ.png")
            await channel.send(embed=embed)


async def run_bot():
    token = os.getenv('token')
    bot = MyBot()
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(run_bot())
