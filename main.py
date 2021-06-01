# imported stuff from discord, very useful for bot to work
import discord
import os
from discord import Embed, Status, Game
from discord.ext import commands
from discord.ext.commands import has_permissions
from webserver import keep_alive

# this took 3 hours to do
bruh = discord.Intents.default()
bruh.members = True

# and so did this
client = commands.Bot(
    command_prefix="!",
    intents=bruh,
    help_command=None
    )

# events

# on ready event
@client.event
async def on_ready():
    await client.change_presence(
        status=Status.online, 
        activity=Game(
            "!help"
            )
        )

    print("Im ready!")

# join event
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(color=0xff0000)
            embed.add_field(
                name="Welcome!",
                value=f"{member.mention} has joined the server!",
                inline=False
                )
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

# leave event
@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            embed = Embed(color=0xff0000)
            embed.add_field(
                name="Good bye!",
                value=f"{member.mention} has left the server!",
                inline=False
                )
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

# commands

# hello command
@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

# ping command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency, 3)* 100}ms")

# say command
@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

@client.command()
async def haram(ctx):
    await ctx.send("yes")

@client.command()
async def restart(ctx):
    await ctx.send("Restarting!")
    sys.exit()

# purge command
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def purge(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} messages have been deleted successfully!")

# purge error handle
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

# help command
@client.command()
async def help(ctx):
    embed = Embed(
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
            ),
        inline=False
        )
    await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv("TOKEN"))
