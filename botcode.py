# imported stuff from discord, very useful for bot to work
import discord, os, sys, time
from discord import Embed, Status, Game, member
from discord.ext import commands
from discord.ext.commands import has_permissions
from webserver import keep_alive

# this took 3 hours to do
bruh = discord.Intents.default()
bruh.members=True

# and so did this
client=commands.Bot(
    command_prefix="!",
    intents=bruh,
    help_command=None
    )

# commands

# load bot_cogs
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f"bot_cogs.{extension}")

# load bot_cogs error handle
@load.error
async def load_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

# unload bot_cogs
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"bot_cogs.{extension}")

# unload bot_cogs error handle
@unload.error
async def unload_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

# some code to check what files are there in bot_cogs
for filename in os.listdir("./bot_cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"bot_cogs.{filename[:-3]}")

keep_alive()
client.run(os.getenv("TOKEN"))
