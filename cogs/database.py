import nextcord
from nextcord.ext import commands
import sqlite3


class DATABASE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="null")
    @commands.is_owner()
    async def null(self,ctx): 
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM messages')
        conn.commit()
        conn.close()
        await ctx.send("Data Clear NULL DB")

    @commands.command(name="insert")
    @commands.is_owner()
    async def insert(self,ctx,*,args):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO messages (content) VALUES (?)', (str(args),))
        conn.commit()
        conn.close()
        await ctx.send(f"1 Data Inserted")

    @commands.command(name="insert_all")
    @commands.is_owner()
    async def insert_all(self,ctx,*,args):
        data = str(args).split(',')
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        
        count = 0
        for i in data:
            cursor.execute('INSERT INTO messages (content) VALUES (?)', (i,))
            count += 1
        conn.commit()
        conn.close()
        await ctx.send(f"{str(count)} Data Inserted")

    @commands.command(name="printdatabse")
    @commands.is_owner()
    async def printdatabse(self,ctx):
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM messages')

        rows = cursor.fetchall()


        for row in rows:
            await ctx.send(f"```\nID: {row[0]} Content: {row[1]}\n```")

        conn.close()


def setup(bot):
    bot.add_cog(DATABASE(bot))




        