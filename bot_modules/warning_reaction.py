# imports
import discord, time
from discord import Embed
from discord.ext import commands


class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message sending




def setup(bot):
    bot.add_cog(warning_reaction(bot))
