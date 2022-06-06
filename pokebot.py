import discord

import random

# APPLICATION ID
# 968951321241735278

# PUBLIC KEY
# 6207e367e63047640489bbb22e2d3d38287bea160bd04da1313124e835d9ebde

# BOT TOKEN
TOKEN = "OTY4OTUxMzIxMjQxNzM1Mjc4.YmmUPQ.H8C-v9DKZS1s3qWym5c1-F0m5bM"

# OAuth2 URL
# https://discord.com/api/oauth2/authorize?client_id=968951321241735278&permissions=8&scope=bot

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
        if 'up' in user_message.lower():
            await message.channel.send(f'{username} moved up')
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
        elif 'r bumper' in user_message.lower():
            await message.channel.send(f'{username} pressed R bumper')
            return
        elif 'l bumper' in user_message.lower():
            await message.channel.send(f'{username} pressed L bumper')
            return
        elif 'start' in user_message.lower():
            await message.channel.send(f'{username} pressed start')
            return
        elif 'select' in user_message.lower():
            await message.channel.send(f'{username} pressed select')
            return
        elif 'press a' in user_message.lower():
            await message.channel.send(f'{username} pressed A')
            return
        elif 'press b' in user_message.lower():
            await message.channel.send(f'{username} pressed B')
            return
        elif 'confus' in user_message.lower():
            await message.channel.send('https://media4.giphy.com/media/6nWhy3ulBL7GSCvKw6/giphy.gif')
            return


    if user_message.lower() == '!anywhere':
            await message.channel.send('This can be seen anywhere')
            return

    

client.run(TOKEN)