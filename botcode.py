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

# check cogs command
@client.command()
async def checkcogs(ctx, cog_name):
    if cog_name=="all":
        for filename in os.listdir("./bot_cogs"):
            if filename.endswith(".py"):
                try:
                    client.load_extension(f"bot_cogs.{filename[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    await ctx.send(f"Cog '{filename[:-3]}' is loaded!")
                except commands.ExtensionNotFound:
                    await ctx.send(f"Cog '{filename[:-3]}' not found!")
                else:
                    await ctx.send(f"Cog '{filename[:-3]}' is unloaded!")
                    client.unload_extension(f"bot_cogs.{filename[:-3]}")

    else:
        try:
            client.load_extension(f"bot_cogs.{cog_name}")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send("Cog is loaded!")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found!")
        else:
            await ctx.send("Cog is unloaded!")
            client.unload_extension(f"bot_cogs.{cog_name}")

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

# help command
@client.command()
async def help(ctx):
    embed=Embed(
        title="\nAvailable commands:\n",
        description="",
        color=0xff0000
        )
    embed.add_field(
        name="\nBasic commands:\n",
        value=(
            "!help - brings up this menu" 
            "\n!ping - pings the bot" 
            "\n!hello - say hi to the bot" 
            "\n!say - make the bot say something" 
            "\n!purge - purge a said amount of messages"
            "\n!load - load a said cog"
            "\n!unload - unload a said cog"
            "\n!checkcogs all - check to see what cogs are loaded or unloaded"
            "\n!checkcogs (cog name goes here) - to specify what cog you want to check"
            ),
        inline=False
        )
    await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv("TOKEN"))
