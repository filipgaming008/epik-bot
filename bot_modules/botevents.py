# imports
import json, discord
from discord import Embed, Status, Game
from discord.ext import commands



class botevents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    # on ready event
    @commands.Cog.listener()
    async def on_ready(self):
        with open("./bot_json_files/config.json", "r") as f:
            brre = json.load(f)
        ea = brre["settings"]["prefix"]
        await self.bot.change_presence(
            status=Status.online,
            activity=Game(
                f"{ea}help"
            )
        )

        print("Im ready!")


    # ISD code
    @commands.Cog.listener()
    async def on_message(self, message):

        channel = message.channel
        user = message.author.id

        if channel == "986325938247716904" or "848878286914322435":
            if message == "***":
                await user.add_roles("986327355838570586")
                await user.remove_roles("986326065049899039")
                print("Roles added.")


"""
    # join event
    @commands.Cog.listener()
    async def on_member_join(self, member):
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
    @commands.Cog.listener()
    async def on_member_remove(self, member):
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
"""


def setup(bot):
    bot.add_cog(botevents(bot))
