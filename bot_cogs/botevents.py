import discord, json
from discord import Embed, Status, Game
from discord.ext import commands

class botevents(commands.Cog):
    def __init__(self, client):
        self.client=client

    # on ready event
    @commands.Cog.listener()
    async def on_ready(self):
        with open("config.json", "r") as f:
            brre=json.load(f)
        ea=brre["settings"]["prefix"]
        await self.client.change_presence(
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
            if str(channel)=="welcome":
                embed=Embed(color=0xff0000)
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
            if str(channel)=="welcome":
                embed=Embed(color=0xff0000)
                embed.add_field(
                    name="Good bye!",
                    value=f"{member.mention} has left the server!",
                    inline=False
                    )
                embed.set_image(url=member.avatar_url)
                await channel.send(embed=embed)

def setup(client):
    client.add_cog(botevents(client))