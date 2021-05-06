#main.py
import os, discord
from dotenv import load_dotenv
from discord.ext import commands
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.target_channel = client.get_channel(817324280651186186)

    with open('commands.json') as json_file:
        client.custom_commands = json.load(json_file)
        print(client.custom_commands)


@client.event
async def on_message(msg):

    if(msg.content[0] != client.command_prefix):
        return

    key = msg.content[1::]


    if(msg.content[1::] in client.custom_commands.keys()):
        await msg.channel.send(client.custom_commands[key])
        


@client.command(name='twitch', help='Sends a message to stannage\'s live channel with the twitch link')
async def twitch(ctx, msg='stannge is live!'):
    print(msg)

    if not isinstance(ctx.channel, discord.channel.DMChannel):
        print('not dm')
        return


    if(ctx.author.id != 306970895988162572 and ctx.author.id != 328589466388267018):
        print('not from correct person')
        return

    await client.target_channel.send(msg + ' https://www.twitch.tv/stannage')

@client.command(name='live', help='Sends a message to stannage\'s live channel')
async def live(ctx, msg):

    if not isinstance(ctx.channel, discord.channel.DMChannel):
        print('not dm')
        return


    if(ctx.author.id != 306970895988162572 and ctx.author.id != 328589466388267018):
        print('not from correct person')
        return

    await client.target_channel.send(msg)


@client.command(name='addcommand', help='adds a command')
async def addcommand(ctx, call, response):

    if not isinstance(ctx.channel, discord.channel.DMChannel):
        print('not dm')
        return

    if(ctx.author.id != 306970895988162572 and ctx.author.id != 328589466388267018):
        print('not from correct person')
        return

    print(call + ' ' + response)

    client.custom_commands[call] = response
    print(client.custom_commands)


    with open('commands.json','w') as outfile:
        json.dump(client.custom_commands, outfile)

client.run(TOKEN)