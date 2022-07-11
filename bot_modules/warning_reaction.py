# imports
import discord, asyncio
from discord.ext import commands, tasks


reactions_channel_id_for_grp = 993132302035062856
logs_channel_id = 993189664213172225
time_between_activity_checks_for_grp = 6  # hours
waiting_time_for_reactions_for_grp = 21168  # seconds
waiting_time_for_warning_for_grp = 300 # seconds

reactions_channel_id_for_atlas = 996093056094838905
time_between_activity_checks_for_atlas = 2 # hours
waiting_time_for_reactions_for_atlas = 6768 # seconds
waiting_time_for_warning_for_atlas = 300 # seconds

class warning_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # GRP Message

    # Message send on interval

    @tasks.loop(hours=time_between_activity_checks_for_grp)
    async def printer(self):
        reactions_channel = self.bot.get_channel(reactions_channel_id_for_grp)

        embed = discord.Embed(
            title="Advertisment check for GRP!",
            description="React with :white_check_mark:",
            color=0xff0000
        )

        message_sent = await reactions_channel.send("@everyone")
        message_sent = await reactions_channel.send(embed=embed)
        await message_sent.add_reaction(u"\U00002705")
        

        await asyncio.sleep(waiting_time_for_warning_for_grp)

        # warning on no users reacted

        last_message = await reactions_channel.fetch_message(message_sent.id)

        users_reacted = await last_message.reactions[0].users().flatten()

        for user in users_reacted:
            if user.bot:
                users_reacted.remove(user)

        user_ids_reacted = list(map(lambda x: x.id, users_reacted))

        if len(user_ids_reacted) == 0:
            await reactions_channel.send("React to the advertisment check! @everyone")
        else:
            pass

        await asyncio.sleep(waiting_time_for_reactions_for_grp)

        member_list = []
        member_list.clear()
        guild = reactions_channel.guild
        for member in guild.members:
            if member.bot:
                pass
            else:
                member_list.append(member.id)


        users_reacted = await last_message.reactions[0].users().flatten()

        for user in users_reacted:
            if user.bot:
                users_reacted.remove(user)

        user_ids_reacted = list(map(lambda x: x.id, users_reacted))

        user_ids_not_reacted = list(set(member_list) - set(user_ids_reacted))


        logs_channel = self.bot.get_channel(logs_channel_id)

        embed = discord.Embed(
            title="Advertisment check results for GRP",
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
    


    # Atlas message

    # Message send on interval

    @tasks.loop(hours=time_between_activity_checks_for_atlas)
    async def printer2(self):
        reactions_channel = self.bot.get_channel(reactions_channel_id_for_atlas)

        embed = discord.Embed(
            title="Advertisment check for Atlas!",
            description="React with :white_check_mark:",
            color=0xff0000
        )

        message_sent = await reactions_channel.send("@everyone")
        message_sent = await reactions_channel.send(embed=embed)
        await message_sent.add_reaction(u"\U00002705")
        

        await asyncio.sleep(waiting_time_for_warning_for_atlas)

        # warning on no users reacted

        last_message = await reactions_channel.fetch_message(message_sent.id)

        users_reacted = await last_message.reactions[0].users().flatten()

        for user in users_reacted:
            if user.bot:
                users_reacted.remove(user)

        user_ids_reacted = list(map(lambda x: x.id, users_reacted))

        if len(user_ids_reacted) == 0:
            await reactions_channel.send("React to the advertisment check! @everyone")
        else:
            pass

        await asyncio.sleep(waiting_time_for_reactions_for_atlas)

        member_list = []
        member_list.clear()
        guild = reactions_channel.guild
        for member in guild.members:
            if member.bot:
                pass
            else:
                member_list.append(member.id)


        users_reacted = await last_message.reactions[0].users().flatten()

        for user in users_reacted:
            if user.bot:
                users_reacted.remove(user)

        user_ids_reacted = list(map(lambda x: x.id, users_reacted))

        user_ids_not_reacted = list(set(member_list) - set(user_ids_reacted))


        logs_channel = self.bot.get_channel(logs_channel_id)

        embed = discord.Embed(
            title="Advertisment check results for Atlas!",
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

    @printer2.before_loop
    async def before_printer2(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def startall(self, ctx):
        self.printer.start()
        self.printer2.start()

    @commands.command()
    async def stopall(self, ctx):
        self.printer.cancel()
        self.printer2.cancel()




def setup(bot):
    bot.add_cog(warning_reaction(bot))
