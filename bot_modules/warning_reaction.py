# imports
import discord, asyncio
from discord.ext import commands, tasks


reactions_channel_id = 993132302035062856
logs_channel_id = 993189664213172225
time_between_activity_checks = 30  # seconds
waiting_time_for_reactions = 20  # seconds

class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message send on interval

    @tasks.loop(seconds=time_between_activity_checks)
    async def printer(self):
        reactions_channel = self.bot.get_channel(reactions_channel_id)

        embed = discord.Embed(
            title="Activity check!",
            description="React with :white_check_mark:"
            color=0xff0000
        )

        message_sent = await reactions_channel.send(embed=embed)
        await message_sent.add_reaction(u"\U00002705")
        

        await asyncio.sleep(waiting_time_for_reactions)

        member_list = []
        member_list.clear()
        guild = reactions_channel.guild
        for member in guild.members:
            if member.bot:
                pass
            else:
                member_list.append(member.id)

        last_message = await reactions_channel.fetch_message(message_sent.id)


        users_reacted = await last_message.reactions[0].users().flatten()

        for user in users_reacted:
            if user.bot:
                users_reacted.remove(user)

        user_ids_reacted = list(map(lambda x: x.id, users_reacted))

        user_ids_not_reacted = list(set(member_list) - set(user_ids_reacted))


        logs_channel = self.bot.get_channel(logs_channel_id)

        embed = discord.Embed(
            title="Activity check results",
            description="",
            color=0xff0000
        )
        results_reacted_list = []
        for user_id in user_ids_reacted:
            results_reacted_list.append(u"\U00002022"+f"<@{user_id}>")
        embed.add_field(
            name="List of users that have reacted:",
            value=("\n".join(results_reacted_list) if results_reacted_list else "No users reacted!")
        )
        results_not_reacted_list = []
        for user_id in user_ids_not_reacted:
            results_not_reacted_list.append(u"\U00002022"+f"<@{user_id}>")
        embed.add_field(
            name="List of users that have not reacted:",
            value=("\n".join(results_not_reacted_list) if results_not_reacted_list else "No users did not react!")
        )

        await logs_channel.send(embed=embed)
    

    @printer.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def startall(self, ctx):
        self.printer.start()

    @commands.command()
    async def stopall(self, ctx):
        self.printer.cancel()



def setup(bot):
    bot.add_cog(warning_reaction(bot))
