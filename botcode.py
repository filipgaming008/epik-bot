# imports
import discord, os, json
from discord import Embed, Status, Game
from discord.ext import commands
from discord.ext.commands import has_permissions

bruh = discord.Intents.default()
bruh.members = True

# json
with open("./bot_json_files/config.json", "r") as f:
    data = json.load(f)

pref = data["settings"]["prefix"]

bot = commands.Bot(
    command_prefix=pref,
    intents=bruh,
    help_command=None
)



# commands

# prefix change command
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def prefix_change(ctx, e):
    with open("./bot_json_files/config.json", "r") as f:
        brej = json.load(f)

    brej["settings"]["prefix"] = e

    with open("./bot_json_files/config.json", "w") as f:
        json.dump(brej, f)

    await ctx.send(f"Prefix has been changed to {e}")
    bot.command_prefix = e

    await bot.change_presence(
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

@bot.command()
async def checkmodules(ctx, module_name):
    if module_name == "all":
        for filename in os.listdir("./bot_modules"):
            if filename.endswith(".py"):
                try:
                    bot.load_extension(f"bot_modules.{filename[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    await ctx.send(f"Module '{filename[:-3]}' is loaded!")
                except commands.ExtensionNotFound:
                    await ctx.send(f"Module '{filename[:-3]}' not found!")
                else:
                    await ctx.send(f"Module '{filename[:-3]}' is unloaded!")
                    bot.unload_extension(f"bot_modules.{filename[:-3]}")

    else:
        try:
            bot.load_extension(f"bot_cogs.{module_name}")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send("Module is loaded!")
        except commands.ExtensionNotFound:
            await ctx.send("Module not found!")
        else:
            await ctx.send("Module is unloaded!")
            bot.unload_extension(f"bot_modules.{module_name}")


@checkmodules.error
async def checkmodules_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument!")

# load bot_cogs
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f"bot_modules.{extension}")
    await ctx.send(f"{extension} has been loaded!")

# load bot_cogs error handle
@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

# unload bot_cogs
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f"bot_modules.{extension}")
    await ctx.send(f"{extension} has been unloaded!")

# unload bot_cogs error handle
@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


# load all Cogs on start command
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def loadmodules(ctx, a):
    with open("./bot_json_files/config.json", "r") as f:
        aa = json.load(f)
    aa["settings"]["module settings"]["loadall"] = a
    if a == "True":
        await ctx.send("Will load all modules on restart!")
        with open("./bot_json_files/config.json", "w") as f:
            json.dump(aa, f)
    elif a == "False":
        await ctx.send("Will not load all modules on restart!")
        with open("./bot_json_files/config.json", "w") as f:
            json.dump(aa, f)
    else:
        await ctx.send("Invalid argument! (Only True/False)")


@loadmodules.error
async def loadmodules_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

with open("./bot_json_files/config.json", "r") as f:
    eee = json.load(f)
    ee = eee["settings"]["module settings"]["loadall"]
    if ee == "True":
        for filename in os.listdir("./bot_modules"):
            if filename.endswith(".py"):
                bot.load_extension(f"bot_modules.{filename[:-3]}")


# help command
"""
@bot.command()
async def help(ctx):
    with open("./bot_json_files/config.json", "r") as f:
        bean = json.load(f)
    broj = bean["settings"]["prefix"]
    embed = Embed(
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
            f"\n{broj}av - avatar command"
        ),
        inline=False
    )
    embed.add_field(
        name="\nAdmin commands\n",
        value=(
            f"{broj}say - make the bot say something"
            f"\n{broj}purge - purge a said amount of messages"
            f"\n{broj}load - load a said module"
            f"\n{broj}unload - unload a said module"
            f"\n{broj}checkmodules all - check to see what modules are loaded or unloaded"
            f"\n{broj}checkmodules (cog name goes here) - to specify what module you want to check"
            f"\n{broj}loadmodules (True/False) - set if u want bot to load all modules on restart or not"
        ),
        inline=False
    )
    await ctx.send(embed=embed)
"""


with open("./bot_json_files/token.json", "r") as f:
    acde = json.load(f)
    token = acde["token"]

bot.run(token)
