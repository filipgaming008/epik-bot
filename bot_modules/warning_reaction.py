# imports
import discord, time, asyncio
from discord import Embed
from discord.ext import commands, tasks


class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.task = self.bot.loop.create_task(self.printingmessage())


    # Message sending on an interval

    async def printingmessage(self):
        channel = self.bot.get_channel(848878286914322435)
        await channel.send("Hello there!")

        await asyncio.sleep(20)
    
    @commands.command(pass_context=True)
    async def stopprintingmessage(self, ctx):
        self.task.cancel()

    @commands.command(pass_context=True)
    async def startprintingmessage(self, ctx):
        self.task.start()



    # # Getting member ID's on on_ready

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     Memberlist = []
    #     Memberlist.clear()
    #     guild = self.bot.get_guild(845624418650161172)
    #     print("Im on it!")
    #     for Member in guild.members:
    #         if Member.id == 848878975824035851:
    #             pass
    #         else:
    #             Memberlist.append(Member.id)
            
    #     print(Memberlist)



def setup(bot):
    bot.add_cog(warning_reaction(bot))
