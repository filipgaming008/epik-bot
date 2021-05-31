#imported stuff from discord, very useful for bot to work
import discord, os
from discord.ext import commands

#this took 3 hours to do
bruh = discord.Intents.default()
bruh.members = True

#and so did this
client = commands.Bot(command_prefix = "!", intents = bruh)

#events
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

#commands
@client.command()
async def hello(cfx):
  print("hi")
  await cfx.message.channel.send("Hello!")

client.run(os.getenv("TOKEN"))
