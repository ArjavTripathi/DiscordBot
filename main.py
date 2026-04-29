import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, 
            name="Faz League",
            state="Locked In",
            
        ),
        status=discord.Status.online
    )

    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = client.get_channel(1498809319368691885)

    embed = discord.Embed(
        title="New Member!",
        description=f"{member.mention} has joined the server!",
        color = discord.Colour.teal()
    )
    embed.set_thumbnail(url=member.display_avatar.url)

    await channel.send(embed=embed)

token = os.getenv('token')
client.run(token)