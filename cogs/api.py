from nextcord.ext import commands
import random 
import requests

class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self,ctx):
            await ctx.message.delete()
            tags = ["baka", "bite", "blush", "bored", "cry", "cuddle", "dance", "facepalm", "feed", "handhold", "handshake", "happy", "highfive", "hug", "kick","kiss", "laugh", "lurk", "nod", "nom", "nope", "pat", "peck", "poke", "pout", "punch", "shoot", "shrug", "slap", "sleep", "smile", "smug", "stare", "think", "thumbsup", "tickle", "wave", "wink", "yawn", "yeet"]

            tag = random.choice(tags)
            url = f"https://nekos.best/api/v2/{tag}"
            res = requests.get(url)
            await ctx.send(res.json()["results"][0]['url'])
            await ctx.channel.send(f'{tag} From: <@{ctx.author.id}>') 

    @commands.command()
    async def gv(self,ctx,*,args:str):
        await ctx.message.delete()
        url = f"https://nekos.best/api/v2/{str(args)}"
        res = requests.get(url)
        await ctx.send(res.json()["results"][0]['url'])
        await ctx.channel.send(f'{str(args)} From: <@{ctx.author.id}>') 

    @commands.command()
    async def neko(self , ctx):
        await ctx.message.delete()
        url = f"https://nekos.best/api/v2/neko"
        res = requests.get(url)
        await ctx.send(res.json()["results"][0]['url'])
        await ctx.channel.send(f'<@{ctx.author.id}>')
         
    @commands.command()
    async def waifu(self , ctx):
        await ctx.message.delete()
        url = f"https://nekos.best/api/v2/waifu"
        res = requests.get(url)
        await ctx.send(res.json()["results"][0]['url'])
        await ctx.channel.send(f'<@{ctx.author.id}>')

    @commands.command()
    async def gvHelp(self,ctx):
        tags = ["baka", "bite", "blush", "bored", "cry", "cuddle", "dance", "facepalm", "feed", "handhold", "handshake", "happy", "highfive", "hug", "kick","kiss", "laugh", "lurk", "nod", "nom", "nope", "pat", "peck", "poke", "pout", "punch", "shoot", "shrug", "slap", "sleep", "smile", "smug", "stare", "think", "thumbsup", "tickle", "wave", "wink", "yawn", "yeet"]

        await ctx.send("Try These Commands.....")
        await ctx.send(str(tags))
         


def setup(bot):
    bot.add_cog(API(bot)) 