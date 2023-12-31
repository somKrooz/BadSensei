from nextcord.ext import commands

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="clean")
    @commands.is_owner()
    async def clean(self, ctx, amount: int):
        try:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"Purged {amount} messages")
        except Exception:
            await ctx.send(f"Only Owners Can Perform This Action")

def setup(bot):
    bot.add_cog(Dev(bot))

