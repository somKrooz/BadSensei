from nextcord.ext import commands
import sqlite3

class smartcontrols(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        words = ["tool","dev","python","api","coding","docker","scraped","server","script","hardcoded"]
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute('SELECT content FROM messages ORDER BY RANDOM() LIMIT 1')
        random_message = cursor.fetchone()
        conn.close()
        
        message_content = message.content.lower()
        if message.author != self.bot.user:
            for word in words:
                if word in message_content:
                    await message.channel.send(f"**{random_message[0]}**")
                    break


def setup(bot):
    bot.add_cog(smartcontrols(bot))

    
