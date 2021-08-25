f = {'f', 'F'}
async def respect(self):
  for i in f:
    if self.content == i:
      await self.reply('F')