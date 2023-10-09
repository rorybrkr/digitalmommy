import discord
import random

TOKEN = 'MTE2MDg2NDQ5NTQwMTQ1MTUyMA.GuVkh6.s7ou4WjmDzwGo3SNmUNX9aIJ3KG_HSZt62UXUg'
PREFIX = '!'

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{PREFIX}losuj'):
        category = message.content[len(f'{PREFIX}losuj'):].strip().lower()

        if category == 'psy':
            file_path = 'http://lists.cultofdumb.com/koty.txt'
        elif category == 'koty':
            file_path = 'http://lists.cultofdumb.com/koty.txt'
        elif category == 'ptaki':
            file_path = 'http://lists.cultofdumb.com/koty.txt'
        else:
            await message.channel.send('Dostępne kategorie: Psy, Koty, Ptaki')
            return

        try:
            with open(file_path, 'r') as file:
                videos = file.read().splitlines()
                random_video = random.choice(videos)
                await message.channel.send(f'Losowy film z kategorii {category}:', file=discord.File(random_video))
        except FileNotFoundError:
            await message.channel.send(f'Brak pliku dla kategorii {category}')

client.run(TOKEN)
