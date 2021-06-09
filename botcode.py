# imported stuff from discord, very useful for bot to work
import discord, os, json
from discord import Embed
from discord.ext import commands
from discord.ext.commands import has_permissions
from webserver import keep_alive

# this took 3 hours to do
bruh = discord.Intents.default()
bruh.members=True

# json

with open("config.json", "r") as f:
    data=json.load(f)

pref=data["settings"]["prefix"]

# this took 3 hours to do
client=commands.Bot(
    command_prefix=pref,
    intents=bruh,
    help_command=None
    )

# commands

# prefix change command
@client.command()
@has_permissions(administrator=True)
async def prefix(ctx, e):
    with open("config.json", "r") as f:
        brej=json.load(f)
    brej["settings"]["prefix"]=e
    with open("config.json", "w") as f:
        json.dump(brej, f)
    await ctx.send(f"Prefix has been changed to {e}")
    client.command_prefix=e

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

# loads all Cogs on start
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
            f"{pref}help - brings up this menu" 
            f"\n{pref}ping - pings the bot" 
            f"\n{pref}hello - say hi to the bot" 
            f"\n{pref}say - make the bot say something" 
            f"\n{pref}purge - purge a said amount of messages"
            f"\n{pref}load - load a said cog"
            f"\n{pref}unload - unload a said cog"
            f"\n{pref}checkcogs all - check to see what cogs are loaded or unloaded"
            f"\n{pref}checkcogs (cog name goes here) - to specify what cog you want to check"
            ),
        inline=False
        )
    await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv("TOKEN"))
