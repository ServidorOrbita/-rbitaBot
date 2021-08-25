oi = ['oi', 'OI', 'Oi', 'oI', 'Oii', 'Oi!', 'Oii!']
async def say_hi(self):
  for i in oi:
    if self.content == i:
      await self.reply('Oi!')