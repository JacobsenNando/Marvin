import discord
import os
from keys import BOT_KEY

class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user.id})')
    print('------')

  async def on_message(self, message):
    # we do not want the bot to reply to itself
    if message.author.id == self.user.id:
      return

    if message.content.startswith('!hi'):
      await message.reply('Hi!', mention_author=False)

    if message.content.startswith('!local'):
      embed = discord.Embed(title='Contato',
                            description='''51 30568251 
          Matriz: Rua Manoel Antônio de Barros, 290 - 96810-370
          
          Comercial: Rua Ramiro Barcelos, 1056 - 96810-054

          Vera Cruz:Rua Cláudio Manoel, 34 - 96880-000
          
          ''',
                            color=0x0000ff)
      await message.reply(embed=embed, mention_author=True)

  
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get(BOT_KEY))
