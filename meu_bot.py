import discord
import os
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True
from time import sleep

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}', format(message))
        if message.content == '?regras':
            await message.channel.send(f'**{message.author.name} seu lindo!**{os.linesep}As regras do servidor são: {os.linesep}1. Não desrespeitar os membros{os.linesep}2. Respeitar a 1ª regra{os.linesep}{os.linesep}\t\t\t**Divirta-se!** :star_struck:')



client = MyClient(intents=intents)
client.run('MTA2MjQ4MDI0MzU4OTM5ODYwMQ.Grh0pY.x7JH3r9rRE1Ckb_OxH8euMRodDUi3neXONMAyM')
