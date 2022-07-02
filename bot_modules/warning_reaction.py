# imports
import discord, time
from discord import Embed
from discord.ext import commands


class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message sending

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.get_guild(863725674065952789)
        print("Im on it!")
        for member in guild.members:
            print (guild.members)





def setup(bot):
    bot.add_cog(warning_reaction(bot))
