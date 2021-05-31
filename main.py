import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

import os

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Im ready!")

@client.event
async def on_message(message):
    print("A message has been sent!")

@client.event
async def on_member_join(member):
  print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
  print(f"{member} has left a server.")

client.run(os.getenv("TOKEN"))
