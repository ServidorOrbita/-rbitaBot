dia = {'Bom dia', 'Bom dia!', 'bom dia', 'bom dia!'}
DIA = {'BOM DIA', 'BOM DIA!'}
async def say_mor(self):
  for i in dia:
    if i == self.content:
      await self.reply('Bom dia!')
    else:
      pass

  for e in DIA:
    if e == self.content:
      await self.reply('BOM DIA, CARALHO!')
    else:
      pass
  