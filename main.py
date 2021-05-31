#imported stuff from discord, very useful for bot to work
import discord, os
from discord import message
from discord.ext import commands

#this took 3 hours to do
bruh = discord.Intents.default()
bruh.members = True

#and so did this
client = commands.Bot(
  command_prefix = "!",
  intents = bruh,
  help_command=None
  )

#events
@client.event
async def on_ready():
    print("Im ready!")

@client.event
async def on_member_join(member):
  print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
  print(f"{member} has left a server.")

#commands
@client.command()
async def hello(ctx):
  await ctx.send("Hello!")

@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency, 3)* 100}ms")

@client.command()
async def help(ctx):
  await ctx.send("\nAvalable commands: \n!help \n!ping \n!hello \n")

client.run(os.getenv("TOKEN"))
