# imports
import discord, json
from discord.ext import commands
from discord.ext.commands import has_permissions



class admincommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        


    # say command
    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")



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
    bot.add_cog(admincommands(bot))