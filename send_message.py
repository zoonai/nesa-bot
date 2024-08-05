import discord
from discord.ext import tasks

TOKEN = 'YOUR_USER_TOKEN_HERE'  # Ganti dengan token akun pengguna Anda
CHANNEL_ID = 123456789012345678  # Ganti dengan ID channel yang diinginkan

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')
    send_message.start()

@tasks.loop(hours=1, minutes=1)
async def send_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send('!work')
    else:
        print('Channel not found')

client.run(TOKEN)
