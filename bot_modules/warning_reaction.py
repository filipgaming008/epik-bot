# imports
import discord, time
from discord import Embed
from discord.ext import commands, tasks


class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.printingmessage.start()



    # Message sending on an interval

    @tasks.loop(seconds=20)
    async def printingmessage(self):
        channel = self.bot.get_channel(848878286914322435)
        await channel.send("Hello there!")

    @printingmessage.before_loop
    async def before_printingmessage(self):
        print("Waiting.....")
        await self.bot.wait_until_ready()


    # Start, stop and cancel

    @commands.command
    async def startmessaging(self):
        self.printingmessage.start()

    @commands.command
    async def stopmessaging(self):
        self.printingmessage.stop()

    @commands.command
    async def cancelmessaging(self):
        self.printingmessage.cancel()

    # Getting member ID's on on_ready

    @commands.Cog.listener()
    async def on_ready(self):
        Memberlist = []
        Memberlist.clear()
        guild = self.bot.get_guild(845624418650161172)
        print("Im on it!")
        for Member in guild.members:
            if Member.id == 848878975824035851:
                pass
            else:
                Memberlist.append(Member.id)
            
        print(Memberlist)


def setup(bot):
    bot.add_cog(warning_reaction(bot))
