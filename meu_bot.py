import discord
from discord.ext import commands
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
         # Imprime a mensagem no console
        print('Message from {0.author}: {0.content}', format(message))

         # Verifica se a mensagem é ?regras e envia uma mensagem de regras para o canal
        if message.content == '?regras':
            await message.channel.send(f'**\t\t\t\tOlá {message.author.name}!**{os.linesep}Cumpra sempre as regras do servidor: {os.linesep}1. Não desrespeitar os membros;{os.linesep}2. Respeitar a 1ª regra; e{os.linesep}{os.linesep}\t\t\t\t**Divirta-se!** :star_struck:')

        # Verifica se a mensagem é ?nivel e envia uma mensagem de nível para o autor da mensagem.
        elif message.content == '?nivel':
            await message.author.send('Nível 1') 

        # Verifica se a mensagem é ?limpar
        elif message.content.startswith('?limpar'):

            # Verifica se o usuário tem permissão para excluir mensagens
            if message.author.guild_permissions.manage_messages:
                 # Define o valor padrão de mensagens a serem excluídas
                amount = 100
                if len(message.content.split()) > 1:
                    amount = int(message.content.split()[1])
                async def clear(channel, amount=amount):
                    messages = []
                    async for message in channel.history(limit=amount):
                        messages.append(message)
                    await channel.delete_messages(messages)
                    await message.channel.send(f'Mensagens deletadas: {amount}')
                await clear(message.channel)
            else:
                await message.channel.send('Você não tem permissão para excluir mensagens.')

    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Seja bem vindo(a) ao {guild.name} :wave: :wave:!'
            await guild.system_channel.send(mensagem)


client = MyClient(intents=intents)
client.run('MTA2MjQ4MDI0MzU4OTM5ODYwMQ.Grh0pY.x7JH3r9rRE1Ckb_OxH8euMRodDUi3neXONMAyM')
