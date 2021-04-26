#bot.py
import os, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.target_channel = client.get_channel(817324280651186186)


@client.command(name='live', help='Sends message to secified channel with costom message')
async def update(ctx, msg='stannge is live!'):
    print(msg)

    if not isinstance(ctx.channel, discord.channel.DMChannel):
        print('not dm')
        return


    if(ctx.author.id != 306970895988162572 and ctx.author.id != 328589466388267018):
        print('not from correct person')
        return

    msg = '@everyone ' + msg + ' https://www.twitch.tv/stannage'
    await client.target_channel.send(msg)

client.run(TOKEN)