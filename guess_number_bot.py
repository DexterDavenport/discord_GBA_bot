import discord

import random

TOKEN = "OTY4OTUxMzIxMjQxNzM1Mjc4.YmmUPQ.H8C-v9DKZS1s3qWym5c1-F0m5bM"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == "play-game":
        if '1' in user_message.lower():
            await message.channel.send(f'Radnom number: {"{:,}".format(random.randint(1,1000000000000))}')
            return
        elif 'down' in user_message.lower():
            await message.channel.send(f'{username} moved down')
            return
        elif 'left' in user_message.lower():
            await message.channel.send(f'{username} moved left')
            return
        elif 'right' in user_message.lower():
            await message.channel.send(f'{username} moved right')
            return
        elif 'confus' in user_message.lower():
            await message.channel.send('https://media4.giphy.com/media/6nWhy3ulBL7GSCvKw6/giphy.gif')
            return

    if user_message.lower() == '!anywhere':
            await message.channel.send('This can be seen anywhere')
            return

    

client.run(TOKEN)