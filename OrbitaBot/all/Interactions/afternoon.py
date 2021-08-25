dia = {'Boa tarde', 'Boa tarde!', 'boa tarde', 'boa tarde!'}
DIA = {'BOA TARDE', 'BOA TARDE!'}
async def say_aft(self):
  for i in dia:
    if i == self.content:
      await self.reply('Bom tarde!')
    else:
      pass

  for e in DIA:
    if e == self.content:
      await self.reply('BOA TARDE, CARALHO!')
    else:
      pass