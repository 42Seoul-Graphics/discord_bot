import discord
import os
from dotenv import load_dotenv
import text_util
import datetime

# 짝수주에는 확인하지 않음
# if datetime.datetime.now().isocalendar()[1] % 2 == 0:
# 	exit(0)

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

  
class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        #  TODO: 조건에 따른 메시지 작성
        uncompleted_members = text_util.get_uncompleted_member()
        await channel.send(f"이번회차에는 {uncompleted_members}님이 안했어요. 다음에는 꼭 해봐요!")
        await self.close()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
