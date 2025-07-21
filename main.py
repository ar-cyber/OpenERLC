# Discord imports
import discord
from discord.ext import commands

# Utils
from utils.conf import *


intents = discord.Intents.none() # The goal is to only use the required intents; message content is not required as of right now.

client = commands.Bot(command_prefix="oe!", intents = intents)

@client.event
async def on_ready():
    for cog in main['features']:
        if cog['name'] == "core":
            pass
        else:
            cogname = f"cogs.{cog['name']}"
            client.load_extension(cogname)

    print("=======================================")
    print()
    print("Login information:")
    print(f"Username: {client.user.name}")
    print(f"User ID: ")
