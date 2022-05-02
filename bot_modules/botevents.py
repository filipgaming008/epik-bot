# imports
import json, discord, aiofiles
from discord import Embed, Status, Game
from discord.ext import commands



class botevents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    bot.warnings = {}


    # on ready event
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in bot.guilds:
            async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
                pass

            bot.warnings[guild.id] = {}

        for guild in bot.guilds:
            async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
                lines = await file.readlines()

                for line in lines:
                    data = line.split(" ")
                    member_id = int(data[0])
                    admin_id = int(data[0])
                    reason = " ".join(data[2:]).strip("\n")

                    try:
                        bot.warnings[guild.id][member_id][0] += 1
                        bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                    except KeyError:
                        bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]


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



def setup(bot):
    bot.add_cog(botevents(bot))
