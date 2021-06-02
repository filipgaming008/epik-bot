import discord, os, sys, time
from discord import Embed, Status, Game, member
from discord.ext import commands
from discord.ext.commands import has_permissions

class botcommands(commands.Cog):
    def __init__(self, client):
        self.client=client

    # hello command
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    # ping command
    @commands.command()
    async def ping(self, ctx):
        start_time=time.time()
        embed=Embed(
            title="Pinging the bot....", 
            description="", 
            color=0xff0000
            )
    
        message=await ctx.send(embed=embed)
        end_time=time.time()

        embed=Embed(
            title="Pong!", 
            description=f"Client latency: {round(self.client.latency, 3)* 100}ms \nAPI Latency: {round((end_time - start_time), 3)* 100}ms", 
            color=0xff0000
            )
    
        await message.edit(embed=embed)

    # say command
    @commands.command()
    async def say(self, ctx, *, text):
        message=ctx.message
        await message.delete()
        await ctx.send(f"{text}")

    # av command
    @commands.command()
    async def av(self, ctx, member: discord.Member):
        await ctx.send(member.avatar_url)

    # av error handle
    @av.error
    async def av_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You have to mention a member or their id!")

    # purge command
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def purge(self, ctx, amount=0):
        if amount != 0:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"{amount} messages have been deleted successfully!")
        else:
            await ctx.send("Invalid amount!")

    # purge error handle
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

    # help command
    @commands.command()
    async def help(self, ctx):
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
                ),
            inline=False
            )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(botcommands(client))