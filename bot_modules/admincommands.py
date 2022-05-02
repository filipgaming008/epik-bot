# imports
import discord, json
from discord.ext import commands
from discord.ext.commands import has_permissions



class admincommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    bot.warnings = {}


    # say command
    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")



    # purge command
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def purge(self, ctx, amount=0):
        if amount != 0:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"{amount} messages have been deleted successfully!")
        else:
            await ctx.send("Invalid amount!")

    # purge error handle
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")



    # warn command
    @commands.command(pass_context=True)
    @has_permissions(administartor=True)
    async def warn(self, ctx, member: discord.Member=None, *, reason=None):
        if member is None:
            return await ctx.send("The given member could not be found or has not been provided!")

        if reason is None:
            return await ctx.send("Please provide a reason for the given member!")

        try:
            first_warning = False
            bot.warnings[ctx.guild.id][member.id][0] += 1
            bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

        except KeyError:
            first_warning = True
            bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

        count = bot.warnings[ctx.guild.id][member.id][0]

        async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
            await file.write(f"{member.id} {ctx.author.id} {reason}\n")

        await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

    # warnings command
    @commands.command(pass_context=True)
    @has_permissions(administartor=True)
    async def warn(self, ctx, member: discord.Member=None, *, reason=None):
        if member is None:
            return await ctx.send("The given member could not be found or has not been provided!")
        
        embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.colour.red())
        try:
            i = 1
            for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
                admin = ctx.guild.get_member(admin_id)
                embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
                i +=1

            await ctx.send(embed=embed)

        except KeyError:
            await ctx.send("This member has no warnings,")




def setup(bot):
    bot.add_cog(admincommands(bot))