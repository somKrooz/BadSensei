import nextcord
from nextcord.ext import commands
import os
from env import Token

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')

for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

@bot.command(name="load")
async def load(ctx, cog: str):
    if ctx.message.author.id == int(os.getenv('Dev')):
        bot.load_extension(f"cogs.{cog}")
        await ctx.send(f"Loaded {cog}")
        
async def unload(ctx, cog: str):
    if ctx.message.author.id == int(os.getenv('Dev')):
        bot.unload_extension(f"cogs.{cog}")
        await ctx.send(f"Unloaded {cog}")

if __name__ == "__main__":
    bot.run(Token)
    