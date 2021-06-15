import discord, time
from discord import Embed
from discord.ext import commands
from discord.ext.commands import has_permissions

class botcommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

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
            description=f"Client latency: {round(self.bot.latency, 3)* 100}ms \nAPI Latency: {round((end_time - start_time), 3)* 100}ms", 
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
            await ctx.send("Missing required argument!")

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

def setup(bot):
    bot.add_cog(botcommands(bot))