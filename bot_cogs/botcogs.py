import discord, os, sys, time
from discord import Embed, Status, Game, member
from discord.ext import commands

class botcogs(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Im ready!")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong!")


def setup(client):
    client.add_cog(botcogs(client))