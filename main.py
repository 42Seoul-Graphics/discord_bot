import discord
import os
from dotenv import load_dotenv
import text_util

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

  
class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        #  TODO: 조건에 따른 메시지 작성
        uncompleted_members = text_util.getUnCompletedMember()
        # await channel.send(text)
        print(f"열심히 하세요. : {uncompleted_members}")
        await self.close()
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
