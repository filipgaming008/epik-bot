# imports
import discord, time, asyncio
from discord import Embed
from discord.ext import commands, tasks


class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot

    @tasks.loop(seconds=1, count=5)
    async def printer(self):
        print(self.index)
        self.index += 1

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()

    @commands.command()
    async def startall(self, ctx):
        self.printer.start()

    @commands.command()
    async def stopall(self, ctx):
        self.printer.cancel()


    # # Message sending on an interval

    # async def printingmessage(self):
    #     channel = self.bot.get_channel(993132302035062856)
    #     await channel.send("Hello there!")

    #     await asyncio.sleep(seconds=20)
    
    # @commands.command(pass_context=True)
    # async def stopprintingmessage(self, ctx):
    #     self.task.cancel()

    # @commands.command(pass_context=True)
    # async def startprintingmessage(self, ctx):
    #     self.task.start()



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
