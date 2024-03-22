from nextcord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def code(self,ctx,*,args:str):
        try:
            Code = args
            await ctx.message.delete()
            await ctx.send(f"```\n{Code}\n```")
            await ctx.channel.send(f'Author: <@{ctx.author.id}>')    

        except Exception:
            return 
    
    @commands.command()
    async def py(self,ctx,*,args:str):
        try:
            Code = args
            await ctx.message.delete()
            await ctx.send(f"```py\n{Code}\n```")
            await ctx.channel.send(f'Author: <@{ctx.author.id}>')    

        except Exception:
            return False
        
    @commands.command()
    async def js(self,ctx,*,args:str):
        try:
            Code = args
            await ctx.message.delete()
            await ctx.send(f"```js\n{Code}\n```")  
            await ctx.channel.send(f'Author: <@{ctx.author.id}>')  

        except Exception:
            return False
        
    @commands.command()
    async def say(self,ctx,*,args:str):
        Store = args
        await ctx.message.delete()
        await ctx.send(f"**{Store}**")

    @commands.command()
    async def python(self , ctx):
        ctx.send("Under dev!")

def setup(bot):
    bot.add_cog(Basic(bot))