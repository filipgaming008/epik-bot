# imported stuff from discord, very useful for bot to work
import discord, os, json
from discord import Embed, Status, Game
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
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def prefix_change(ctx, e):
    with open("config.json", "r") as f:
        brej=json.load(f)
    
    brej["settings"]["prefix"]=e

    with open("config.json", "w") as f:
        json.dump(brej, f)
    
    await ctx.send(f"Prefix has been changed to {e}")
    client.command_prefix=e

    await client.change_presence(
            status=Status.online, 
            activity=Game(
                f"{e}help"
                )
            )

# prefix change command error handle
@prefix_change.error
async def prefix_change_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

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
    await ctx.send(f"{extension} has been loaded!")

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
    await ctx.send(f"{extension} has been unloaded!")

# unload bot_cogs error handle
@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

# load all Cogs on start command
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def loadcogs(ctx, a):
    with open("config.json", "r") as f:
        aa=json.load(f)
    aa["settings"]["cogs settings"]["loadall"]=a
    if a=="True":
        await ctx.send("Will load all cogs on restart!")
        with open("config.json", "w") as f:
            json.dump(aa, f)
    elif a=="False":
        await ctx.send("Will not load all cogs on restart!")
        with open("config.json", "w") as f:
            json.dump(aa, f)
    else:
        await ctx.send("You can only enter 'True' or 'False'!")

@loadcogs.error
async def loadcogs_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.event
async def on_ready():
    with open("config.json", "r") as f:
        eee=json.load(f)
        ee=eee["settings"]["cogs settings"]["loadall"]
        if ee=="True":
            for filename in os.listdir("./bot_cogs"):
                if filename.endswith(".py"):
                    client.load_extension(f"bot_cogs.{filename[:-3]}")

# help command
@client.command()
async def help(ctx):
    with open("config.json", "r") as f:
        bean=json.load(f)
    broj=bean["settings"]["prefix"]
    embed=Embed(
        title="\nAvailable commands:\n",
        description="",
        color=0xff0000
        )
    embed.add_field(
        name="\nBasic commands:\n",
        value=(
            f"{broj}help - brings up this menu" 
            f"\n{broj}ping - pings the bot" 
            f"\n{broj}hello - say hi to the bot" 
            f"\n{broj}say - make the bot say something" 
            f"\n{broj}purge - purge a said amount of messages"
            f"\n{broj}load - load a said cog"
            f"\n{broj}unload - unload a said cog"
            f"\n{broj}checkcogs all - check to see what cogs are loaded or unloaded"
            f"\n{broj}checkcogs (cog name goes here) - to specify what cog you want to check"
            ),
        inline=False
        )
    await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv("TOKEN"))
