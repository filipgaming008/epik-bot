# imports
import discord, time
from discord import Embed
from discord.ext import commands


class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Getting member ID's on on_ready

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(845624418650161172)
        print("Im on it!")
        for Member in guild.members:
            print(Member.id)



def setup(bot):
    bot.add_cog(warning_reaction(bot))
