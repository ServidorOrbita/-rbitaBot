import discord
from datetime import datetime

async def reply_embed(self, cli):
    if self.content.startswith('*'):

      # EMBEDED
      if 'help' in self.content:
        embed = discord.Embed(title="Comandos:", description="", colour=0x483D8B, timestamp=datetime.utcnow())

        embed.set_thumbnail(url='https://i.imgur.com/AhHZ2mJ.gif')

        embed.add_field(name="Prefixo:", value="`*`", inline=False)

        embed.add_field(name="Geral:", value='`help` `ping` `paulo guedes` `paulo kogos` `gafeu` `ciencia` `zap` `massagem@user`', inline=False)

        embed.add_field(name="Lives:", value="`orbitancap` `duduxqx`", inline=False)

        embed.add_field(name="Mods:", value="`say`", inline=False)

        embed.add_field(name="Converse com o Bot:", value="`Bom dia` `Boa tarde` `Boa noite` `Oi` `F` `Bolsonaro`", inline=False)

        embed.add_field(name="Contribua com o meu desenvolvimento!", value="Link: https://github.com/ServidorOrbita", inline=False)

        embed.set_footer(text = 'Órbita Bot - by OGabrielPereira - written in Python')
        
        await self.reply(embed = embed)

      else:
        pass
