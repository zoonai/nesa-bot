import discord
from discord.ext import tasks
import asyncio

ACCOUNTS = [
    {
        'token': 'YOUR_USER_TOKEN_HERE', # Ganti dengan token akun pengguna Anda
        'channel_id': 123456789012345678 # Ganti dengan ID channel yang diinginkan
    }
    # Tambahkan akun lain di sini
]

class MyClient(discord.Client):
    def __init__(self, token, channel_id):
        super().__init__()
        self.token = token
        self.channel_id = channel_id

    async def on_ready(self):
        print(f'Logged Discord as {self.user}!')
        self.send_message.start()

    @tasks.loop(hours=1, minutes=2)
    async def send_message(self):
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send('!work')
        else:
            print('Channel not found')

    def run_bot(self):
        self.run(self.token)

clients = []

for account in ACCOUNTS:
    client = MyClient(account['token'], account['channel_id'])
    clients.append(client)

async def main():
    await asyncio.gather(*(client.start(client.token) for client in clients))

asyncio.run(main())
