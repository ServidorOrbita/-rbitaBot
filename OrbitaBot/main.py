# GERAL - GERAL - GERAL
import discord
import os
from keep_alive import keep_alive

# GERAL - GERAL - GERAL

# IMPORTANDO FUNÇÕES - IMPORTANDO FUNÇÕES

from all.Embed import embed
from all.Interactions import oi, morning, afternoon, f
from all.WelBye import welcome

# IMPORTANDO FUNÇÕES - IMPORTANDO FUNÇÕES

class MyClient(discord.Client):

    async def on_ready(self):
        print('---------------------------------------------------')
        print(f'Conectado como {self.user.name}, id = {self.user.id}')
        print('---------------------------------------------------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


    async def on_message(self, message):
      if message.author.id == self.user.id:
        return

      await embed.reply_embed(message, client)
      await oi.say_hi(message)
      await morning.say_mor(message)
      await f.respect(message)
      await afternoon.say_aft(message)

      

keep_alive()

intents = discord.Intents.default()
intents.members = True

my_secret = os.environ['token']

client = MyClient(intents=intents)
client.run(my_secret)